import json
import copy
import pathlib

data_path = "scripts/rotatable_blocks.json"
modifier_folder_path = "data/event_rebalance/block_transformer"

block_transformer_data = []


def add_common_properties(transformer):
    return transformer


with open(data_path, "r") as file:
    data_file = json.loads(file.read())


axis_transformer = {
    "y": {
        "block_state_provider": {
            "type": "minecraft:rule_based",
            "rules": [],
        },
        "disallowed_faces": ["north", "east", "south", "west"],
    },
    "x": {
        "block_state_provider": {
            "type": "minecraft:rule_based",
            "rules": [],
        },
        "disallowed_faces": ["north", "up", "south", "down"],
    },
    "z": {
        "block_state_provider": {
            "type": "minecraft:rule_based",
            "rules": [],
        },
        "disallowed_faces": ["up", "east", "down", "west"],
    },
}

any_direction_transformer = [
    {
        "block_state_provider": {
            "type": "minecraft:rule_based",
            "rules": [],
        },
        "disallowed_faces": ["north", "east", "south", "west"],
    },
    {
        "block_state_provider": {
            "type": "minecraft:rule_based",
            "rules": [],
        },
        "disallowed_faces": ["north", "up", "south", "down"],
    },
    {
        "block_state_provider": {
            "type": "minecraft:rule_based",
            "rules": [],
        },
        "disallowed_faces": ["up", "east", "down", "west"],
    },
]
any_direction_faces = {"y": 0, "x": 1, "z": 2}

for block_i, block in enumerate(data_file["axis"]):
    for axis_key in axis_transformer.keys():

        axis_transformer[axis_key]["block_state_provider"]["rules"].append(
            {
                "if_true": {
                    "type": "minecraft:matching_blocks",
                    "blocks": "minecraft:" + block,
                },
                "then": {
                    "type": "minecraft:copy_properties",
                    "source": {
                        "id": "minecraft:" + block,
                        "properties": {"axis": axis_key},
                    },
                },
            }
        )

for axis_key in axis_transformer.keys():
    block_transformer_data.append(add_common_properties(axis_transformer[axis_key]))

# Saving the Modifier
modifier_directory = modifier_folder_path + "/"
pathlib.Path(modifier_directory).mkdir(parents=True, exist_ok=True)

modifier_path = modifier_directory + "wrench.json"
with open(modifier_path, "w") as file:
    file.write(json.dumps(block_transformer_data, indent=4))
