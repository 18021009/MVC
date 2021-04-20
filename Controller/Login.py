from fastapi import APIRouter
from sqlalchemy.sql.expression import text
from Application.user.login import login

login_routers = APIRouter()

@login_routers.post(
    "/login"
)
def _login(username: str, password: str):
    return login(username, password)