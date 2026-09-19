scoreboard players add @s event_rebalance.acceleration_count 1
summon marker ~ ~ ~ {Tags:["balance.acceleration_marker"]}
execute store result entity @n[type=marker,tag=balance.acceleration_marker] data.acceleration_count double 1 run scoreboard players get @s event_rebalance.acceleration_count
execute store result entity @n[type=marker,tag=balance.acceleration_marker] data.acceleration_level int 1 run data get entity @s equipment.legs.components."minecraft:enchantments"."event_rebalance:acceleration" 1
function event_rebalance:enchantments/acceleration/calc with entity @n[type=marker,tag=balance.acceleration_marker] data