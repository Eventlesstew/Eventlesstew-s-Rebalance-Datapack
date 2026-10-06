execute if entity @s[tag=!balance.borer] run playsound enchant.felling.activate master @a ~ ~ ~ 0.6 1.4
tag @s[tag=!balance.borer] add balance.borer
summon marker ~ ~ ~ {Tags:["balance.borer_marker"]}
execute store result entity @n[type=marker,tag=balance.borer_marker] data.block_range double 1 run data get entity @s SelectedItem.components."minecraft:enchantments"."event_rebalance:felling" 4
#execute store result entity @n[type=marker,tag=balance.borer_marker] data.mining_speed double 1 run data get entity @s SelectedItem.components."minecraft:enchantments"."event_rebalance:felling" 16
function event_rebalance:enchantments/felling/effect with entity @n[type=marker,tag=balance.borer_marker] data
kill @e[type=marker,tag=balance.borer_marker]