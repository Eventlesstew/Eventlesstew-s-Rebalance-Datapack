from item_class.item import *

regeneration_values = [50, 25, 12, 6, 3, 1]
poison_values = [25, 12]


def is_effect_negative(effect_id: str):
    if effect_id in config["effect_sets"]["negative"]:
        return True
    else:
        return False


class food_item(item):
    def get_components(self,tier):
        components = super().get_components(tier)

        nutrition = get_item_value(self.item_id, "food",tier)
        saturation = get_item_value(self.item_id, "saturation",tier)
        always_edible = get_item_value(self.item_id, "always_edible",tier)
        eat_time = get_item_value(self.item_id, "eat_time",tier)
        eat_speed = get_item_value(self.item_id, "eat_speed",tier)
        eat_sound = get_item_value(self.item_id, "eat_sound",tier)
        is_drink = get_item_value(self.item_id, "is_drink",tier)

        food_effects = self.get_food_effects(tier)

        components["food"] = {
            "nutrition": nutrition,
            "saturation": saturation,
            "can_always_eat": always_edible,
        }
        components["consumable"] = {
            "consume_seconds": eat_time,
            "on_consume_effects": food_effects,
        }
        components["use_effects"] = {
            "speed_multiplier": eat_speed,
            "can_sprint": eat_speed >= 0.5,
        }

        if eat_sound != "default":
            sound_id = "item." + eat_sound
            if is_drink:
                sound_id += ".drink"
            else:
                sound_id += ".eat"

            components["consumable"]["sound"] = {"sound_id": sound_id}

        return components

    def get_lore(self, tier=""):
        nutrition = get_item_value(self.item_id, "food",tier)
        saturation = get_item_value(self.item_id, "saturation",tier)
        healing = get_item_value(self.item_id, "healing",tier)
        always_edible = get_item_value(self.item_id, "always_edible",tier)
        eat_time = get_item_value(self.item_id, "eat_time",tier)
        eat_speed = get_item_value(self.item_id, "eat_speed",tier)
        is_drink = get_item_value(self.item_id, "is_drink",tier)

        item_lore = []
        if nutrition > 0:
            item_lore.append(
                self.get_lore_base(
                    "attribute.name.consumable.food.nutrition." + str(nutrition),
                    color="#f5ce0c",
                )
            )
        if saturation > 0:
            item_lore.append(
                self.get_lore_base(
                    "attribute.name.consumable.food.saturation." + str(saturation),
                    color="#f5ce0c",
                )
            )
        if healing > 0:
            item_lore.append(
                self.get_lore_base(
                    "attribute.name.consumable.food.health." + str(healing),
                    color="#f545ac",
                )
            )

        if is_drink:
            item_lore.append(
                self.get_lore_from_config(
                    eat_time, "eat_time", "attribute.name.consumable.food.drink_time"
                )
            )
            if eat_speed != config["eat_speed"]["default"]:
                item_lore.append(
                    self.get_lore_from_config(
                        eat_speed,
                        "eat_speed",
                        "attribute.name.consumable.food.drink_speed",
                    )
                )
            if always_edible:
                item_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food.always_drinkable",
                        color="#f78324",
                    )
                )
        else:
            item_lore.append(
                self.get_lore_from_config(
                    eat_time, "eat_time", "attribute.name.consumable.food.eat_time"
                )
            )
            if eat_speed != config["eat_speed"]["default"]:
                item_lore.append(
                    self.get_lore_from_config(
                        eat_speed,
                        "eat_speed",
                        "attribute.name.consumable.food.eat_speed",
                    )
                )
            if always_edible:
                item_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food.always_edible", color="#f78324"
                    )
                )

        for food_effect_lore_item in self.get_food_effects_lore(tier):
            item_lore.append(food_effect_lore_item)

        for lore_item in super().get_lore():
            item_lore.append(lore_item)

        return item_lore

    def get_food_effects(self,tier=""):
        food_effects = []

        for effect in get_item_value(self.item_id, "effects",tier):
            effect_type = effect["effect_type"]
            if effect_type == "cure_effect":
                effect_id = effect["effect"]
                food_effects.append({"type": "remove_effects", "effects": [effect_id]})

            elif effect_type == "cure_effect_set":
                effect_set_id = effect["effect_set"]
                food_effects.append(
                    {
                        "type": "remove_effects",
                        "effects": config["effect_sets"][effect_set_id],
                    }
                )

            elif effect_type == "apply_effect":
                effect_id = effect["effect"]
                effect_duration = 0
                effect_level = 1
                effect_probability = 1
                if "level" in effect:
                    effect_level = effect["level"] - 1
                if "duration_seconds" in effect:
                    effect_duration += effect["duration_seconds"] * 20
                if "duration_ticks" in effect:
                    effect_duration += effect["duration_ticks"]
                if "probability" in effect:
                    effect_probability = effect["probability"]

                effect_data = {
                    "type": "apply_effects",
                    "probability": effect_probability,
                    "effects": [
                        {
                            "id": effect_id,
                            "amplifier": effect_level,
                            "duration": effect_duration,
                        }
                    ],
                }

                food_effects.append(effect_data)

            elif effect_type == "teleport_randomly":
                food_effects.append({"type": "teleport_randomly"})
            elif effect_type == "clear_all_effects":
                food_effects.append({"type": "clear_all_effects"})

        healing = get_item_value(self.item_id, "healing",tier)
        eat_time = get_item_value(self.item_id, "eat_time",tier)

        if healing > 0:
            target_level = 5
            target_level_result = 99999
            for i, v in enumerate(regeneration_values):
                result = (eat_time * 20 / v) - healing

                if 0 <= result <= target_level_result:
                    target_level = i
                    target_level_result = result

            target_duration = healing * regeneration_values[target_level]
            food_effects.append(
                {
                    "type": "apply_effects",
                    "effects": [
                        {
                            "id": "regeneration",
                            "amplifier": target_level,
                            "duration": target_duration,
                            "show_icon": False,
                            "show_particles": False,
                        }
                    ],
                }
            )

        eat_sound_finish = get_item_value(self.item_id, "eat_sound_finish",tier)

        if eat_sound_finish != default_item_data["eat_sound_finish"]:
            food_effects.append(
                {
                    "type": "play_sound",
                    "sound": {"sound_id": "item." + eat_sound_finish + ".consume"},
                }
            )

        return food_effects

    def get_food_effects_lore(self,tier=""):
        food_effect_lore = []

        for effect in get_item_value(self.item_id, "effects",tier):
            effect_type = effect["effect_type"]
            if effect_type == "cure_effect":
                effect_id = effect["effect"]
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food."
                        + effect_type
                        + "."
                        + effect_id,
                        color=self.get_effect_color(effect_id, True),
                    )
                )
            elif effect_type == "cure_effect_set":
                effect_set_id = effect["effect_set"]

                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food."
                        + effect_type
                        + "."
                        + effect_set_id,
                        color="#5555ff",
                    )
                )

            elif effect_type == "apply_effect":
                effect_id = effect["effect"]
                effect_duration = 0
                effect_level = 1
                effect_probability = 1
                if "level" in effect:
                    effect_level = effect["level"] - 1
                if "duration_seconds" in effect:
                    effect_duration += int(effect["duration_seconds"] / 20)
                if "duration_ticks" in effect:
                    effect_duration += effect["duration_ticks"]
                if "probability" in effect:
                    effect_probability = effect["probability"]

                translation_key = (
                    "attribute.name.consumable.food."
                    + effect_type
                    + "."
                    + effect_id
                    + "."
                    + str(effect_level + 1)
                    + "."
                    + str(effect_duration)
                    + "s"
                )
                if effect_probability < 1:
                    effect_probability_percent = (
                        str(int(effect_probability * 100)) + "%"
                    )
                    translation_key += "." + effect_probability_percent

                food_effect_lore.append(
                    self.get_lore_base(
                        translation_key,
                        color=self.get_effect_color(effect_id),
                    )
                )

            elif effect_type == "teleport_randomly":
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food.teleport_randomly",
                        color="#5555ff",
                    )
                )

            elif effect_type == "teleport_forward":
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food.teleport_forward",
                        color="#5555ff",
                    )
                )
            elif effect_type == "unknown_effect":
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food.unknown_effect",
                        color="#5555ff",
                    )
                )
            elif effect_type == "clear_all_effects":
                food_effect_lore.append(
                    self.get_lore_base(
                        "attribute.name.consumable.food.cure_all_effects",
                        color="#5555ff",
                    )
                )
        return food_effect_lore

    def get_effect_color(self, effect, inverted=False):
        if effect in config["effect_sets"]["negative"]:
            if inverted:
                return "#5555ff"
            else:
                return "#ff5555"
        else:
            if inverted:
                return "#ff5555"
            else:
                return "#5555ff"

    def get_value(self):
        result = 0

        nutrition = get_item_value(self.item_id, "food")
        saturation = get_item_value(self.item_id, "saturation")
        healing = get_item_value(self.item_id, "healing")
        always_edible = get_item_value(self.item_id, "always_edible")
        eat_time = get_item_value(self.item_id, "eat_time")
        eat_speed = get_item_value(self.item_id, "eat_speed")

        def get_effect_value(
            effect_id: str,
            effect_level: int,
            effect_duration_ticks: int,
            effect_probability: float,
        ):
            effect_value_result = 0
            healing_result = 0
            if effect_id == "poison":
                poison_rate = regeneration_values[effect_level - 1]
                health_lost = effect_duration_ticks / poison_rate
                if health_lost > 19:
                    healing_result -= 19
                else:
                    healing_result -= health_lost
            elif effect_id == "regeneration" or effect_id == "wither":
                if effect_id == "wither" and effect_level > 3:
                    effect_level = 3
                regeneration_rate = regeneration_values[effect_level - 1]

                eat_time_ticks = eat_time * 20

                if (
                    effect_id == "regeneration"
                    and effect_duration_ticks > eat_time_ticks
                ):
                    healing_result += eat_time_ticks / regeneration_rate
                    healing_result += (
                        (effect_duration_ticks - eat_time_ticks)
                        / regeneration_rate
                        * 0.5
                    )
                else:
                    healing_result += effect_duration_ticks / regeneration_rate

                if effect_id == "wither":
                    healing_result *= -1

            elif effect_id == "instant_health" or effect_id == "instant_damage":
                healing_result += 2 * (2**effect_level) * 2

                if effect_id == "instant_health" and not always_edible:
                    healing_result *= 0.8
                elif effect_id == "instant_damage":
                    healing_result *= -1

            elif effect_id == "absorption":
                healing_result += 4 * effect_level * 2 * 1.5

                if not always_edible:
                    healing_result *= 0.8

            else:
                effect_value_result += effect_level

            if effect_id in config["effect_sets"]["negative"]:
                effect_value_result *= -1

            effect_value_result *= effect_probability
            healing_result *= effect_probability
            return {"effect_value": effect_value_result, "healing": healing_result}

        for effect in get_item_value(self.item_id, "effects"):
            effect_type = effect["effect_type"]
            if effect_type == "cure_effect":
                effect_id = effect["effect"]

                if is_effect_negative(effect_id=effect_id):
                    result += 0.5
                else:
                    result -= 0.5

            elif effect_type == "cure_effect_set":
                effect_set_id = effect["effect_set"]
                for effect_id in config["effect_sets"][effect_set_id]:
                    if is_effect_negative(effect_id=effect_id):
                        result += 0.5
                    else:
                        result -= 0.5

            elif effect_type == "apply_effect":
                effect_id = effect["effect"]
                effect_duration = 0
                effect_level = 1
                effect_probability = 1
                if "level" in effect:
                    effect_level = effect["level"]
                if "duration_seconds" in effect:
                    effect_duration += effect["duration_seconds"] * 20
                if "duration_ticks" in effect:
                    effect_duration += effect["duration_ticks"]
                if "probability" in effect:
                    effect_probability = effect["probability"]

                effect_value_result = get_effect_value(
                    effect_id=effect_id,
                    effect_level=effect_level,
                    effect_duration_ticks=effect_duration,
                    effect_probability=effect_probability,
                )
                result += effect_value_result["effect_value"]
                healing += effect_value_result["healing"]

            elif effect_type == "teleport_randomly":
                result += 0.0
            elif effect_type == "teleport_forward":
                result += 1
            elif effect_type == "unknown_effect":
                pass
            elif effect_type == "clear_all_effects":
                pass

        always_edible_int = int(always_edible)
        result += (
            (nutrition + ((saturation * 1.5) + healing) * ((always_edible_int / 4) + 1))
            * ((2.4 / eat_time) + eat_speed)
        ) / 7.5
        print(self.item_id, result)
        return result
