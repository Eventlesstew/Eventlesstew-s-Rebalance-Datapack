execute as @e[tag=homing_arrow] at @s run function event_rebalance:enchantments/homing/check_all with entity @s data
execute if entity @e[tag=homing_arrow] run schedule function event_rebalance:enchantments/homing/check_one 1t append
execute as @e[tag=homing_marker] unless predicate {type:"minecraft:entity_properties",entity:"this",predicate:{vehicle:{}}} run kill @s