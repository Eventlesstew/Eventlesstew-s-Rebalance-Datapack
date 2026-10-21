import json
import copy
import csv

template_path = "project files/scripts/template.json"
data_path = "project files/scripts/food_rebalance_data.json"
config_path = "project files/scripts/food_rebalance_config.json"
modifier_file_path = "project files/scripts/test/food_values.csv"

lore_base = {
    "italic": False,
    "color": "#1aa819",
}

regeneration_values = [50, 25, 12, 6, 3, 1]
poison_values = [25,12]

with open(template_path, "r") as file:
    modifier_template = json.loads(file.read())

with open(data_path, "r") as file:
    data_file = json.loads(file.read())

with open(config_path, "r") as file:
    config = json.loads(file.read())


def get_modifier_template() -> dict:
    modifier_template_base = copy.deepcopy(modifier_template)
    return modifier_template_base


default_food_data = data_file["default"]
food_keys = data_file.keys()

def is_effect_negative(effect_id:str):
    if effect_id in config["effect_sets"]["negative"]:
        return True
    else:
        return False

def get_default_food_value(target_key: str):
    return default_food_data[target_key]

def calculate_value(food_key: str):
    result = 0

    food = data_file[food_key]  # The food data

    def get_food_value(target_key: str):
        if target_key in food:
            return food[target_key]
        elif target_key in default_food_data:
            return default_food_data[target_key]

    
    nutrition = get_food_value("food")
    saturation = get_food_value("saturation")
    healing = get_food_value("healing")
    always_edible = get_food_value("always_edible")
    eat_time = get_food_value("eat_time")
    eat_speed = get_food_value("eat_speed")

    def get_effect_value(effect_id:str,effect_level:int,effect_duration_ticks:int,effect_probability:float):
        effect_value_result = 0
        healing_result = 0
        if effect_id == "poison":
            poison_rate = regeneration_values[effect_level-1]
            health_lost = effect_duration_ticks/poison_rate
            if health_lost > 19:
                healing_result -= 19
            else:
                healing_result -= health_lost
        elif effect_id == "regeneration" or effect_id == "wither":
            if effect_id == "wither" and effect_level >3:
                effect_level = 3
            regeneration_rate = regeneration_values[effect_level-1]
            
            eat_time_ticks = eat_time * 20

            if effect_id == "regeneration" and effect_duration_ticks > eat_time_ticks:
                healing_result += eat_time_ticks/regeneration_rate
                healing_result += (effect_duration_ticks-eat_time_ticks)/regeneration_rate * 0.5
            else:
                healing_result += effect_duration_ticks/regeneration_rate

            if effect_id == "wither":
                healing_result *= -1

        elif effect_id == "instant_health" or effect_id == "instant_damage":
            healing_result += 2 * (2**effect_level) * 2

            if effect_id == "instant_health" and not always_edible:
                healing_result *= 0.8
            elif effect_id == "instant_damage":
                healing_result *= -1

        elif effect_id == "absorption":
            healing_result += 4 * effect_level * 2 * 1.5

            if not always_edible:
                healing_result *= 0.8
            
        else:
            effect_value_result += effect_level

        if effect_id in config["effect_sets"]["negative"]:
            effect_value_result *= -1

        effect_value_result *= effect_probability
        healing_result *= effect_probability
        return {
            "effect_value":effect_value_result,
            "healing":healing_result
        }


    for effect in get_food_value("effects"):
        effect_type = effect["effect_type"]
        if effect_type == "cure_effect":
            effect_id = effect["effect"]

            if is_effect_negative(effect_id=effect_id):
                result += 0.5
            else:
                result -= 0.5
            

        elif effect_type == "cure_effect_set":
            effect_set_id = effect["effect_set"]
            for effect_id in config["effect_sets"][effect_set_id]:
                if is_effect_negative(effect_id=effect_id):
                    result += 0.5
                else:
                    result -= 0.5
            
        elif effect_type == "apply_effect":
            effect_id = effect["effect"]
            effect_duration = 0
            effect_level = 1
            effect_probability = 1
            if "level" in effect:
                effect_level = effect["level"]
            if "duration_seconds" in effect:
                effect_duration += effect["duration_seconds"] * 20
            if "duration_ticks" in effect:
                effect_duration += effect["duration_ticks"]
            if "probability" in effect:
                effect_probability = effect["probability"]

            effect_value_result = get_effect_value(effect_id=effect_id,effect_level=effect_level,effect_duration_ticks=effect_duration,effect_probability=effect_probability)
            result += effect_value_result["effect_value"]
            healing += effect_value_result["healing"]

        elif effect_type == "teleport_randomly":
            result += 0.0
        elif effect_type == "teleport_forward":
            result += 1
        elif effect_type == "unknown_effect":
            pass
        elif effect_type == "clear_all_effects":
            pass

    always_edible_int = int(always_edible)
    result += (((nutrition+((saturation*1.5)+healing)*((always_edible_int/4)+1)) * ((2.4/eat_time)+eat_speed))/7.5)
    print(food_key, result)
    return result
    
    #with open(modifier_file_path, "w") as file:
    #    file.write(json.dumps(food_modifier, indent=4))
    #print("Creating " + food_key)

food_values = []

for food_i, food_key in enumerate(food_keys):
    if food_key != "default":
        food_values.append({
            "id":food_key,
            "value":calculate_value(food_key)
        })

csv_table = []
for food in sorted(food_values,key=lambda food_value: food_value["value"], reverse=True):
    csv_table.append([food["id"], food["value"]])
    print(food["id"], food["value"])

with open(modifier_file_path, "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(csv_table)
print("CSV file created successfully")