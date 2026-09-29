import json
import copy
import pathlib

template_path = "scripts/gear_rebalance_template.json"
data_path = "scripts/gear_rebalance_data.json"
modifier_folder_path = "scripts/modifiers"

with open(template_path, "r") as file:
    modifier_template = json.loads(file.read())

with open(data_path, "r") as file:
    data_file = json.loads(file.read())


def get_tier_value(tier: str, id: str):
    value = None
    try:
        value = data_file["tiers"][tier][id]
    except KeyError:
        try:
            value = data_file["default"][id]
        except KeyError:
            pass
    return value


def get_tool_value(tier: str, tool: str, id: str):
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
        value_data = get_tier_value(tier, id)

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


def add_tool_attribute(
    data: dict, tier: str, tool: str, type: str, id: str, base: float = 0
):
    value = get_tool_value(tier, tool, id)
    if value == None:
        return
    value -= base
    slot = get_tool_value(tier, tool, "slot")
    if slot == None:
        slot = "mainhand"

    attribute = {
        "id": "balance",
        "operation": type,
        "attribute": id,
        "value": value,
        "slot": slot,
    }

    data["attributes"].append(attribute)

    lore = {
        "text": " " + str(value) + " ",
        "extra": [{"translate": "attribute.name.id"}],
        "italic": False,
        "color": "#1aa819",
    }

    data["lore"].append(lore)
    return attribute


def is_custom(tier: str, tool: str) -> bool:
    try:
        if data_file["tiers"][tier]["custom_tier"]:
            return True
    except KeyError:
        pass

    if get_tool_value(tier, tool, "custom_tool"):
        return True

    return False


for tier_i, tier in enumerate(data_file["tiers"]):
    tier_data = data_file["tiers"][tier]
    tier_tool_data = tier_data["tools"]
    # print(tier_data["tools"])

    for tool_i, tool in enumerate(data_file["config"]["tool_list"]):
        modifier = copy.deepcopy(modifier_template)

        tool_data = {
            "attributes": [],
            "components": {},
            "lore": [{"translate": " ", "color": "#AAAAAA", "italic": False}],
        }
        components = tool_data["components"]

        modifier["on_pass"]["functions"].append(
            {"type": "minecraft:set_attributes", "modifiers": tool_data["attributes"]}
        )
        modifier["on_pass"]["functions"].append(
            {"type": "minecraft:set_components", "components": components}
        )
        modifier["on_pass"]["functions"].append(
            {"type": "minecraft:set_lore", "lore": tool_data["lore"]}
        )

        add_tool_attribute(tool_data, tier, tool, "add_value", "attack_damage", 1)
        add_tool_attribute(tool_data, tier, tool, "add_value", "attack_speed", 4)
        ## TODO - Add a check if the item is unbreakable, for horse and nautilus armor.
        components["max_damage"] = get_tool_value(tier, tool, "max_damage")

        # Item Filter
        display_tier = tier

        if get_tool_value(tier, tool, "uses_armor_tier"):
            armor_tier = get_tier_value(tier, "armor_name")
            if armor_tier:
                display_tier = armor_tier

        ## TODO: Add an item modifier that changes Discs or Pottery Sherds into a suitable dummy item.
        if is_custom(tier, tool):
            modifier["item_filter"]["items"] = (
                "#event_rebalance:custom_item/" + display_tier + "/" + tool
            )
            modifier["item_filter"]["components"] = {
                "item_model": "event:gear/" + display_tier + "/" + tool
            }
            components["item_name"] = "item.event." + display_tier + "_" + tool
            components["damage"] = 0
        else:
            modifier["item_filter"]["items"] = display_tier + "_" + tool

        # Saving the Modifier
        modifier_directory = modifier_folder_path + "/" + tool + "/"
        pathlib.Path(modifier_directory).mkdir(parents=True, exist_ok=True)

        modifier_path = modifier_directory + display_tier + ".json"
        with open(modifier_path, "w") as file:
            file.write(json.dumps(modifier, indent=4))
        print("Creating " + display_tier + "_" + tool)
