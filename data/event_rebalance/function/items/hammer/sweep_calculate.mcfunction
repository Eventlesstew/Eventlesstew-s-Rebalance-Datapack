data modify storage balance.hammer_attack sweeping_edge set value 0
execute if predicate event_rebalance:item/hammer/enchantment/sweeping_edge store result storage balance.hammer_attack sweeping_edge float 0.2 run data get entity @s SelectedItem.components."minecraft:enchantments"."minecraft:sweeping_edge"
data modify storage balance.hammer_attack sweep set compute default float event_rebalance:items/hammer/sweep
function event_rebalance:items/hammer/base_damage with storage balance.hammer_attack