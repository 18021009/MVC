from sqlalchemy.sql.expression import select
from Model.db_url import db_url
from sqlalchemy import create_engine
from Model.model import user_infomation as user
from pydantic import BaseModel

class signup_infomation(BaseModel):
    username: str
    hashpassword: str
    email: str
    firstname: str
    lastname: str
    old_user: int = None
    address: str = None
    isactive: bool = True


def signup(_signup_infomation : signup_infomation):
    try:
        create_engine(db_url).connect().execute(user.insert().values(
            username = _signup_infomation.username, 
            hashpassword = _signup_infomation.hashpassword,
            email = _signup_infomation.email,
            firstname = _signup_infomation.firstname,
            lastname = _signup_infomation.lastname,
            old_user = _signup_infomation.old_user,
            address = _signup_infomation.address,
            isactive = _signup_infomation.isactive
            ))
        return "success"
    except:
        return "error"

