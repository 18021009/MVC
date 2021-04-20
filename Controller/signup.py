from fastapi import APIRouter
from Application.user.signup import signup, signup_infomation
from pydantic import BaseModel

signup_router = APIRouter()

@signup_router.post(
    "/signup"
)
def _signup(_signup_infomation : signup_infomation):
    return signup(_signup_infomation)