execute unless entity @s[tag=event.block_break_trigger] run return fail

scoreboard players add @s timer 1
execute if score @s timer >= 1200 static run kill
execute if score @s timer >= 1200 static run return fail
#execute as @p if predicate {type:"entity_properties",entity:"this",predicate:{"type_specific/player":{looking_at:{entity_type:"marker"}}}} run say hi
execute unless block ~ ~ ~ #air run return fail
#say hi

execute if entity @s[tag=event.mending_marker] run function event_rebalance:enchantments/mending/block_mined

#kill