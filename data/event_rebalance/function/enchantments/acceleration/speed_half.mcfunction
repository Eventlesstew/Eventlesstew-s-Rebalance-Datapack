scoreboard players remove @s event_rebalance.acceleration_count 5
execute if score @s event_rebalance.acceleration_count matches ..0 run scoreboard players set @s event_rebalance.acceleration_count 0
summon marker ~ ~ ~ {Tags:["balance.acceleration_marker"]}
execute store result entity @n[type=marker,tag=balance.acceleration_marker] data.acceleration_count double 1 run scoreboard players get @s event_rebalance.acceleration_count
execute store result entity @n[type=marker,tag=balance.acceleration_marker] data.acceleration_level int 1 run data get entity @s equipment.legs.components."minecraft:enchantments"."event_rebalance:acceleration" 1
function event_rebalance:enchantments/acceleration/calc with entity @n[type=marker,tag=balance.acceleration_marker] data