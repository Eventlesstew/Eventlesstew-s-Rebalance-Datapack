import json
import copy
import pathlib

template_path = "project files/scripts/template.json"
data_path = "project files/scripts/food_rebalance_data.json"
config_path = "project files/scripts/food_rebalance_config.json"
modifier_folder_path = "data/event_rebalance/item_modifier/food"

lore_base = {
    "italic": False,
    "color": "#1aa819",
}

regeneration_values = [50, 25, 12, 6, 3, 1]

with open(template_path, "r") as file:
    modifier_template = json.loads(file.read())

with open(data_path, "r") as file:
    data_file = json.loads(file.read())

with open(config_path, "r") as file:
    config = json.loads(file.read())


def get_tooltip(text, color):
    lore = copy.deepcopy(lore_base)
    lore["translate"] = text
    lore["color"] = color
    return lore


def get_tooltip_from_config(text, key, value):
    config_value = config[key]
    tooltip_colour = "#ffffff"

    default_value = config_value["default"]
    if value == default_value:
        tooltip_colour = config_value["colour_if_equal"]
    elif value > default_value:
        tooltip_colour = config_value["colour_if_greater"]
    else:
        tooltip_colour = config_value["colour_if_lesser"]

    return get_tooltip(text + "." + str(value), tooltip_colour)


def get_tooltip_effect_colour(effect, inverted=False):
    if effect in config["effect_sets"]["negative"]:
        if inverted:
            return "#5555ff"
        else:
            return "#ff5555"
    else:
        if inverted:
            return "#ff5555"
        else:
            return "#5555ff"


def get_modifier_template() -> dict:
    modifier_template_base = copy.deepcopy(modifier_template)
    return modifier_template_base


default_food_data = data_file["default"]

pathlib.Path(modifier_folder_path).mkdir(parents=True, exist_ok=True)

food_keys = data_file.keys()


def add_food_item(food_key: str):
    food = data_file[food_key]  # The food data
    food_modifier = get_modifier_template()  # The modifier itself
    food_modifier_functions = food_modifier["on_pass"][
        "functions"
    ]  # All of the functions for the food

    def get_food_value(target_key: str):
        if target_key in food:
            return food[target_key]
        elif target_key in default_food_data:
            return default_food_data[target_key]

    item_type = get_food_value("item_type")
    nutrition = get_food_value("food")
    saturation = get_food_value("saturation")
    healing = get_food_value("healing")
    always_edible = get_food_value("always_edible")
    eat_time = get_food_value("eat_time")
    eat_speed = get_food_value("eat_speed")
    eat_sound = get_food_value("eat_sound")

    if item_type == "custom":
        food_modifier["item_filter"] = {
            "components": {"item_model": "event:" + food_key}
        }
    else:
        food_modifier["item_filter"] = {"items": food_key}

    food_effects = []
    food_effect_lore = []

    for effect in get_food_value("effects"):
        effect_type = effect["effect_type"]
        if effect_type == "cure_effect":
            effect_id = effect["effect"]
            food_effects.append({"type": "remove_effects", "effects": [effect_id]})
            food_effect_lore.append(
                get_tooltip(
                    "attribute.name.consumable.food." + effect_type + "." + effect_id,
                    get_tooltip_effect_colour(effect_id, True),
                )
            )

        elif effect_type == "cure_effect_set":
            effect_set_id = effect["effect_set"]
            food_effects.append(
                {
                    "type": "remove_effects",
                    "effects": config["effect_sets"][effect_set_id],
                }
            )

            food_effect_lore.append(
                get_tooltip(
                    "attribute.name.consumable.food."
                    + effect_type
                    + "."
                    + effect_set_id,
                    "#5555ff",
                )
            )
        elif effect_type == "apply_effect":
            effect_id = effect["effect"]
            effect_duration = 0
            effect_level = 1
            effect_probability = 1
            if "level" in effect:
                effect_level = effect["level"] - 1
            if "duration_seconds" in effect:
                effect_duration += effect["duration_seconds"] * 20
            if "duration_ticks" in effect:
                effect_duration += effect["duration_ticks"]
            if "probability" in effect:
                effect_probability = effect["probability"]

            effect_data = {
                "type": "apply_effects",
                "probability": effect_probability,
                "effects": [
                    {
                        "id": effect_id,
                        "amplifier": effect_level,
                        "duration": effect_duration,
                    }
                ],
            }

            food_effects.append(effect_data)

            effect_duration_seconds = int(effect_duration / 20)

            translation_key = (
                "attribute.name.consumable.food."
                + effect_type
                + "."
                + effect_id
                + "."
                + str(effect_level + 1)
                + "."
                + str(effect_duration_seconds)
                + "s"
            )
            if effect_probability < 1:
                effect_probability_percent = str(int(effect_probability * 100)) + "%"
                translation_key += "." + effect_probability_percent
            food_effect_lore.append(
                get_tooltip(
                    translation_key,
                    get_tooltip_effect_colour(effect_id),
                )
            )
        elif effect_type == "teleport_randomly":
            food_effects.append({"type": "teleport_randomly"})
            food_effect_lore.append(
                get_tooltip(
                    "attribute.name.consumable.food.teleport_randomly",
                    "#5555ff",
                )
            )
        elif effect_type == "teleport_forward":
            food_effect_lore.append(
                get_tooltip(
                    "attribute.name.consumable.food.teleport_forward",
                    "#5555ff",
                )
            )
        elif effect_type == "unknown_effect":
            food_effect_lore.append(
                get_tooltip(
                    "attribute.name.consumable.food.unknown_effect",
                    "#5555ff",
                )
            )
        elif effect_type == "clear_all_effects":
            food_effects.append({"type": "clear_all_effects"})
            food_effect_lore.append(
                get_tooltip(
                    "attribute.name.consumable.food.cure_all_effects",
                    "#5555ff",
                )
            )

    food_components = {  # The components to apply for the food
        "food": {
            "nutrition": nutrition,
            "saturation": saturation,
            "can_always_eat": always_edible,
        },
        "consumable": {
            "consume_seconds": eat_time,
            "on_consume_effects": food_effects,
        },
        "minecraft:use_effects": {
            "speed_multiplier": eat_speed,
            "can_sprint": eat_speed >= 0.5,
        },
    }

    food_lore = []

    if nutrition > 0:
        food_lore.append(
            get_tooltip(
                "attribute.name.consumable.food.nutrition." + str(nutrition), "#f5ce0c"
            )
        )
    if saturation > 0:
        food_lore.append(
            get_tooltip(
                "attribute.name.consumable.food.saturation." + str(saturation),
                "#f5ce0c",
            )
        )
    if healing > 0:
        target_level = 5
        target_level_result = 99999
        for i, v in enumerate(regeneration_values):
            result = (eat_time * 20 / v) - healing

            if 0 <= result <= target_level_result:
                target_level = i
                target_level_result = result

        target_duration = healing * regeneration_values[target_level]
        food_effects.append(
            {
                "type": "apply_effects",
                "effects": [
                    {
                        "id": "regeneration",
                        "amplifier": target_level,
                        "duration": target_duration,
                        "show_icon": False,
                        "show_particles": False,
                    }
                ],
            }
        )
        food_lore.append(
            get_tooltip(
                "attribute.name.consumable.food.health." + str(healing), "#f545ac"
            )
        )

    food_lore.append(
        get_tooltip_from_config(
            "attribute.name.consumable.food.eat_time", "eat_time", eat_time
        )
    )
    if eat_speed != config["eat_speed"]["default"]:
        food_lore.append(
            get_tooltip_from_config(
                "attribute.name.consumable.food.eat_speed", "eat_speed", eat_speed
            )
        )
    if always_edible:
        food_lore.append(
            get_tooltip("attribute.name.consumable.food.always_edible", "#f78324")
        )

    for food_effect_lore_item in food_effect_lore:
        food_lore.append(food_effect_lore_item)

    if eat_sound != "default":
        food_components["consumable"]["sound"] = {
            "sound_id": "item." + eat_sound + ".eat"
        }

    food_modifier_functions.append(
        {"type": "set_components", "components": food_components}
    )
    food_modifier_functions.append(
        {"type": "set_lore", "mode": "replace_all", "lore": food_lore}
    )
    modifier_file_path = (
        modifier_folder_path + "/" + food_key + ".json"
    )  # The file path to write the json file to

    with open(modifier_file_path, "w") as file:
        file.write(json.dumps(food_modifier, indent=4))
    print("Creating " + food_key)


for food_i, food_key in enumerate(food_keys):
    if food_key != "default":
        add_food_item(food_key)
