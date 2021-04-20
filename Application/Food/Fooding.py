from sqlalchemy.sql.expression import select
from pydantic import BaseModel
from Model.db_url import db_url
from sqlalchemy import create_engine
from Model.model import food as foodTabel


    

def get_food(food_name : str):
    try:
        result = []
        food_description = create_engine(db_url).connect().execute(select(foodTabel).where(foodTabel.c.name_food == food_name))
        for row in food_description:
            result.append(dict(row))
        return result[0]
    except:
        return "error"

def get_listFood():
        result = []
        list_food = create_engine(db_url).connect().execute(select(foodTabel))
        for row in list_food:
            result.append(dict(row))
        return result


class Food(BaseModel):
    name_food: str
    name_category: str
    price: float
    food_description: str
    image: str


def add_food(_food : Food):
    try:
        create_engine(db_url).connect().execute(foodTabel.insert().values(
            name_food = _food.name_food, 
            name_category = _food.name_category,
            price = _food.price,
            food_description = _food.food_description,
            url_image = _food.image
            ))
        return "success"
    except:
        return "error"

