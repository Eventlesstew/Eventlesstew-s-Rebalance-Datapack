effect give @s weakness infinite 1 true

attribute @s max_health modifier add event_rebalance 0.5 add_multiplied_base
attribute @s follow_range modifier add event_rebalance -0.5 add_multiplied_base
attribute @s movement_speed modifier add event_rebalance -0.25 add_multiplied_base

effect give @s instant_damage 1 6 true