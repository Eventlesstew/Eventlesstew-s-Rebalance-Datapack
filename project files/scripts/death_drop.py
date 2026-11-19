import json

drop_path = "data/event_rebalance/item_modifier/function/death_item_drop/"
keep_path = "data/event_rebalance/item_modifier/function/death_item_keep/"

drop_items = {}
keep_items = {}

keep_amounts = {"easy": 0.75, "normal": 0.5, "hard": 0.25}

for key in keep_amounts:
    drop_items[key] = []
    keep_items[key] = []

for i in range(1, 100):
    for key in keep_amounts:
        keep_amount = keep_amounts[key]
        amount_to_keep = int(i // (1 / keep_amount))
        keep_items[key].append(
            {
                "type": "filtered",
                "item_filter": {"count": i},
                "on_pass": {"type": "set_count", "count": amount_to_keep},
            }
        )
        drop_items[key].append(
            {
                "type": "filtered",
                "item_filter": {"count": i},
                "on_pass": {"type": "set_count", "count": i - amount_to_keep},
            }
        )

for key in keep_amounts:
    drop_path_diff = drop_path + key + ".json"
    keep_path_diff = keep_path + key + ".json"

    drop_data = {"type": "sequence", "functions": drop_items[key]}
    keep_data = {"type": "sequence", "functions": keep_items[key]}

    with open(drop_path_diff, "w") as file:
        file.write(json.dumps(drop_data, indent=4))

    with open(keep_path_diff, "w") as file:
        file.write(json.dumps(keep_data, indent=4))
