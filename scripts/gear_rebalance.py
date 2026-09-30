import json
import copy
import pathlib

template_path = "scripts/gear_rebalance_template.json"
data_path = "scripts/gear_rebalance_data.json"
modifier_folder_path = "data/event_rebalance/item_modifier/gear"

lore_base = {
    "text": "",
    "extra": [],
    "italic": False,
    "color": "#1aa819",
}
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
    data: dict,
    tier: str,
    tool: str,
    type: str,
    id: str,
    base: float = 0,
    display_attribute: bool = True,
):
    value = get_tool_value(tier, tool, id)
    if value == None:
        return

    slot = get_tool_value(tier, tool, "slot")
    if slot == None:
        slot = "mainhand"

    display_value = str(value)
    value -= base
    if type == "add_multiplied_base":
        value *= 0.01
        display_value += "%"
    attribute = {
        "id": "balance",
        "operation": type,
        "attribute": id,
        "amount": value,
        "slot": slot,
    }

    data["attributes"].append(attribute)

    if display_attribute:
        lore = copy.deepcopy(lore_base)
        lore["text"] = " " + display_value + " "
        lore["extra"] = [{"translate": "attribute.name." + id}]

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
            "lore": [{"text": " ", "color": "#AAAAAA", "italic": False}],
        }
        components = tool_data["components"]

        def add_attribute(
            id: str,
            base: float = 0.0,
            operator: str = "add_value",
            show_attribute: bool = True,
        ):
            add_tool_attribute(
                tool_data, tier, tool, operator, id, base, show_attribute
            )

        modifier["on_pass"]["functions"].append(
            {"type": "minecraft:set_attributes", "modifiers": tool_data["attributes"]}
        )
        modifier["on_pass"]["functions"].append(
            {"type": "minecraft:set_components", "components": components}
        )
        modifier["on_pass"]["functions"].append(
            {
                "type": "minecraft:set_lore",
                "mode": "replace_all",
                "lore": tool_data["lore"],
            }
        )

        add_attribute("attack_damage", 1)
        add_attribute("attack_speed", 4)
        add_attribute("armor")
        add_attribute("armor_toughness")
        add_attribute("movement_speed", operator="add_multiplied_base")
        add_attribute(
            "air_drag_modifier", operator="add_multiplied_base", show_attribute=False
        )
        add_attribute("burning_time", operator="add_multiplied_base")

        # Item Filter
        display_tier = tier

        if get_tool_value(tier, tool, "uses_armor_tier"):
            armor_tier = get_tier_value(tier, "armor_name")
            if armor_tier:
                display_tier = armor_tier

        if not get_tool_value(tier, tool, "unbreakable"):
            components["max_damage"] = get_tool_value(tier, tool, "max_damage")
            components["repairable"] = {
                "items": "#event_rebalance:tool_repair/" + display_tier
            }

        # Stealth
        stealth = get_tool_value(tier, tool, "stealth")
        if stealth:
            components["mob_visibility"] = {
                "targeting_entity_types": "#event_rebalance:mobs",
                "visibility": 1 / stealth,
            }

        # Durability and Shield Break Handling
        components["weapon"] = {
            "item_damage_per_attack": 1,
            "disable_blocking_for_seconds": get_tool_value(
                tier, tool, "shield_disable_time"
            ),
        }

        # Mining Components
        mineable = get_tool_value(tier, tool, "mineable")
        if mineable:
            # Mining Speed
            mining_speed = get_tool_value(tier, tool, "mining_speed")
            tool_rules = []
            components["tool"] = {"rules": tool_rules}

            tool_rules.append(
                {
                    "blocks": "#mineable/" + mineable,
                    "speed": mining_speed,
                    "correct_for_drops": True,
                }
            )

            # Mining Speed tooltip
            mining_speed_tooltip = copy.deepcopy(lore_base)
            mining_speed_tooltip["text"] = " " + str(mining_speed) + " "
            mining_speed_tooltip["extra"] = [
                {"translate": "attribute.name." + mineable + "_mining_speed"}
            ]
            tool_data["lore"].append(mining_speed_tooltip)

            if get_tool_value(tier, tool, "uses_pickaxe_mining_power"):
                mining_power = get_tool_value(tier, tool, "mining_power")

                if mineable == "pickaxe" and mining_power >= 3:
                    tool_rules.insert(
                        0,
                        {
                            "blocks": "#event_rebalance:obsidian",
                            "speed": mining_speed * 2,
                            "correct_for_drops": True,
                        },
                    )

                tool_rules.insert(
                    0,
                    {
                        "blocks": "#event_rebalance:pickaxe_power_"
                        + str(mining_power + 1),
                        "speed": mining_speed / 4,
                        "correct_for_drops": False,
                    },
                )

                mining_power_tooltip = copy.deepcopy(lore_base)
                mining_power_tooltip["text"] = " " + str(mining_power) + " "
                mining_power_tooltip["extra"] = [
                    {"translate": "attribute.name.mining_power"}
                ]
                tool_data["lore"].append(mining_power_tooltip)

        # Dagger Animation
        if tool == "dagger":
            components["damage_type"] = "event_rebalance:dagger"
            components["attack_animation"] = {"type": "stab", "duration": 4}

        # Spear Data
        if tool == "spear":
            charge_delay_seconds = get_tool_value(tier, tool, "charge_delay")
            charge_delay_ticks = charge_delay_seconds * 20
            charge_duration_seconds = get_tool_value(tier, tool, "charge_duration")
            charge_duration_ticks = charge_duration_seconds * 20
            sound_id = get_tool_value(tier, tool, "spear_sound_id")
            components["piercing_weapon"] = {
                "sound": "item." + sound_id + ".attack",
                "hit_sound": "item." + sound_id + ".hit",
            }
            components["kinetic_weapon"] = {
                "delay_ticks": get_tool_value(tier, tool, "charge_delay") * 20,
                "dismount_conditions": {
                    "max_duration_ticks": int(charge_duration_ticks / 3),
                    "min_speed": 8,
                },
                "knockback_conditions": {
                    "max_duration_ticks": int(charge_duration_ticks * 2 / 3),
                    "min_speed": 4,
                },
                "damage_conditions": {
                    "max_duration_ticks": int(charge_duration_ticks),
                    "min_speed": 4,
                },
                "damage_multiplier": get_tool_value(
                    tier, tool, "spear_damage_multiplier"
                ),
                "contact_cooldown_ticks": 10,
                "sound": "item." + sound_id + ".use",
                "hit_sound": "item." + sound_id + ".hit",
                "forward_movement": 0.4,
            }
            components["attack_range"] = {
                "min_reach": 2,
                "max_reach": 4.5,
                "mob_factor": 0.5,
            }
            components["minimum_attack_charge"] = 1

            # Charge Delay Tooltip
            charge_delay_lore = copy.deepcopy(lore_base)
            charge_delay_lore["text"] = " " + str(charge_delay_seconds) + "s "
            charge_delay_lore["extra"] = [{"translate": "attribute.name.charge_delay"}]
            tool_data["lore"].append(charge_delay_lore)

            # Charge Duration Tooltip
            charge_duration_lore = copy.deepcopy(lore_base)
            charge_duration_lore["text"] = " " + str(charge_duration_seconds) + "s "
            charge_duration_lore["extra"] = [
                {"translate": "attribute.name.charge_duration"}
            ]
            tool_data["lore"].append(charge_duration_lore)

        if is_custom(tier, tool):
            modifier["item_filter"]["items"] = (
                "#event_rebalance:custom_item/gear/" + display_tier + "/" + tool
            )
            modifier["item_filter"]["components"] = {
                "item_model": "event:gear/" + display_tier + "/" + tool
            }
            components["item_name"] = {
                "translate": "item.event." + display_tier + "_" + tool
            }
            components["damage"] = 0
            components["!jukebox_playable"] = {}
            components["!provides_pottery_pattern"] = {}
            components["max_stack_size"] = 1
            components["rarity"] = "common"
        else:
            modifier["item_filter"]["items"] = display_tier + "_" + tool

        # Saving the Modifier
        modifier_directory = modifier_folder_path + "/" + display_tier + "/"
        pathlib.Path(modifier_directory).mkdir(parents=True, exist_ok=True)

        modifier_path = modifier_directory + tool + ".json"
        with open(modifier_path, "w") as file:
            file.write(json.dumps(modifier, indent=4))
        print("Creating " + display_tier + "_" + tool)
