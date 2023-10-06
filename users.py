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
    protein int,
    iron int,
    foreign key (id) references users (id) on delete cascade
    )
"""

def register_user(username : str, password : str, co : sql.Connection ) :
    password_hash = generate_password_hash(password)
    co.execute("insert into users (username, password) values (?,?)", (username.lower(),password_hash))
    co.commit()

def log_in(username: str, password : str, co : sql.Connection):
    user = co.execute("select * from users where username == ? ", [username.lower()] ).fetchone()
    if user is None:
        return 
    success = check_password_hash(user["password"], password)
    if not success:
        return
    
    return user

    
if __name__ == "__main__":
    co = sql.connect("users.db")
    co.execute("PRAGMA foreign_keys = ON;")
    co.execute(users_schema)
    co.execute(user_nutrient_schema)
    co.execute("insert into user_nutrients (iron) values ( ?)", (100,))
    co.commit()
    