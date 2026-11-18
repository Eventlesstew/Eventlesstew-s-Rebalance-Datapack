execute if predicate event_rebalance:item/magnet/pull_up/3 run attribute @s gravity modifier add balance.magnet_pull_up -0.25 add_value
execute if predicate event_rebalance:item/magnet/pull_up/6 run attribute @s gravity modifier add balance.magnet_pull_up -0.19 add_value
execute if predicate event_rebalance:item/magnet/pull_up/10 run attribute @s gravity modifier add balance.magnet_pull_up -0.13 add_value
execute if predicate event_rebalance:item/magnet/pull_up/20 run attribute @s gravity modifier add balance.magnet_pull_up -0.09 add_value
execute if predicate event_rebalance:item/magnet/pull_up/30 run attribute @s gravity modifier add balance.magnet_pull_up -0.05 add_value

execute if predicate event_rebalance:item/magnet/pull_up/20 run attribute @s fall_damage_multiplier modifier add balance.magnet_pull -1 add_multiplied_total
execute if predicate event_rebalance:item/magnet/pull_up/30 run attribute @s fall_damage_multiplier modifier add balance.magnet_pull -0.5 add_multiplied_total
tag @s add balance.magnet_pull_detect