import sqlite3 as sql
from werkzeug.security import generate_password_hash, check_password_hash


users_schema = f"""
create table if not exists users (
    id integer primary key autoincrement,
    username text unique not null,
    password text
)
"""
user_nutrient_schema = f""" 
create table if not exists user_nutrients (
    id integer primary key,
    kcal int,
    protein int,
    glucid int,
    lipid int,
    foreign key (id) references users (id) on delete cascade
    )
"""

def register_user(username : str, password : str, co : sql.Connection ) :
    password_hash = generate_password_hash(password)
    cursor = co.cursor()
    cursor.execute("insert into users (username, password) values (?,?)", (username.lower(),password_hash))
    co.commit()
    
    return cursor.lastrowid

def log_in(username: str, password : str, co : sql.Connection):
    user = co.execute("select * from users where username == ? ", [username.lower()] ).fetchone()
    if user is None:
        return 
    success = check_password_hash(user["password"], password)
    if not success:
        return
    
    return user

def user_nutrients(user_id : int, co : sql.Connection):
    return co.execute("select * from user_nutrients where id == (?)", [user_id]).fetchone()

def get_user(user_id : int, co : sql.Connection):
    return co.execute("select * from users where id == (?)", [user_id]).fetchone()

def set_user_nutrients(user_id : int, nutris : dict, co : sql.Connection):
    """
    The nutris dict has to conform with the nutrient's table's schema
    """
    user_nutris = co.execute("select (id) from user_nutrients where id == ?", [user_id]).fetchone()
    print("=============", nutris)
    placeholders = ",".join([f"{k} = ?" for k in nutris.keys()])
    print(f"update {placeholders} where id == ?")
    co.execute(f"update user_nutrients set {placeholders} where id == ?", list(nutris.values()) + [user_id])
    co.commit()
    
if __name__ == "__main__":
    co = sql.connect("users.db")
    co.execute("PRAGMA foreign_keys = ON;")
    co.execute(users_schema)
    co.execute(user_nutrient_schema)
    co.commit()
    