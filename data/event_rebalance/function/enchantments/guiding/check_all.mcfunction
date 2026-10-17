execute as @e[tag=guide_arrow,tag=!echo_arrow] at @s run function event_rebalance:enchantments/guiding/check_one
execute if entity @e[tag=guide_arrow] run schedule function event_rebalance:enchantments/guiding/check_all 1t append
execute as @e[tag=guiding_marker] unless predicate {type:"minecraft:entity_properties",entity:"this",predicate:{vehicle:{}}} run kill @s