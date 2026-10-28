from item_class.item import *
from item_class.food_item import *

import json

create_compost = True
create_furnace_fuel = True
create_brewing_fuel = True

compost_path = "data/event_rebalance/item_modifier/compostable"
furnace_fuel_path = "data/event_rebalance/item_modifier/furnace_fuel"
brewing_fuel_path = "data/event_rebalance/item_modifier/brewing_fuel"


def add_food_item(item_key: str):
    if item_key == "default":
        return

    item_class = "default"
    if "item_class" in data_file[item_key]:
        item_class = data_file[item_key]["item_class"]

    item_object = None
    if item_class == "food":
        item_object = food_item(item_key)
    elif item_class == "template":
        pass
    else:
        item_object = item(item_key)

    if item_object:
        item_object.save()

    return item_object


item_keys = data_file.keys()
compost_values = ["event_rebalance:modified"]
furnace_fuel_values = ["event_rebalance:modified"]
brewing_fuel_values = ["event_rebalance:modified"]


def create_fuel_data(fuel_type: str, tier:str=""):
    fuel = {}
    if fuel_type == "furnace":
        fuel = item_object.get_furnace_fuel(tier)
    elif fuel_type == "brewing":
        fuel = item_object.get_brewing_fuel(tier)

    if not "fuel" in fuel:
        return None

    fuel_value = fuel["fuel"]
    fuel_modifier_path = str(fuel_value)

    fuel_speed = 1
    if "fuel_speed" in fuel:
        fuel_speed = fuel["fuel_speed"]
        fuel_modifier_path += "x" + str(fuel_speed)

    with open(
        "data/event_rebalance/item_modifier/"
        + fuel_type
        + "_fuel/"
        + fuel_modifier_path
        + ".json",
        "w",
    ) as file:
        data = {
            "type": "sequence",
            "functions": [
                {"type": "set_components", "components": {}},
                {
                    "type": "set_lore",
                    "mode": "append",
                    "lore": [
                        {
                            "text": str(fuel_value),
                            "extra": [
                                " ",
                                {"translate": "attribute.name." + fuel_type + "_fuel"},
                            ],
                            "italic": False,
                            "color": "#AAAAAA",
                        }
                    ],
                },
            ],
        }

        if fuel_type == "furnace":
            data["functions"][0]["components"]["cooking_fuel"] = {
                "burn_time": int(fuel_value * 200),
                "speed_multiplier": fuel_speed,
            }
        elif fuel_type == "brewing":
            data["functions"][0]["components"]["brewing_fuel"] = {
                "uses": fuel_value,
                "speed_multiplier": fuel_speed,
            }

        if fuel_speed > 1:
            data["functions"][1]["lore"].append(
                {
                    "text": str(fuel_speed),
                    "extra": [
                        " ",
                        {"translate": "attribute.name." + fuel_type + "_fuel_speed"},
                    ],
                    "italic": False,
                    "color": "#AAAAAA",
                }
            )

        file.write(json.dumps(data, indent=4))

    return "event_rebalance:" + fuel_type + "_fuel/" + fuel_modifier_path


for item_key in item_keys:
    item_object = add_food_item(item_key)

    if item_object:
        item_tiers = [""]
        if item_object.uses_tiers():
            item_tiers = get_item_value(item_object.item_id, "tiers")

        for tier in item_tiers:
            item_filter = item_object.get_item_filter(tier)
            if create_compost:
                compost = item_object.get_compost_value(tier)

                if compost:
                    compost_values.append(
                        {
                            "type": "filtered",
                            "item_filter": item_filter,
                            "on_pass": "event_rebalance:compostable/"
                            + str(int(compost * 100)),
                        }
                    )

            if create_furnace_fuel:
                item_furnace_fuel_path = create_fuel_data("furnace", tier)
                if item_furnace_fuel_path:
                    furnace_fuel_values.append(
                        {
                            "type": "filtered",
                            "item_filter": item_filter,
                            "on_pass": item_furnace_fuel_path,
                        }
                    )

            if create_brewing_fuel:
                item_brewing_fuel_path = create_fuel_data("brewing", tier)
                if item_brewing_fuel_path:
                    brewing_fuel_values.append(
                        {
                            "type": "filtered",
                            "item_filter": item_filter,
                            "on_pass": item_brewing_fuel_path,
                        }
                    )


if create_compost:
    compost_file = {"type": "sequence", "functions": compost_values}
    with open(compost_path + "/apply.json", "w") as file:
        file.write(json.dumps(compost_file, indent=4))

if create_furnace_fuel:
    furnace_fuel_file = {"type": "sequence", "functions": furnace_fuel_values}
    with open(furnace_fuel_path + "/apply.json", "w") as file:
        file.write(json.dumps(furnace_fuel_file, indent=4))

if create_brewing_fuel:
    brewing_fuel_file = {"type": "sequence", "functions": brewing_fuel_values}
    with open(brewing_fuel_path + "/apply.json", "w") as file:
        file.write(json.dumps(brewing_fuel_file, indent=4))
