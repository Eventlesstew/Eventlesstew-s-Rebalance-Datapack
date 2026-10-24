import json
import csv

data_path = "project files/scripts/item_rebalance_data.json"
modifier_file_path = "project files/scripts/test/food_values.csv"

lore_base = {
    "italic": False,
    "color": "#1aa819",
}

with open(data_path, "r") as file:
    data_file = json.loads(file.read())


def is_effect_negative(effect_id: str):
    if effect_id in config["effect_sets"]["negative"]:
        return True
    else:
        return False


from item_class.item import *
from item_class.food_item import *


def get_food_value(item_key: str):
    if item_key == "default":
        return None
    item_class = "default"
    if "item_class" in data_file[item_key]:
        item_class = data_file[item_key]["item_class"]

    item_object = None
    if item_class == "food":
        item_object = food_item(item_key)

    if not item_object:
        return None

    return {"id": item_key, "value": item_object.get_value()}


item_keys = data_file.keys()
item_table = []

for item_key in item_keys:
    result = get_food_value(item_key)

    if result:
        item_table.append(result)

csv_table = []

for food in sorted(
    item_table, key=lambda food_value: food_value["value"], reverse=True
):
    csv_table.append([food["id"], food["value"]])
    print(food["id"], food["value"])

for i in csv_table:
    print(i)
with open(modifier_file_path, "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(csv_table)
print("CSV file created successfully")
