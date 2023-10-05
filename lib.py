#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:40:06 2023

@author: jak
"""

import itertools
import random 

import pandas as pd
import numpy as np

#rang 3120 à retirer, dupliqua de 3121 mais avec des infos manquantes

# les recettes et les ingrédiants sont mélangés, certaines recettes necessitent des accompagnements
# et d'autres non, ex:
# 'Meloukhia, plat à base de boeuf et corete, fait maison' <- plat complet
# 'Merguez, pur boeuf, crue' <- à complèter par des accompagnements

#values from https://fr.wikipedia.org/wiki/Apports_journaliers_recommand%C3%A9s
daily_goals = {"kcal": 2000,
               'proteins': 50,
               'glucids': 260,
               'lipids': 70}
def str_to_float(val):
    """ 
    kcal values are sometimes float, sometimes '-' to indicate missing values and sometimes 
    strings of european floating point nation (ex: '29,7'), converts all those to float
    """
    if type(val) == str:
        if val == '-':
            return np.nan
        if val == 'traces':
            return 0
        else:
            # treats entries like proteins : '< 0,5'
            if '<' in val:
                val = val.replace("<",'')
            return float(val.replace(",","."))
    return val

def load_ciqual_dataset(path : str) -> pd.DataFrame:
    df = pd.read_excel(path)
    df.rename(columns={
        "Energie, Règlement UE N° 1169/2011 (kcal/100 g)":"kcal",
        "alim_nom_fr":"name",
        "Protéines, N x 6.25 (g/100 g)":"proteins",
        "Glucides (g/100 g)": "glucids",
        "Lipides (g/100 g)":"lipids"}, inplace=True)
    
    for col_name in daily_goals.keys():
        df[col_name] = df[col_name].apply(str_to_float)
    
    #duplicate columns with different units
    df.drop(['Energie, Règlement UE N° 1169/2011 (kJ/100 g)',
    'Energie, N x facteur Jones, avec fibres  (kJ/100 g)',
    'Energie, N x facteur Jones, avec fibres  (kcal/100 g)',
    'Eau (g/100 g)', 'Protéines, N x facteur de Jones (g/100 g)'], axis=1)
    
    return df

def solve_naive(n_meals, all_meals, objective, tolerance, n_results=10):
    results = []
    
    all_meals_idx = list(range(len(all_meals)))
    
    i=0
    for meal_plan_idx in itertools.combinations(all_meals_idx, n_meals):
        meal_plan = all_meals[list(meal_plan_idx)]
        loss = compute_loss(meal_plan, objective)
        print(loss)
        
        i+=1
        if loss <= tolerance:
            results.append({"ids":meal_plan_idx,"nutrients": np.sum(meal_plan,axis=0) ,"loss": loss } )
            if len(results) == n_results:
                print(f"took {i} steps" )
                return results

def solve_heuristic(n_meals, all_meals, objective, tolerance, n_results):
    current_meals_idx = random.sample(range(len(all_meals)), n_meals)
    current_meals = all_meals[current_meals_idx]
    

    best_loss = compute_loss(current_meals, objective)
    for i in range(20):
        current_meals = current_meals[random.sample(range(len(current_meals)), len(current_meals))]
        t = current_meals[1:]
        all_diffs = [compute_loss(np.vstack([m, t]),objective) for m in all_meals]
        new_meals = np.vstack([all_meals[np.argmin(all_diffs)],t])
        new_loss = compute_loss(new_meals, objective)
        print(new_loss, best_loss, "\n")
        if new_loss < best_loss:
            best_loss = new_loss
            current_meals = new_meals
    
    print("optimal loss", best_loss)
    return current_meals

    
def compute_loss(meal_plan, objective):
    ratio_losses = np.sum(meal_plan, axis=0) / objective -1
    return np.linalg.norm( ratio_losses ,2)

def solve_naive(current_plan, all_meals, objective):
    n_meals = len(current_plan)
    all_meals_idx = list(range(len(all_meals)))
    
    for meal_plan_idx in itertools.combinations(all_meals_idx, n_meals):
        meal_plan = all_meals[list(meal_plan_idx)]
        yield meal_plan_idx, compute_loss(meal_plan, objective)
        
def solve_swap(current_plan, all_meals, objective, temperature = 5, cooling_factor = 0.001):
    n_meals = len(current_plan)
    best_loss = compute_loss(all_meals[current_plan], objective)
    
    steps = 1
    while True:
        new_plan = current_plan.copy()
        new_meal = np.random.randint(0, len(all_meals)-1)
        new_plan[steps%n_meals] = new_meal
        #print(f"swapping {new_plan[i]} at index {i} for {new_meal}")
        
        loss = compute_loss(all_meals[new_plan], objective)
        
        yield new_plan, loss
        
        
        if loss < best_loss: #+ (temperature*(1-cooling_factor) ** steps) :
            current_plan = new_plan
            best_loss = loss
        steps += 1


    
if __name__ == "__main__":
    import time
    
    df = load_ciqual_dataset("ciqual.xls")
    df_meals = df[(df["alim_grp_nom_fr"] ==  "entrées et plats composés") & (~df["kcal"].isna()) ]
    #df_plats = df_plats.sample(frac = 1)
    
    n_days = 7
    meals_per_day = 2
    n_meals = n_days * meals_per_day
    
    all_meals = df_meals[list(daily_goals.keys())].to_numpy() * 5#00g per meal
    
    #objective_plan = np.random.choice(len(all_meals), n_meals)
    #objective = np.sum(all_meals[objective_plan], axis = 0)
    objective = np.array(list(daily_goals.values())) * n_days
    
    best_plan = list(range(n_meals))
    best_loss = compute_loss(all_meals[best_plan], objective)
    print("initial loss : ", best_loss,"\n")
    
    start_time = time.time()
    tolerance = 0.05
    steps = 0
    try :
        for plan_ids, loss in solve_swap(best_plan, all_meals, objective):
            #print(plan_ids, loss)
            steps +=1
            if loss < best_loss:
                best_loss = loss
                best_plan = plan_ids
                
                if loss < tolerance:
                    break
    except KeyboardInterrupt:
        pass
    
    #print("objective plan :", objective_plan)
    print("objective :", objective, '\n')

    plan_value = np.sum(all_meals[best_plan], axis=0)
    print("found plan :", best_plan)
    print("plan value :", plan_value, '\n')

    print("loss :", best_loss)
    print("steps taken :", steps)
    print("time taken :", time.time() - start_time, "\n")
    
    meals = df_meals.iloc[best_plan]
    
    print("meals :", list(meals["name"]))
    #print("objective meals : ", list(df_meals.iloc[objective_plan]["name"]))
    

