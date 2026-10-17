execute as @e[type=firework_rocket,distance=..3] run tag @s add homing_firework
execute if predicate event_rebalance:enchant/homing/mainhand store result score COUNT_A temp run data get entity @s SelectedItem.components."minecraft:enchantments"."event_rebalance:homing" 1
execute unless predicate event_rebalance:enchant/homing/mainhand if predicate event_rebalance:enchant/homing/offhand store result score COUNT_A temp run data get entity @s equipment.offhand.components."minecraft:enchantments"."event_rebalance:homing" 1
scoreboard players add COUNT_B temp 2
scoreboard players operation COUNT_A temp += COUNT_B temp
execute as @e[type=firework_rocket,tag=homing_firework] run execute store result entity @s data.homing_distance_1 double 0.2 run scoreboard players get COUNT_A temp
execute as @e[type=firework_rocket,tag=homing_firework] run execute store result entity @s data.homing_distance_2 double 0.4 run scoreboard players get COUNT_A temp
execute as @e[type=firework_rocket,tag=homing_firework] run execute store result entity @s data.homing_distance_3 double 0.6 run scoreboard players get COUNT_A temp
execute as @e[type=firework_rocket,tag=homing_firework] run execute store result entity @s data.homing_distance_4 double 0.8 run scoreboard players get COUNT_A temp
execute as @e[type=firework_rocket,tag=homing_firework] run execute store result entity @s data.homing_distance_5 double 1 run scoreboard players get COUNT_A temp

execute as @e[type=firework_rocket,tag=homing_firework] run function event_rebalance:enchantments/homing/start
execute as @e[type=firework_rocket,tag=homing_firework] run tag @s remove homing_firework
advancement revoke @s only event_rebalance:function/enchantments/homing_firework