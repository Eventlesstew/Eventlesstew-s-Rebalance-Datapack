tag @s add homing_arrow
execute store result score COUNT_A temp run data get entity @s weapon.components."minecraft:enchantments"."event_rebalance:homing" 1
scoreboard players set COUNT_B temp 2
scoreboard players operation COUNT_A temp += COUNT_B temp
execute store result entity @s[type=#arrows] data.homing_distance_1 double 0.2 run scoreboard players get COUNT_A temp
execute store result entity @s[type=#arrows] data.homing_distance_2 double 0.4 run scoreboard players get COUNT_A temp
execute store result entity @s[type=#arrows] data.homing_distance_3 double 0.6 run scoreboard players get COUNT_A temp
execute store result entity @s[type=#arrows] data.homing_distance_4 double 0.8 run scoreboard players get COUNT_A temp
execute store result entity @s[type=#arrows] data.homing_distance_5 double 1 run scoreboard players get COUNT_A temp

data modify entity @s data.old_x set from entity @s Pos[0]
data modify entity @s data.old_y set from entity @s Pos[1]
data modify entity @s data.old_z set from entity @s Pos[2]

summon marker ~ ~ ~ {Tags:["homing_marker"]}
ride @n[tag=homing_marker] mount @s

schedule function event_rebalance:enchantments/homing/check_all 1t append