from fastapi import APIRouter

from Controller.Food import foods_router
from Controller.signup import signup_router
from Controller.Login import login_routers

data_router = APIRouter()
data_router.include_router(foods_router, tags=["datas"], prefix="/data")
data_router.include_router(login_routers, tags=["datas"], prefix="/data")
data_router.include_router(signup_router,tags=["datas"], prefix="/data")
# data_router.include_router(foods_router, tags=["data"], prefix="/data")
