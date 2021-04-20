from fastapi import APIRouter
from Application.Food.Fooding import get_food, get_listFood, add_food, Food


foods_router = APIRouter()


@foods_router.get(
    "/Food/ListFood",
    name="data:food"
)
def get_listFoods():
    return get_listFood()


@foods_router.get(
    "/Food/Description",
)
def get_foods(food_name : str):
    return get_food(food_name)

@foods_router.post(
    "/add_food"
)
def _add_food(_food : Food):
    return add_food(_food)
