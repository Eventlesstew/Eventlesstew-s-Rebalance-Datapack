execute if entity @s[tag=!event.mounted] run return fail
tag @s remove event.mounted

attribute @s movement_speed modifier remove event_rebalance_speed