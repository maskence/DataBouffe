#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:12:46 2023

@author: jak
"""
import sqlite3 as sql

from flask import Flask, request, g, Response, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from users import register_user, log_in
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
        res = co.execute("select * from user_nutrients where id == (?)", [user_id]).fetchone()
        if res is None:
            return {"error":"user infos not set"}, 400
        else:
            return dict(res),200 
        
    if request.method == "POST":
        nutris = request.get_json()
        nutri_cols = ",".join(nutris.keys())
        placeholders = ",".join("?"*len(nutris))
        co.execute(f"insert into user_nutrients (id,{nutri_cols}) values (?,{placeholders})", [user_id]+list(nutris.values()) )
        co.commit()
        return '', 200
    

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()