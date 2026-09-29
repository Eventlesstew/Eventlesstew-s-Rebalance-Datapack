import json
import copy

with open("scripts/gear_rebalance_template.json", "r") as file:
    modifier_template = json.loads(file.read())

with open("scripts/gear_rebalance_data.json", "r") as file:
    data_file = json.loads(file.read())

def get_tool_value(tier:str, tool:str, id:str):
    value_data = None
    value = None
    try:
        value_data = data_file["tiers"][tier]["tools"][tool][id]
    except KeyError:
        try:
            value_data = data_file["default"][tool][id]
        except KeyError:
            pass

    if value_data == None:
        return None
    elif type(value_data) is dict:
        value = get_tool_value(tier, value_data["reference"], id)

        if value == None:
            return None

        try:
            value *= value_data["mult"]
        except KeyError:
            pass
        try:
            value += value_data["mod"]
        except KeyError:
            pass
    else:
        value = value_data
    return value

def add_tool_attribute(array: list, tier: str, tool: str, type: str, id: str, base:float=0):
    value = get_tool_value(tier, tool, id)
    if value == None:
        return
    value -= base
    slot = get_tool_value(tier, tool, "slot")
    if slot == None:
        slot = "mainhand"

    result = {
        "id": "balance",
        "operation": type,
        "attribute": id,
        "value": value,
        "slot": slot
    }

    if result != None:
        attributes.append(result)
    return result

for tier_i, tier in enumerate(data_file["tiers"]):
    tier_data = data_file["tiers"][tier]
    tier_tool_data = tier_data["tools"]
    #print(tier_data["tools"])

    for tool_i, tool in enumerate(data_file["config"]["tool_list"]):
        modifier = copy.deepcopy(modifier_template)

        attributes = []
        add_tool_attribute(attributes, tier, tool, "add_value", "attack_damage", 1)
        add_tool_attribute(attributes, tier, tool, "add_value", "attack_speed", 4)

        modifier["on_pass"]["functions"].append({
            "type":"minecraft:set_attributes",
            "modifiers":attributes
        })
        tool_data = get_tool_value(tier, tool, "attack_damage")
        print(tier+"_"+tool)
        print(attributes)