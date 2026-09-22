$execute if items entity @s $(inventory_slot) air run return fail

# Check if the item has the Lasting enchantment on
$execute if items entity @s $(inventory_slot) *[minecraft:enchantments~[{enchantments:"event_rebalance:lasting"}]] run return fail

# Drop the item
summon item ~ ~ ~ {Tags:["death_item"],Item:{id:"dirt"}}
$item replace entity @n[tag=death_item,type=item] contents from entity @s $(inventory_slot)
$item replace entity @s $(inventory_slot) with air

tag @n[tag=death_item] remove death_item