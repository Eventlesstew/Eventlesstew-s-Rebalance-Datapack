advancement revoke @s only event_rebalance:function/use_magnet
attribute @s gravity modifier remove event.magnet
tag @s add event.using_magnet

# Find a better way to do all this
# I suggest using enchants to achieve this.
execute if predicate event_rebalance:item/magnet/pull_up_10 run advancement grant @s only event_rebalance:construction/magnet_up
execute if predicate event_rebalance:item/magnet/advancement/netherite_10 run advancement grant @s only event_rebalance:construction/magnet_netherite

execute if predicate event_rebalance:item/magnet/pull_horizontal_10 run function event_rebalance:items/magnet/horizontal_pull
execute if predicate event_rebalance:item/magnet/pull_down_10 run attribute @s gravity modifier add event.magnet 1 add_multiplied_base
execute if predicate event_rebalance:item/magnet/pull_up_10 run attribute @s gravity modifier add event.magnet -3 add_multiplied_base
