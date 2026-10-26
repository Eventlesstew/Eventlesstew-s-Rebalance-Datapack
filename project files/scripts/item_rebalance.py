from item_class.item import *
from item_class.food_item import *

import json

create_compost = True

compost_path = "data/event_rebalance/item_modifier/compostable/apply.json"

compost_values = []

def add_food_item(item_key: str):
    if item_key == "default":
        return 
    
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
        if item_object.has_changes():
            item_object.save()

    return item_object


item_keys = data_file.keys()

for item_key in item_keys:
    item_object = add_food_item(item_key)

    if item_object:
        if create_compost:
            compost = item_object.get_compost_value()

            if compost:
                compost_values.append({
                    "type": "filtered",
                    "item_filter": item_object.get_item_filter(),
                    "on_pass": "event_rebalance:compostable/" + str(int(compost * 100))
                })

if create_compost:
    compost_file = {
        "type":"sequence",
        "functions":compost_values
    }
    with open(compost_path, "w") as file:
        file.write(json.dumps(compost_file,indent=4))
