tag @s add ricochet_arrow

execute store result score COUNT_A temp run data get entity @s weapon.components."minecraft:enchantments"."event_rebalance:ricochet"
execute store result score COUNT_B temp run data get entity @s item.components."minecraft:enchantments"."event_rebalance:ricochet"
scoreboard players operation COUNT_A temp += COUNT_B temp
execute store result entity @s data.ricochets int 1 run scoreboard players get COUNT_A temp

schedule function event_rebalance:enchantments/ricochet/check_all 1t append