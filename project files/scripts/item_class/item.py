import json
import copy
import pathlib
from enum import Enum

class tier_id_type(Enum):
    ID=0, # wooden_pickaxe
    DIRECTORY=1 # pickaxe/wooden
data_path = "project files/scripts/item_rebalance_data.json"
template_path = "project files/scripts/template.json"
config_path = "project files/scripts/food_rebalance_config.json"

with open(data_path, "r") as file:
    data_file = json.loads(file.read())

with open(template_path, "r") as file:
    modifier_template = json.loads(file.read())

with open(config_path, "r") as file:
    config = json.loads(file.read())

def get_item_value(item_id, key: str, tier:str=""):
    item_data = data_file[item_id]
    default_item_data = data_file["default"]
    result = None
    if key in item_data:
        result = item_data[key]
    elif key in default_item_data:
        result = default_item_data[key]

    if isinstance(result, dict) and "_type" in result:
        if tier != "" and result["_type"] == "tiered":
            if tier in result:
                result = result[tier]
            elif "other" in result:
                result = result["other"]
            else:
                result = None
    
    if isinstance(result, dict) and "_type" in result:
        if result["_type"] == "reference":
            ref = result
            result = get_item_value(result["reference"], key, tier)
            if "add" in ref:
                result += ref["add"]
            if "mult" in ref:
                result *= ref["mult"]

    return result


def get_modifier_template() -> dict:
    modifier_template_base = copy.deepcopy(modifier_template)
    return modifier_template_base

def get_modifier_template_functions() -> list:
    modifier_template_base = copy.deepcopy(modifier_template["on_pass"]["functions"])
    return modifier_template_base

default_item_data = data_file["default"]


class item:
    _PATH = "project files/scripts/test/items/"
    #_PATH = "data/event_rebalance/item_modifier/"

    def __init__(self, key):
        self.item_id = key
        print("Getting " + self.item_id)
        # The Data
        self.data = data_file[key]

    def uses_tiers(self) -> bool:
        if get_item_value(self.item_id, "tiers"):
            return True
        else:
            return False

    def get_item_id(self, tier="", format = tier_id_type.ID):
        if tier != "" and self.uses_tiers():
            if format == tier_id_type.DIRECTORY:
                return self.item_id + "/" + tier
            else:
                return tier + "_" + self.item_id
        else:
            return self.item_id
        
    def get_modifier(self, tier = ""):
        modifier = get_modifier_template()
        modifier_functions = modifier["on_pass"]["functions"]

        modifier["item_filter"] = self.get_item_filter(tier)

        attributes = self.get_attributes(tier)
        if len(attributes) > 0:
            modifier_functions.append(
                {"type": "set_attributes", "modifiers": attributes}
            )

        components = self.get_components(tier)
        if len(components) > 0:
            modifier_functions.append(
                {"type": "set_components", "components": components}
            )

        lore = self.get_lore(tier)
        if len(self.get_lore(tier)) > 0:
            modifier_functions.append(
                {"type": "set_lore", "mode": "append", "lore": lore}
            )

        return modifier

    def get_item_filter(self, tier=""):
        result = {}
        item_type = get_item_value(self.item_id, "item_type")
        
        if item_type == "custom_item_model":
            result = {
                "components": {"item_model": "event:" + self.get_item_id(tier, tier_id_type.DIRECTORY)}
            }
        elif item_type == "custom_item_tag":
            result = {"items": "#event_rebalance:custom_item/" + self.get_item_id(tier, tier_id_type.DIRECTORY)}
        elif item_type == "vanilla_tag":
            result = {"items": "#" + self.get_item_id(tier, tier_id_type.DIRECTORY)}
        elif item_type == "custom_tag":
            result = {"items": "#event_rebalance:" + self.get_item_id(tier, tier_id_type.DIRECTORY)}
        else:
            result = {"items": self.get_item_id(tier, tier_id_type.ID)}
            if item_type == "vanilla_model_sensitive":
                result["components"] = {"item_model": "minecraft:" + self.get_item_id(tier, tier_id_type.DIRECTORY)}

        return result
    
    def get_lore_base(self, text, extra=[], color="#1aa819"):
        lore = {
            "translate": text,
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

        return self.get_lore_base(
            text=text + "." + str(value), extra=extra, color=tooltip_colour
        )

    def get_attributes(self, tier = ""):
        attributes = []

        def add_attribute(from_value, base=0, operation="add_value", to_value=None):
            amount = 0
            if isinstance(from_value, str):
                if not to_value:
                    to_value = from_value
                amount = get_item_value(self.item_id, from_value, tier)
            else:
                amount = from_value
            
            if not amount or amount == 0:
                return
            amount -= base
            created_attribute = {}
            
            slot = get_item_value(self.item_id, "slot", tier)
            if slot:
                created_attribute["slot"] = slot
                created_attribute["id"] = "balance_" + slot
            else:
                created_attribute["slot"] = "mainhand"
                created_attribute["id"] = "balance"

            created_attribute["attribute"] = to_value
            created_attribute["amount"] = amount
            created_attribute["operation"] = operation

            attributes.append(created_attribute)

        add_attribute("attack_damage",1)
        add_attribute("attack_speed",4)
        add_attribute("armor")
        add_attribute("armor_toughness")
        add_attribute("block_interaction_range",0)
        add_attribute("burning_time",0,to_value="burning_time")

        movement_speed = get_item_value(self.item_id, "movement_speed", tier)
        if movement_speed:
            movement_speed *= 0.01
            air_drag = movement_speed * -1
            if air_drag > 0:
                air_drag *= 2

            add_attribute(movement_speed, 0, "add_multiplied_base", "movement_speed")
            add_attribute(air_drag, 0, "add_multiplied_base", "air_drag_modifier")
        return attributes

    def get_components(self, tier = ""):
        components = {}
        item_type = get_item_value(self.item_id, "item_type",tier)
        if item_type == "custom":
            components["item_model"] = "event:" + self.item_id
            components["item_name"] = {"translate": "item.event." + self.item_id}

        durability = get_item_value(self.item_id, "max_damage", tier)
        if durability:
            components["max_damage"] = durability
            components["damage"] = 0
            components["max_stack_size"] = 1

            if tier == "":
                components["repairable"] = {
                    "items": "#event_rebalance:tool_repair/" + self.item_id
                }
            else:
                components["repairable"] = {
                    "items": "#event_rebalance:tool_repair/" + tier
                }
        
        stealth = get_item_value(self.item_id, "stealth", tier)
        if stealth:
            components["mob_visibility"] = {
                "targeting_entity_types": "#event_rebalance:mobs",
                "visibility": 1 / stealth
            }

        return components

    def get_lore(self, tier=""):
        lore = []

        def add_lore(value:str, key:str):
            lore.append(self.get_lore_base(
                value,
                extra=[
                    {
                        "translate":"attribute.name."+key
                    }
                ],
                color="#1aa819",
            ))

        attack_damage = get_item_value(self.item_id, "attack_damage", tier)
        if attack_damage:
            add_lore(attack_damage, "attack_damage")

        attack_speed = get_item_value(self.item_id, "attack_speed", tier)
        if attack_speed:
            add_lore(attack_speed, "attack_speed")

        block_interaction_range = get_item_value(self.item_id, "block_interaction_range", tier)
        if block_interaction_range:
            if block_interaction_range > 0:
                block_interaction_range = "+" + str(block_interaction_range)
            add_lore(block_interaction_range, "block_interaction_range")

        armor = get_item_value(self.item_id, "armor", tier)
        if armor:
            add_lore(armor, "armor")
        
        armor_toughness = get_item_value(self.item_id, "armor_toughness", tier)
        if armor_toughness:
            add_lore(armor_toughness, "armor_toughness")

        movement_speed = get_item_value(self.item_id, "movement_speed", tier)
        if movement_speed:
            movement_speed = str(movement_speed) + "%"
            add_lore(movement_speed, "movement_speed")

        burn_time = get_item_value(self.item_id, "burn_time", tier)
        if burn_time:
            burn_time = str(int(burn_time*100)) + "%"
            add_lore(burn_time, "burning_time")

        return lore

    def get_compost_value(self,tier=""):
        return get_item_value(self.item_id, "compost_value",tier)

    def _get_fuel(self, value, tier=""):
        result = {}
        fuel = get_item_value(self.item_id, value, tier)

        if fuel:
            result["fuel"] = fuel
            fuel_speed = get_item_value(self.item_id, value+"_speed", tier)

            if fuel_speed:
                result["fuel_speed"] = fuel_speed

        return result

    def get_furnace_fuel(self, tier=""):
        return self._get_fuel("furnace_fuel", tier)

    def get_brewing_fuel(self, tier=""):
        return self._get_fuel("brewing_fuel", tier)
    
    def has_changes(self, tier=""):
        if (
            len(self.get_attributes(tier)) == 0 and 
            len(self.get_components(tier)) == 0 and 
            len(self.get_lore(tier)) == 0 
        ):
            return False
        return True

    def save(self):
        uses_tiers = self.uses_tiers()

        folder_path = ""
        if uses_tiers:
            folder_path = self._PATH + "tiered/" + self.item_id + "/"
        else:
            folder_path = self._PATH + get_item_value(self.item_id, "item_class") + "/"

        pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)

        if uses_tiers:
            for tier in get_item_value(self.item_id, "tiers"):
                if self.has_changes(tier):
                    file_path = folder_path + tier + ".json"
                    
                    with open(file_path, "w") as file:
                        file.write(json.dumps(self.get_modifier(tier), indent=4))
                    print("Created " + tier + self.item_id)
        else:
            if self.has_changes():
                file_path = folder_path + self.item_id + ".json"

                with open(file_path, "w") as file:
                    file.write(json.dumps(self.get_modifier(), indent=4))
                print("Created " + self.item_id)
