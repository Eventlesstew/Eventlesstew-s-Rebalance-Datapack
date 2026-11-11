import json
import os
import pathlib
import copy

BUTTON_WIDTH = 100
enchant_dialog_path = "data/event_rebalance/dialog/enchantments"
dialog_template_path = "project files/scripts/enchantment_dialog_template.json"
list_template_path = "project files/scripts/enchantment_list_template.json"
enchant_list = os.listdir(enchant_dialog_path)

prot_enchants = ["protection", "barrier", "lightweight", "regrow"]
dialog_template = {}
list_template = {}
with open(dialog_template_path, "r") as f:
    dialog_template = json.loads(f.read())
with open(enchant_dialog_path + ".json", "r") as f:
    list_template = json.loads(f.read())

for i in list_template["dialogs"]:
    print(i.split("/")[1])
    enchant_list.append(i.split("/")[1])


def get_enchantment_file(enchant: str):
    data_file = {}

    event_rebalance_path = "data/event_rebalance/enchantment/" + enchant + ".json"
    minecraft_path = "data/minecraft/enchantment/" + enchant + ".json"
    namespace = ""
    if pathlib.Path(event_rebalance_path).is_file():
        with open(event_rebalance_path, "r") as f:
            data_file = json.loads(f.read())
        namespace = "event_rebalance"

    elif pathlib.Path(minecraft_path).is_file():
        with open(minecraft_path, "r") as f:
            data_file = json.loads(f.read())
        namespace = "minecraft"
    else:
        print(enchant, "does Not Exist")

    data_file["namespace"] = namespace + ":" + enchant
    return data_file


for enchant_n, enchant in enumerate(enchant_list):
    data_file = get_enchantment_file(enchant)

    enchant_dialog = copy.deepcopy(dialog_template)

    translation_key = {"translate": data_file["description"]["translate"]}
    enchant_dialog["external_title"] = translation_key
    enchant_dialog["body"][0]["description"] = translation_key

    list_template["dialogs"].append("event_rebalance:enchantments/" + enchant + "/1")

    # Iterates over the levels
    for i in range(0, data_file["max_level"]):
        i += 1
        enchant_dialog["body"][0]["item"]["components"]["stored_enchantments"] = {
            data_file["namespace"]: i
        }

        # Enchantment Description
        enchant_dialog["body"] = [enchant_dialog["body"][0]]
        enchant_dialog["body"].append(
            {
                "type": "minecraft:plain_message",
                "contents": {
                    "translate": "dialog.enchant." + enchant + ".description." + str(i)
                },
                "width": 3 * BUTTON_WIDTH,
            }
        )

        if enchant == "breach":
            enchant_dialog["body"][1] = {
                "type": "minecraft:plain_message",
                "contents": {
                    "translate": "dialog.enchant." + enchant + ".description.main"
                },
                "width": 3 * BUTTON_WIDTH,
            }
            enchant_dialog["body"].append(
                {
                    "type": "minecraft:plain_message",
                    "contents": {
                        "translate": "dialog.enchant."
                        + enchant
                        + ".description."
                        + str(i)
                        + ".a",
                    },
                    "width": 3 * BUTTON_WIDTH,
                }
            )
            enchant_dialog["body"].append(
                {
                    "type": "minecraft:plain_message",
                    "contents": {
                        "translate": "dialog.enchant."
                        + enchant
                        + ".description."
                        + str(i)
                        + ".b",
                    },
                    "width": 3 * BUTTON_WIDTH,
                }
            )
            enchant_dialog["body"].append(
                {
                    "type": "minecraft:plain_message",
                    "contents": {
                        "translate": "dialog.enchant."
                        + enchant
                        + ".description."
                        + str(i)
                        + ".c",
                    },
                    "width": 3 * BUTTON_WIDTH,
                }
            )

        if enchant in prot_enchants:
            enchant_dialog["body"].append(
                {
                    "type": "minecraft:plain_message",
                    "contents": {
                        "translate": "dialog.enchant.full_armor",
                        "extra": [
                            " ",
                            {
                                "translate": "dialog.enchant."
                                + enchant
                                + ".description.full."
                                + str(i)
                            },
                        ],
                    },
                    "width": 3 * BUTTON_WIDTH,
                }
            )

        # Gets the necessary data for previous enchant
        previous_enchant_n = enchant_n - 1

        if previous_enchant_n <= -1:
            previous_enchant_n = len(enchant_list) - 1

        previous_enchant = enchant_list[previous_enchant_n]
        previous_data_file = get_enchantment_file(enchant_list[previous_enchant_n])
        previous_translation_key = {
            "translate": previous_data_file["description"]["translate"]
        }
        previous_level = min(i, previous_data_file["max_level"])

        if previous_data_file["max_level"] > 1:
            previous_translation_key["extra"] = [
                " ",
                {"translate": "enchantment.level." + str(previous_level)},
            ]

        # Gets the necessary data for the next enchant
        next_enchant_n = enchant_n + 1
        if next_enchant_n >= len(enchant_list):
            next_enchant_n = 0

        next_enchant = enchant_list[next_enchant_n]
        next_data_file = get_enchantment_file(enchant_list[next_enchant_n])
        next_translation_key = {"translate": next_data_file["description"]["translate"]}
        next_level = min(i, next_data_file["max_level"])

        if next_data_file["max_level"] > 1:
            next_translation_key["extra"] = [
                " ",
                {"translate": "enchantment.level." + str(next_level)},
            ]

        # Clears the actions list
        enchant_dialog["actions"] = []

        # Adds the previous enchant
        enchant_dialog["actions"].append(
            {
                "label": previous_translation_key,
                "action": {
                    "type": "show_dialog",
                    "dialog": "event_rebalance:enchantments/"
                    + previous_enchant
                    + "/"
                    + str(previous_level),
                },
                "width": BUTTON_WIDTH,
            }
        )

        # Adds the +level button
        if data_file["max_level"] > 1:
            translation_key["extra"] = [
                " ",
                {"translate": "enchantment.level." + str(i)},
            ]

            if i < data_file["max_level"]:
                enchant_dialog["actions"].append(
                    {
                        "label": {
                            "translate": "dialog.enchantment.level",
                            "extra": [
                                " ",
                                {"translate": "enchantment.level." + str(i + 1)},
                            ],
                        },
                        "action": {
                            "type": "show_dialog",
                            "dialog": "event_rebalance:enchantments/"
                            + enchant
                            + "/"
                            + str(i + 1),
                        },
                        "width": BUTTON_WIDTH,
                    }
                )
            else:
                enchant_dialog["actions"].append(
                    {
                        "label": {"translate": "dialog.enchantment.level.max"},
                        "action": {
                            "type": "show_dialog",
                            "dialog": "event_rebalance:enchantments/"
                            + enchant
                            + "/"
                            + str(i),
                        },
                        "width": BUTTON_WIDTH,
                    }
                )
        else:
            enchant_dialog["actions"].append(
                {
                    "label": {"translate": "dialog.enchantment.level.none"},
                    "action": {
                        "type": "show_dialog",
                        "dialog": "event_rebalance:enchantments/"
                        + enchant
                        + "/"
                        + str(i),
                    },
                    "width": BUTTON_WIDTH,
                }
            )

        # Adds the next enchant button
        enchant_dialog["actions"].append(
            {
                "label": next_translation_key,
                "action": {
                    "type": "show_dialog",
                    "dialog": "event_rebalance:enchantments/"
                    + next_enchant
                    + "/"
                    + str(next_level),
                },
                "width": BUTTON_WIDTH,
            }
        )

        # Adds the previous level button
        if data_file["max_level"] > 1:
            if i > 1:
                enchant_dialog["actions"].append(
                    {
                        "label": {
                            "translate": "dialog.enchantment.level",
                            "extra": [
                                " ",
                                {"translate": "enchantment.level." + str(i - 1)},
                            ],
                        },
                        "action": {
                            "type": "show_dialog",
                            "dialog": "event_rebalance:enchantments/"
                            + enchant
                            + "/"
                            + str(i - 1),
                        },
                        "width": BUTTON_WIDTH,
                    }
                )
            else:
                enchant_dialog["actions"].append(
                    {
                        "label": {"translate": "dialog.enchantment.level.min"},
                        "action": {
                            "type": "show_dialog",
                            "dialog": "event_rebalance:enchantments/"
                            + enchant
                            + "/"
                            + str(i),
                        },
                        "width": BUTTON_WIDTH,
                    }
                )

        with open(
            enchant_dialog_path + "/" + enchant + "/" + str(i) + ".json", "w"
        ) as f:
            f.write(json.dumps(enchant_dialog, indent=4))

# with open(enchant_dialog_path + ".json", "w") as f:
#    f.write(json.dumps(list_template, indent=4))
