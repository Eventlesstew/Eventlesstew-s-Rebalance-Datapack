execute unless items entity @s event_rebalance:all #event_rebalance:custom_item/lode run return fail
$execute unless items entity @s $(slot) *[enchantments={"event_rebalance:auto_repair":1},damage~{durability:{max:10}}] run return fail

$item modify entity @s $(slot) event_rebalance:enchantment/auto_repair
clear @s #event_rebalance:custom_item/lode 1
scoreboard players set auto_repair_used temp 1