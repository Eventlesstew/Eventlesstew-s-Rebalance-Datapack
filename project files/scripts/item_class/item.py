import json
import copy
import pathlib

data_path = "project files/scripts/item_rebalance_data.json"
template_path = "project files/scripts/template.json"
config_path = "project files/scripts/food_rebalance_config.json"

with open(data_path, "r") as file:
    data_file = json.loads(file.read())

with open(template_path, "r") as file:
    modifier_template = json.loads(file.read())

with open(config_path, "r") as file:
    config = json.loads(file.read())


def get_item_value(item_id, key: str):
    item_data = data_file[item_id]
    default_item_data = data_file["default"]

    if key in item_data:
        return item_data[key]
    elif key in default_item_data:
        return default_item_data[key]
    else:
        return None


def get_modifier_template() -> dict:
    modifier_template_base = copy.deepcopy(modifier_template)
    return modifier_template_base


default_item_data = data_file["default"]


class item:
    _PATH = "data/event_rebalance/item_modifier/"

    def __init__(self, key):
        self.item_id = key
        print("Getting " + self.item_id)
        # The Data
        self.data = data_file[key]
        # The modifier itself
        self.modifier = get_modifier_template()
        # All of the functions for the item
        self.modifier_functions = self.modifier["on_pass"]["functions"]

        self.initialise_modifier()

    def initialise_modifier(self):
        item_type = get_item_value(self.item_id, "item_type")

        if item_type == "custom":
            self.modifier["item_filter"] = {
                "components": {"item_model": "event:" + self.item_id}
            }
        elif item_type == "vanilla_tag":
            self.modifier["item_filter"] = {"items": "#" + self.item_id}
        elif item_type == "custom_tag":
            self.modifier["item_filter"] = {"items": "#event_rebalance:" + self.item_id}
        else:
            self.modifier["item_filter"] = {"items": self.item_id}

        self.modifier_functions.append(
            {"type": "set_components", "components": self.get_components()}
        )
        self.modifier_functions.append(
            {"type": "set_lore", "mode": "append", "lore": self.get_lore()}
        )

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

    def get_components(self):
        components = {}
        item_type = get_item_value(self.item_id, "item_type")
        if item_type == "custom":
            components["item_model"] = "event:" + self.item_id
            components["item_name"] = {"translate": "item.event." + self.item_id}

        compost_value = get_item_value(self.item_id, "compost_value")
        if compost_value:
            components["compostable"] = {"layers": compost_value}

        furnace_fuel = get_item_value(self.item_id, "furnace_fuel")
        if furnace_fuel:
            furnace_fuel_speed = get_item_value(self.item_id, "furnace_fuel_speed")
            if not furnace_fuel_speed:
                furnace_fuel_speed = 1

            components["cooking_fuel"] = {
                "burn_time": int(furnace_fuel * 200),
                "speed_multiplier": 1,
            }

        brewing_fuel = get_item_value(self.item_id, "brewing_fuel")
        if brewing_fuel:
            brewing_fuel_speed = get_item_value(self.item_id, "brewing_fuel_speed")
            if not brewing_fuel_speed:
                brewing_fuel_speed = 1
            components["brewing_fuel"] = {
                "uses": int(brewing_fuel),
                "speed_multiplier": brewing_fuel_speed,
            }

        return components

    def get_lore(self):
        lore = []
        compost_value = get_item_value(self.item_id, "compost_value")
        if compost_value and compost_value != 0:
            lore.append(
                self.get_lore_base(
                    "attribute.name.compostable." + str(compost_value), [], "#AAAAAA"
                )
            )

        furnace_fuel = get_item_value(self.item_id, "furnace_fuel")
        if furnace_fuel:
            lore.append(
                self.get_lore_base(
                    str(furnace_fuel) + " ",
                    [{"translate": "attribute.name.furnace_fuel"}],
                    "#AAAAAA",
                )
            )
            furnace_fuel_speed = get_item_value(self.item_id, "furnace_fuel_speed")
            if furnace_fuel_speed:
                lore.append(
                    self.get_lore_base(
                        str(furnace_fuel_speed) + "X ",
                        [{"translate": "attribute.name.furnace_fuel_speed"}],
                        "#AAAAAA",
                    )
                )

        brewing_fuel = get_item_value(self.item_id, "brewing_fuel")
        if brewing_fuel:
            lore.append(
                self.get_lore_base(
                    str(brewing_fuel) + " ",
                    [{"translate": "attribute.name.brewing_fuel"}],
                    "#AAAAAA",
                )
            )
            brewing_fuel_speed = get_item_value(self.item_id, "brewing_fuel_speed")
            if brewing_fuel_speed:
                lore.append(
                    self.get_lore_base(
                        str(brewing_fuel_speed) + "X ",
                        [{"translate": "attribute.name.brewing_fuel_speed"}],
                        "#AAAAAA",
                    )
                )
        return lore

    def save(self):
        folder_path = self._PATH + get_item_value(self.item_id, "item_class") + "/"

        pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)

        file_path = folder_path + self.item_id + ".json"

        with open(file_path, "w") as file:
            file.write(json.dumps(self.modifier, indent=4))
        print("Created " + self.item_id)
