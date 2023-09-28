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
        
def compute_loss(meal_plan, objective):
    #print("meal plan :",meal_plan)
    #print("abs losses :",np.sum(meal_plan) - objective)
    ratio_losses = np.abs( np.sum(meal_plan, axis=0) / objective -1)
    #print("ratio losses :", ratio_losses)
    return np.linalg.norm( ratio_losses ,2)
    
if __name__ == "__main__":
    df = load_ciqual_dataset("ciqual.xls")
    df_plats = df[(df["alim_grp_nom_fr"] ==  "entrées et plats composés") & (~df["kcal"].isna()) ]
    df_plats = df_plats.sample(frac = 1)
    
    n_days = 7
    meals_per_day = 2
    n_meals = n_days * meals_per_day
    
    all_meals = df_plats[list(daily_goals.keys())].to_numpy() * 5#00g per meal
    objective = np.array(list(daily_goals.values())) * n_days
    results = solve_naive(n_meals, all_meals, objective, tolerance=0.5, n_results=10)
    
    meal_plans = []
    for res in results:
        meal_plans.append(df_plats.iloc[list(res["ids"])][ ["name"] + list(daily_goals.keys()) ])
    
    
    

