#execute if predicate event_rebalance:item/magnet/pull_no_vertical_10 run attribute @s gravity modifier add event.magnet -1 add_multiplied_base
execute if predicate event_rebalance:item/magnet/pull_east_10 facing ~10 ~ ~ run function event_rebalance:items/magnet/pull_user
execute if predicate event_rebalance:item/magnet/pull_south_10 facing ~ ~ ~10 run function event_rebalance:items/magnet/pull_user
execute if predicate event_rebalance:item/magnet/pull_west_10 facing ~-10 ~ ~ run function event_rebalance:items/magnet/pull_user
execute if predicate event_rebalance:item/magnet/pull_north_10 facing ~ ~ ~-10 run function event_rebalance:items/magnet/pull_user