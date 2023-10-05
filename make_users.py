import sqlite3 as sql
from lib import daily_goals

class User():
    def __init__(self, name, password, goals):
        self.name, self.password, self.goals = name, password, goals


co = sql.connect("users.db")


nutri_columns = ",\n".join([f"{k} float" for k in daily_goals.keys()])
users_schema = f"""
create table if not exists users (
    id integer primary key,
    name text unique,
    password text,
    {nutri_columns}
)
"""
co.execute(users_schema)

insert_user = f"insert into users (name, password, {','.join(daily_goals.keys())}) values (?,?, {','.join('?'*len(daily_goals))})"
print(insert_user,)
import random
username = "user-"+str(random.randint(0,100000000))
co.execute(insert_user, [username,"password"] + list(daily_goals.values()))

co.commit()

print(co.execute("select * from users").fetchall())