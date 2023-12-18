#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:12:46 2023

@author: jak
"""
import sqlite3 as sql

from flask import Flask, request, g, Response, jsonify, make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, set_access_cookies, unset_jwt_cookies

from users import register_user, log_in, user_nutrients, set_user_nutrients, get_user
from lib import default_daily_goals, get_meal_plan, load_ciqual_dataset
from utils import dict_from_row

app = Flask(__name__)
CORS(app,supports_credentials=True)
app.config['SECRET_KEY'] = 'fillboosted'


jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'fillboosted'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token_cookie'
app.config['JWT_COOKIE_SECURE'] = False

df_meals = load_ciqual_dataset("ciqual.xls")

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
        user_id = register_user(username, password, co)
        set_user_nutrients(user_id, default_daily_goals, co)
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
        return {"msg": "username or password invalid"}, 400
    else:
        access_token = create_access_token(identity=user["id"])
        response = jsonify({'login': True})
        set_access_cookies(response, access_token)
        return response

@app.route('/api/logout', methods=['POST'])
def logout():
    response = jsonify({'msg': 'Logout successful'})
    unset_jwt_cookies(response)  
    return response

@app.route("/api/check_auth")
@jwt_required()
def check_auth_route():
    user_id = get_jwt_identity()
    co = get_users_db()
    user_row = get_user(user_id,co)
    return {"username": user_row["username"]}, 200  

@app.route("/api/goals", methods = ["POST", "GET"])
@jwt_required()
def goals_route():
    user_id = get_jwt_identity()
    print("USER ID", user_id)
    co = get_users_db()
    
    if request.method == "GET":
        nutris = dict(user_nutrients(user_id, co))
        nutris.pop("id")
        return nutris, 200 
        
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

    meal_nutris = meals[list(default_daily_goals.keys())].to_dict("records")
    meal_names, meal_ids = meals["name"],meals["alim_code"]

    meal_records = []
    for name, _id, nutri in zip(meal_names,meal_ids, meal_nutris):
        meal_records.append({"name" : name, "id" : _id, "nutrients" : nutri})
    
    return meal_records, 200
    

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.after_request
def after_request(response):
    print("Response Headers:", response.headers, response)
    return response
