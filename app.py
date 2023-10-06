#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:12:46 2023

@author: jak
"""
import sqlite3 as sql

from flask import Flask, request, g, Response, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from users import register_user, log_in, user_nutrients, set_user_nutrients
from lib import df_meals, default_daily_goals, get_meal_plan
from utils import dict_from_row

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fillboosted'
jwt = JWTManager(app)

def get_users_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect("users.db", check_same_thread=False)
        db.execute("PRAGMA foreign_keys = ON;")
        db.row_factory = sql.Row
    return db



@app.route("/api/register", methods = ["POST"])
def register_route():
    data = request.get_json()
    
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return {"message","no username or password provided"},400
    
    co = get_users_db()
    
    try:
        register_user(username, password, co)
    except sql.IntegrityError:
        return {"message": "username already taken"}, 400
    except Exception:
        return {"message":"unknown error"}, 400
    
    return {"message":"registerd sccuessfully"} ,200

@app.route("/api/login", methods = ["POST"])
def login_route():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    
    co = get_users_db()
    user = log_in(username, password, co)
    if user is None:
        return {"message": "username or password invalid"}, 400
    else:
        access_token = create_access_token(identity=user["id"])
        return jsonify(access_token=access_token) ,200
    
@app.route("/api/infos", methods = ["POST", "GET"])
@jwt_required()
def info_route():
    user_id = get_jwt_identity()
    print("USER ID", user_id)
    co = get_users_db()
    
    if request.method == "GET":
        nutris = user_nutrients(user_id, co)
        if nutris is None:
            return {"error":"user infos not set"}, 400
        else:
            return dict(nutris),200 
        
    if request.method == "POST":
        nutris = request.get_json()
        set_user_nutrients(user_id, nutris, co)
        return '', 200

@app.route("/api/meal_plan")
@jwt_required()
def meal_plan_route():
    user_id = get_jwt_identity()
    co = get_users_db()
    
    goals_row = user_nutrients(user_id, co)
    if goals_row is None:
        return {'message': 'user infos not set'}, 400
    
    #fill missing nutris with default values
    goals = dict(goals_row)
    goals.pop("id")
    goals = {k:v if v is not None else default_daily_goals[k] for k,v in goals.items()}
    
    meals = get_meal_plan(df_meals, goals, tolerance=0.2)
    
    return meals.to_dict(), 200
    

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()