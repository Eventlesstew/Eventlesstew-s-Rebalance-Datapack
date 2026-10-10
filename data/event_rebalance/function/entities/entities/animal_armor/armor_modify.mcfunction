summon marker ~ ~ ~ {Tags:["event.animal_armor_marker"]}
execute store result entity @n[type=marker,tag=event.animal_armor_marker] data.speed double 1 run data get entity @s SelectedItem.components."minecraft:enchantments"."event_rebalance:lightweight" 3
function event_rebalance:enchantments/lightweight/animal_armor with entity @n[type=marker,tag=event.animal_armor_marker] data
kill @e[type=marker,tag=event.animal_armor_marker]