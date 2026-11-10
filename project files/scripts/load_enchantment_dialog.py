import json
import os
import pathlib
import copy

enchant_dialog_path = "data/event_rebalance/dialog/enchantments"
dialog_template_path = "project files/scripts/enchantment_dialog_template.json"
enchant_list = os.listdir(enchant_dialog_path)

dialog_template = {}
with open(dialog_template_path, "r") as f:
    dialog_template = json.loads(f.read())
print(enchant_list)


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


for enchant in enchant_list:
    data_file = get_enchantment_file(enchant)

    enchant_dialog = copy.deepcopy(dialog_template)

    translation_key = {"translate": data_file["description"]["translate"]}
    enchant_dialog["external_title"] = translation_key
    enchant_dialog["body"][0]["description"] = translation_key

    for i in range(0, data_file["max_level"]):
        i += 1
        enchant_dialog["body"][0]["item"]["components"]["stored_enchantments"] = {
            data_file["namespace"]: i
        }
        enchant_dialog["body"][1]["contents"] = {
            "translate": "dialog.enchant." + enchant + ".description." + str(i)
        }
        if data_file["max_level"] > 1:
            translation_key["extra"] = [
                " ",
                {"translate": "enchantment.level." + str(i)},
            ]

            enchant_dialog["actions"] = []
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
                        "width": 64,
                    }
                )
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
                        "width": 64,
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
                    "width": 64,
                }
            )

        with open(
            enchant_dialog_path + "/" + enchant + "/" + str(i) + ".json", "w"
        ) as f:
            f.write(json.dumps(enchant_dialog, indent=4))
