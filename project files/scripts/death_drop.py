import json

drop_path = "data/event_rebalance/item_modifier/function/death_item_drop.json"
keep_path = "data/event_rebalance/item_modifier/function/death_item_keep.json"

drop_items = []
drop_data = {"type": "sequence", "functions": drop_items}

keep_items = []
keep_data = {"type": "sequence", "functions": keep_items}

for i in range(1, 100):
    keep_items.append(
        {
            "type": "filtered",
            "item_filter": {"count": i},
            "on_pass": {"type": "set_count", "count": i - (i // 2)},
        }
    )
    drop_items.append(
        {
            "type": "filtered",
            "item_filter": {"count": i},
            "on_pass": {"type": "set_count", "count": (i // 2)},
        }
    )

with open(drop_path, "w") as file:
    file.write(json.dumps(drop_data, indent=4))

with open(keep_path, "w") as file:
    file.write(json.dumps(keep_data, indent=4))
