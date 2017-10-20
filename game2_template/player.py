from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
mass_list = [item_id["mass"] , item_laptop["mass"] , item_money["mass"]]
mass = item_id["mass"] + item_laptop["mass"] + item_money["mass"]

mass_of_all_items = [item_id["mass"], item_laptop["mass"], item_money["mass"],
item_handbook ["mass"], item_pen ["mass"],item_biscuits["mass"]]


all_items = [item_id , item_laptop , item_money , item_handbook  , item_pen  ,
item_biscuits ]


# Start game at the reception
current_room = rooms["Reception"]
