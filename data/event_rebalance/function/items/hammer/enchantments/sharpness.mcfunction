scoreboard players set COUNT_A temp 1
execute store result score COUNT_B temp run data get entity @s SelectedItem.components."minecraft:enchantments"."minecraft:power"
execute store result storage balance.hammer_attack sharpness float 0.5 run scoreboard players operation COUNT_A temp += COUNT_B temp