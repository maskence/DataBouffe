#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:20:56 2023

@author: jak
"""

import requests


host = "http://localhost:5000"
def test_register(username, password):
    payload = {
        'username': username,
        'password': password
    }
    headers = {'Content-Type': 'application/json'}
    
    resp = requests.post(host + "/api/register", json=payload, headers=headers )
    return resp

def test_login( username, password):
    payload = {
        'username': username,
        'password': password
    }
    resp = requests.post(host + '/api/login', json=payload)
    return resp

def test_goals(token):
    cookies = {'access_token_cookie': token}
    resp = requests.post(host + '/api/goals', cookies=cookies, json={"glucid":150,"protein":100})
    resp2 = requests.get(host + '/api/goals', cookies=cookies)
    return resp, resp2

import random
username = "okklssoyu" + str(random.randint(0,100000000))
password = "chancla"

resp = test_register(username, password)
print(resp.status_code)
print(resp.json())

resp = test_login(username, password)
print(resp.json())
jwt = resp.cookies["access_token_cookie"]

resp, resp2 = test_goals(jwt)
print("test goals", jwt, resp, resp2.json())

resp_meals = requests.get(host + '/api/meal_plan', cookies = {'access_token_cookie': jwt})
print(resp_meals.text)
