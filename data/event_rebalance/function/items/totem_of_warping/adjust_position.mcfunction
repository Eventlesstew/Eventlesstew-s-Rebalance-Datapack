execute if block ~ ~ ~ respawn_anchor run function event_rebalance:items/totem_of_warping/respawn_anchor_deplete
execute unless block ~ ~ ~ #event_rebalance:passable if block ~ ~ ~-1 #event_rebalance:passable if block ~ ~1 ~-1 #event_rebalance:passable unless block ~ ~-1 ~-1 #event_rebalance:passable run tp ~ ~ ~-1
execute unless block ~ ~ ~ #event_rebalance:passable if block ~ ~ ~1 #event_rebalance:passable if block ~ ~1 ~1 #event_rebalance:passable unless block ~ ~-1 ~1 #event_rebalance:passable run tp ~ ~ ~1
execute unless block ~ ~ ~ #event_rebalance:passable if block ~-1 ~ ~ #event_rebalance:passable if block ~-1 ~1 ~ #event_rebalance:passable unless block ~-1 ~-1 ~ #event_rebalance:passable run tp ~-1 ~ ~
execute unless block ~ ~ ~ #event_rebalance:passable if block ~1 ~ ~ #event_rebalance:passable if block ~1 ~1 ~ #event_rebalance:passable unless block ~1 ~-1 ~ #event_rebalance:passable run tp ~1 ~ ~
tag @s remove balance.totem_of_warping_adjust