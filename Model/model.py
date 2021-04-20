from sqlalchemy import MetaData
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime, Integer, String, Float, Boolean, Text

meta = MetaData()

user_infomation = Table(
    'user_infomation', meta,
    Column('username', String(50), primary_key=True),
    Column('hashpassword', String(50)),
    Column('email', String(50)),
    Column('firstname', String(50)),
    Column('lastname', String(50)),
    Column('old_user', Integer),
    Column('address', String(50)),
    Column('isactive', Boolean),
    mysql_engine='InnoDB'
)


category = Table(
    'category', meta,
    Column('name_category', String(50), primary_key=True),
    Column('image_url', Text),
    mysql_engine='InnoDB'
)

food = Table(
    'food', meta,
    Column('name_food', String(50), primary_key=True),
    Column('name_category', String(50), ForeignKey(category.c.name_category), nullable=False),
    Column('price', Float),
    Column('food_description', String(50)),
    Column('url_image', String(50)),
    mysql_engine='InnoDB'
)


order_user = Table(
    'order_user', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(50), ForeignKey(user_infomation.c.username), nullable=False),
    Column('name_food', String(50), ForeignKey(food.c.name_food), nullable = False),
    Column('number_food', String(50), nullable = False),
    Column('time_order', DateTime, nullable = False),
    Column('address', String(50), nullable = False),
    Column('total_money',Float, nullable = False),
    mysql_engine='InnoDB'
)

