$execute if items entity @s $(inventory_slot) *[minecraft:enchantments~[{enchantments:"minecraft:vanishing_curse"}]] run item replace entity @s $(inventory_slot) with air


$execute if items entity @s $(inventory_slot) air run return fail

#$execute if score difficulty temp = 1 static run function event_rebalance:entities/rebalance/player/drop_item_mod_damage {difficulty:easy, inventory_slot:$(inventory_slot)}
$execute if score difficulty temp = 2 static run function event_rebalance:entities/rebalance/player/drop_item_mod_damage {difficulty:normal, inventory_slot:$(inventory_slot)}
$execute if score difficulty temp >= 3 static run function event_rebalance:entities/rebalance/player/drop_item_mod_damage {difficulty:hard, inventory_slot:$(inventory_slot)}
$execute if items entity @s $(inventory_slot) *[max_damage] run return fail
summon item ~ ~ ~ {Tags:["death_item"],Item:{id:"dirt"}}
$item replace entity @n[tag=death_item,type=item] contents from entity @s $(inventory_slot)

$execute if score difficulty temp = 1 static run function event_rebalance:entities/rebalance/player/drop_item_mod {difficulty:easy, inventory_slot:$(inventory_slot)}
$execute if score difficulty temp = 2 static run function event_rebalance:entities/rebalance/player/drop_item_mod {difficulty:normal, inventory_slot:$(inventory_slot)}
$execute if score difficulty temp >= 3 static run function event_rebalance:entities/rebalance/player/drop_item_mod {difficulty:hard, inventory_slot:$(inventory_slot)}

execute store result entity @n[tag=death_item,type=item] Motion[0] float 0.001 run random value -100..100 event_rebalance:death_loot_x
execute store result entity @n[tag=death_item,type=item] Motion[2] float 0.001 run random value -100..100 event_rebalance:death_loot_z
data modify entity @n[tag=death_item,type=item] Motion[1] set value 0.33
tag @n[tag=death_item] remove death_item