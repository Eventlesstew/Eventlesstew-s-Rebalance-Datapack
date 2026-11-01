$execute if items entity @s $(inventory_slot) *[minecraft:enchantments~[{enchantments:"minecraft:vanishing_curse"}]] run item replace entity @s $(inventory_slot) with air

$execute if items entity @s $(inventory_slot) air run return fail
$execute if items entity @s $(inventory_slot) *[max_damage] run item modify entity @s $(inventory_slot) event_rebalance:function/death_damage
$execute if items entity @s $(inventory_slot) *[max_damage] run return fail

#execute if items entity @s container.0 *[max_damage] run say hi
# Drop the item
summon item ~ ~ ~ {Tags:["death_item"],Item:{id:"dirt"}}

$item replace entity @n[tag=death_item,type=item] contents from entity @s $(inventory_slot)
item modify entity @n[tag=death_item,type=item] contents event_rebalance:function/death_item_drop
$item modify entity @s $(inventory_slot) event_rebalance:function/death_item_keep

execute store result entity @n[tag=death_item,type=item] Motion[0] float 0.001 run random value -100..100 event_rebalance:death_loot_x
execute store result entity @n[tag=death_item,type=item] Motion[2] float 0.001 run random value -100..100 event_rebalance:death_loot_z
data modify entity @n[tag=death_item,type=item] Motion[1] set value 0.33
tag @n[tag=death_item] remove death_item