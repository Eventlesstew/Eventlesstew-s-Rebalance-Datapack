import json
import copy
import pathlib

template_path = "project files/scripts/template.json"
data_path = "project files/scripts/item_rebalance_data.json"
config_path = "project files/scripts/food_rebalance_config.json"

regeneration_values = [50, 25, 12, 6, 3, 1]

with open(template_path, "r") as file:
    modifier_template = json.loads(file.read())

with open(data_path, "r") as file:
    data_file = json.loads(file.read())

with open(config_path, "r") as file:
    config = json.loads(file.read())

def get_modifier_template() -> dict:
    modifier_template_base = copy.deepcopy(modifier_template)
    return modifier_template_base

default_item_data = data_file["default"]

class item():
    _PATH = "data/event_rebalance/item_modifier/"
    
    def __init__(self, key):
        self.item_id = key
        print("Getting "+self.item_id)
        # The Data
        self.data = data_file[key]
        # The modifier itself
        self.modifier = get_modifier_template()
        # All of the functions for the item
        self.modifier_functions = self.modifier["on_pass"]["functions"]

        self.initialise_modifier()

    def initialise_modifier(self):
        item_type = self.get_item_value("item_type")

        if item_type == "custom":
            self.modifier["item_filter"] = {
                "components": {"item_model": "event:" + self.item_id}
            }
        elif item_type == "vanilla_tag":
            self.modifier["item_filter"] = {"items": "#"+self.item_id}
        else:
            self.modifier["item_filter"] = {"items": self.item_id}

        self.modifier_functions.append({
            "type":"set_components",
            "components":self.get_components()
        })
        self.modifier_functions.append({
            "type":"set_lore",
            "mode":"replace_all",
            "lore":self.get_lore()
        })

    def get_item_value(self, target_key: str):
        if target_key in self.data:
            return self.data[target_key]
        elif target_key in default_item_data:
            return default_item_data[target_key]
        else:
            return None
        
    def get_lore_base(self, text, extra=[], color="#1aa819"):
        lore = {
            "translate":text,
            "italic": False,
            "color": color,
        }
        if len(extra) > 0:
            lore["extra"] = extra
        return lore

    def get_lore_from_config(self, value, key, text, extra=[]):
        config_value = config[key]
        tooltip_colour = "#ffffff"

        default_value = config_value["default"]
        if value == default_value:
            tooltip_colour = config_value["colour_if_equal"]
        elif value > default_value:
            tooltip_colour = config_value["colour_if_greater"]
        else:
            tooltip_colour = config_value["colour_if_lesser"]

        return self.get_lore_base(text=text + "." + str(value), extra=extra, color=tooltip_colour)

    def get_components(self):
        components = {}
        item_type = self.get_item_value("item_type")
        if item_type == "custom":
            components["item_model"] = "event:"+self.item_id
            components["item_name"] = {
                "translate": "item.event." + self.item_id
            }

        compost_value = self.get_item_value("compost_value")
        if compost_value:
            components["compostable"] = {"layers":compost_value}
        return components
    
    def get_lore(self):
        lore = []
        compost_value = self.get_item_value("compost_value")
        if compost_value and compost_value != 0:
            lore.append(
                self.get_lore_base("attribute.name.compostable."+str(compost_value),[],"#AAAAAA")
            )
        return lore

    def save(self):
        folder_path = self._PATH + self.get_item_value("item_class") + "/"

        pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)

        file_path = folder_path + self.item_id + ".json"
    
        with open(file_path, "w") as file:
            file.write(json.dumps(self.modifier, indent=4))
        print("Created " + self.item_id)

class food_item(item):
    def get_components(self):
        components = super().get_components()

        nutrition = self.get_item_value("food")
        saturation = self.get_item_value("saturation")
        always_edible = self.get_item_value("always_edible")
        eat_time = self.get_item_value("eat_time")
        eat_speed = self.get_item_value("eat_speed")
        eat_sound = self.get_item_value("eat_sound")
        is_drink = self.get_item_value("is_drink")

        food_effects = self.get_food_effects()

        components["food"] = {
            "nutrition": nutrition,
            "saturation": saturation,
            "can_always_eat": always_edible
        }
        components["consumable"] = {
            "consume_seconds": eat_time,
            "on_consume_effects": food_effects
        }
        components["use_effects"] = {
            "speed_multiplier": eat_speed,
            "can_sprint": eat_speed >= 0.5
        }

        if eat_sound != "default":
            sound_id = "item." + eat_sound
            if is_drink:
                sound_id += ".drink"
            else:
                sound_id += ".eat"

            components["consumable"]["sound"] = {
                "sound_id": sound_id
            }

        return components

    def get_lore(self):
        nutrition = self.get_item_value("food")
        saturation = self.get_item_value("saturation")
        healing = self.get_item_value("healing")
        always_edible = self.get_item_value("always_edible")
        eat_time = self.get_item_value("eat_time")
        eat_speed = self.get_item_value("eat_speed")
        is_drink = self.get_item_value("is_drink")

        item_lore = []
        if nutrition > 0:
            item_lore.append(
                self.get_lore_base(
                    "attribute.name.consumable.food.nutrition." + str(nutrition), color= "#f5ce0c"
                )
            )
        if saturation > 0:
            item_lore.append(
                self.get_lore_base(
                    "attribute.name.consumable.food.saturation." + str(saturation),
                    color="#f5ce0c",
                )
            )
        if healing > 0:
            item_lore.append(
                self.get_lore_base(
                    "attribute.name.consumable.food.health." + str(healing), color="#f545ac"
                )
            )

        if is_drink:
            item_lore.append(
                self.get_lore_from_config(
                    eat_time, "eat_time", "attribute.name.consumable.food.drink_time"
                )
            )
            if eat_speed != config["eat_speed"]["default"]:
                item_lore.append(
                    self.get_lore_from_config(
                        eat_speed, "eat_speed", "attribute.name.consumable.food.drink_speed"
                    )
                )
            if always_edible:
                item_lore.append(
                    self.get_lore_base("attribute.name.consumable.food.always_drinkable", color="#f78324")
                )
        else:
            item_lore.append(
                self.get_lore_from_config(
                    eat_time, "eat_time", "attribute.name.consumable.food.eat_time"
                )
            )
            if eat_speed != config["eat_speed"]["default"]:
                item_lore.append(
                    self.get_lore_from_config(
                        eat_speed, "eat_speed", "attribute.name.consumable.food.eat_speed"
                    )
                )
            if always_edible:
                item_lore.append(
                    self.get_lore_base("attribute.name.consumable.food.always_edible", color="#f78324")
                )
    
        for food_effect_lore_item in self.get_food_effects_lore():
            item_lore.append(food_effect_lore_item)

        for lore_item in super().get_lore():
            item_lore.append(lore_item)

        return item_lore

    def get_food_effects(self):
        food_effects = []

        for effect in self.get_item_value("effects"):
            effect_type = effect["effect_type"]
            if effect_type == "cure_effect":
                effect_id = effect["effect"]
                food_effects.append({"type": "remove_effects", "effects": [effect_id]})
    
            elif effect_type == "cure_effect_set":
                effect_set_id = effect["effect_set"]
                food_effects.append(
                    {
                        "type": "remove_effects",
                        "effects": config["effect_sets"][effect_set_id],
                    }
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

            elif effect_type == "teleport_randomly":
                food_effects.append({"type": "teleport_randomly"})
            elif effect_type == "clear_all_effects":
                food_effects.append({"type": "clear_all_effects"})

        healing = self.get_item_value("healing")
        eat_time = self.get_item_value("eat_time")

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

        eat_sound_finish = self.get_item_value("eat_sound_finish")

        if eat_sound_finish != default_item_data["eat_sound_finish"]:
            food_effects.append(
                {
                    "type": "play_sound",
                    "sound":{
                        "sound_id":"item."+eat_sound_finish+".consume"
                    }
                }
            )
        
        return food_effects

    def get_food_effects_lore(self):
        food_effect_lore = []
        
        for effect in self.get_item_value("effects"):
            effect_type = effect["effect_type"]
            if effect_type == "cure_effect":
                effect_id = effect["effect"]
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food." + effect_type + "." + effect_id,
                        color=self.get_effect_color(effect_id, True),
                    )
                )
            elif effect_type == "cure_effect_set":
                effect_set_id = effect["effect_set"]
    
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food."
                        + effect_type
                        + "."
                        + effect_set_id,
                        color="#5555ff"
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
                    effect_duration += int(effect["duration_seconds"] / 20)
                if "duration_ticks" in effect:
                    effect_duration += effect["duration_ticks"]
                if "probability" in effect:
                    effect_probability = effect["probability"]
    
                translation_key = (
                    "attribute.name.consumable.food."
                    + effect_type
                    + "."
                    + effect_id
                    + "."
                    + str(effect_level + 1)
                    + "."
                    + str(effect_duration)
                    + "s"
                )
                if effect_probability < 1:
                    effect_probability_percent = str(int(effect_probability * 100)) + "%"
                    translation_key += "." + effect_probability_percent
                
                food_effect_lore.append(
                    self.get_lore_base(
                        translation_key,
                        color=self.get_effect_color(effect_id),
                    )
                )

            elif effect_type == "teleport_randomly":
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food.teleport_randomly",
                        color="#5555ff",
                    )
                )

            elif effect_type == "teleport_forward":
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food.teleport_forward",
                        color="#5555ff",
                    )
                )
            elif effect_type == "unknown_effect":
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food.unknown_effect",
                        color="#5555ff",
                    )
                )
            elif effect_type == "clear_all_effects":
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food.cure_all_effects",
                        color="#5555ff",
                    )
                )
        return food_effect_lore
    def get_effect_color(self, effect, inverted=False):
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

def add_food_item(item_key: str):
    item_class = "default"
    if "item_class" in data_file[item_key]:
        item_class = data_file[item_key]["item_class"]

    item_object = None
    if item_class == "food":
        item_object = food_item(item_key)
    else:
        item_object = item(item_key)

    item_object.save()

item_keys = data_file.keys()

for item_key in item_keys:
    if item_key != "default":
        add_food_item(item_key)
