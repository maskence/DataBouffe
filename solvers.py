#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:47:52 2023

@author: max
"""

import random
import numpy as np
import itertools

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
        
np.random.seed(0)

#all_meals = np.arange(300*10).reshape(300,10)
all_meals = np.random.uniform(0,100, size=(300,10))

n_meals = 7

objective_plan = np.random.choice(range(len(all_meals)),n_meals)
objective = np.sum(all_meals[objective_plan], axis=0)

best_plan = list(range(n_meals))
best_loss = compute_loss(all_meals[best_plan], objective)
print("initial loss : ", best_loss,"\n")

steps = 0
try :
    for plan_ids, loss in solve_swap(best_plan, all_meals, objective):
        #print(plan_ids, loss)
        steps +=1
        if loss < best_loss:
            best_loss = loss
            best_plan = plan_ids
            
            if loss == 0:
                break
except KeyboardInterrupt:
    pass

print("objective plan :", objective_plan)
print("objective :", objective, '\n')

plan_value = np.sum(all_meals[best_plan], axis=0)
print("found plan :", best_plan)
print("plan value :", plan_value, '\n')

print("loss :", best_loss)
print("steps taken :", steps)