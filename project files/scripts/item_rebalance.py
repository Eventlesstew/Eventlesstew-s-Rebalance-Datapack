from item_class.item import *
from item_class.food_item import *


def add_food_item(item_key: str):
    item_class = "default"
    if "item_class" in data_file[item_key]:
        item_class = data_file[item_key]["item_class"]

    item_object = None
    if item_class == "food":
        item_object = food_item(item_key)
    elif item_class == "tiered":
        pass
    elif item_class == "template":
        pass
    else:
        item_object = item(item_key)

    if item_object:
        item_object.save()


item_keys = data_file.keys()

for item_key in item_keys:
    if item_key != "default":
        add_food_item(item_key)
