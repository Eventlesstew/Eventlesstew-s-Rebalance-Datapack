$execute unless data entity @s Inventory[{Slot:$(data_slot)}] run return fail

summon item ~ ~ ~ {Tags:["death_item"],Item:{id:"dirt"}}
$data modify entity @n[tag=death_item,type=item] Item set from entity @s Inventory[{Slot:$(data_slot)}]
tag @n[tag=death_item] remove death_item

$item replace entity @s inventory.$(inventory_slot) with air