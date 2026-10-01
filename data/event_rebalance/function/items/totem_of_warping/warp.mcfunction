$tp @s $(x) $(y) $(z)
tag @s add balance.totem_of_warping_adjust
schedule function event_rebalance:items/totem_of_warping/adjust_position_check 1t
effect give @s resistance 1 4
effect give @s regeneration 1 5