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

def test_info(token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = requests.post(host + '/api/infos', headers=headers, json={"protein":100})
    resp2 = requests.get(host + '/api/infos', headers=headers)
    return resp, resp2
username = "issoyu"
password = "chancla"

resp = test_register(username, password)
print(resp.status_code)
print(resp.json())

resp = test_login(username, password)
print(resp)
jwt = resp.json()["access_token"]

resp, resp2 = test_info(jwt)