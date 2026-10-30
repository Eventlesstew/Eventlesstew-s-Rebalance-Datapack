execute if entity @s[tag=event.mounted] run return fail
tag @s add event.mounted

execute if entity @s[type=horse] run attribute @s movement_speed modifier add event_rebalance_speed 1.5 add_multiplied_base
execute if entity @s[type=zombie_horse] run attribute @s movement_speed modifier add event_rebalance_speed 1.5 add_multiplied_base
execute if entity @s[type=skeleton_horse] run attribute @s movement_speed modifier add event_rebalance_speed 1.5 add_multiplied_base
execute if entity @s[type=donkey] run attribute @s movement_speed modifier add event_rebalance_speed 1.5 add_multiplied_base
execute if entity @s[type=mule] run attribute @s movement_speed modifier add event_rebalance_speed 1.5 add_multiplied_base
execute if entity @s[type=camel] run attribute @s movement_speed modifier add event_rebalance_speed 1.5 add_multiplied_base
execute if entity @s[type=camel_husk] run attribute @s movement_speed modifier add event_rebalance_speed 1.5 add_multiplied_base
execute if entity @s[type=pig] run attribute @s movement_speed modifier add event_rebalance_speed 3 add_multiplied_base
execute if entity @s[type=strider] run attribute @s movement_speed modifier add event_rebalance_speed 2 add_multiplied_base

execute if entity @s[type=nautilus] run attribute @s movement_speed modifier add event_rebalance_speed 1.5 add_multiplied_base
execute if entity @s[type=zombie_nautilus] run attribute @s movement_speed modifier add event_rebalance_speed 1.5 add_multiplied_base