attribute @s attack_damage modifier remove balance.squeeze
scoreboard players set @s balance.squeeze_active 1
scoreboard players set COUNT_A temp 1
execute store result score COUNT_B temp run data get entity @s SelectedItem.components."minecraft:enchantments"."event_rebalance:squeeze"
execute store result storage balance.hammer_attack squeeze_single float 0.25 run scoreboard players operation COUNT_A temp += COUNT_B temp
tag @s add balance.hammer_attacker
function event_rebalance:items/hammer/sweep_radius_calculate
function event_rebalance:items/hammer/enchantments/squeeze/radius with storage balance.hammer_attack
function event_rebalance:items/hammer/enchantments/squeeze/tag with storage balance.hammer_attack
kill @e[type=marker,tag=balance.squeeze_area]
tag @s remove balance.hammer_attacker
data modify storage balance.hammer_attack squeeze set compute default float event_rebalance:items/hammer/enchantment/squeeze
function event_rebalance:items/hammer/enchantments/squeeze/damage with storage balance.hammer_attack