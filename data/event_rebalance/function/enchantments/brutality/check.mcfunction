execute store result storage balance.brutality level int 1 run data get entity @s SelectedItem.components."minecraft:enchantments"."event_rebalance:brutality"
data modify storage balance.brutality damage set compute default float event_rebalance:enchantments/brutality
function event_rebalance:enchantments/brutality/apply with storage balance.brutality