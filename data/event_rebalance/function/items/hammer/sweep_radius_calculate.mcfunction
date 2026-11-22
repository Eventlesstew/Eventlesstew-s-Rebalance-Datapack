data modify storage balance.hammer_attack spinner set value 0
execute if predicate event_rebalance:item/hammer/enchantment/spinner store result storage balance.hammer_attack spinner float 1 run data get entity @s SelectedItem.components."minecraft:enchantments"."event_rebalance:spinner"
data modify storage balance.hammer_attack sweep_radius set compute default float event_rebalance:items/hammer/sweep_radius
data modify storage balance.hammer_attack sweep_center_distance set compute default float event_rebalance:items/hammer/sweep_center_distance