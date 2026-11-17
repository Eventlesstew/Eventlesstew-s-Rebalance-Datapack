$scoreboard players add @s balance.acceleration_count $(lunge_level)
$scoreboard players add @s balance.acceleration_count $(dashing_level)
summon marker ~ ~ ~ {Tags:["balance.acceleration_marker"]}
execute store result entity @n[type=marker,tag=balance.acceleration_marker] data.acceleration_count double 1 run scoreboard players get @s event_rebalance.acceleration_count
execute unless entity @s[type=#event_rebalance:can_wear_animal_armor] store result entity @n[type=marker,tag=balance.acceleration_marker] data.acceleration_level int 1 run data get entity @s equipment.legs.components."minecraft:enchantments"."event_rebalance:acceleration" 1
execute if entity @s[type=#event_rebalance:can_wear_animal_armor] store result entity @n[type=marker,tag=balance.acceleration_marker] data.acceleration_level int 1 run data get entity @s equipment.body.components."minecraft:enchantments"."event_rebalance:acceleration" 1
function event_rebalance:enchantments/acceleration/calc with entity @n[type=marker,tag=balance.acceleration_marker] data