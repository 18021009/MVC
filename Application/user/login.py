from sqlalchemy.sql.expression import select
from Model.db_url import db_url
from sqlalchemy import create_engine
from Model.model import user_infomation as user


def login(username: str, password: str):
    try:
        _user = []
        for row in create_engine(db_url).connect().execute(select(user).where(user.c.username == username)):
            _user.append(dict(row))


        if(password == _user[0]['hashpassword']):
            return "login success"
        else:
            return "login fail"
    except:
        return "error"

