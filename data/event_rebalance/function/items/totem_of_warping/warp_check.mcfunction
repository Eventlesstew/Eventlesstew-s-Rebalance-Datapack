$execute store success score COUNT_A temp run forceload add $(x) $(z)
$execute if block $(x) $(y) $(z) #beds run function event_rebalance:items/totem_of_warping/warp {x:$(x),y:$(y),z:$(z)}
$execute if block $(x) $(y) $(z) respawn_anchor unless block $(x) $(y) $(z) respawn_anchor[charges=0] run function event_rebalance:items/totem_of_warping/warp {x:$(x),y:$(y),z:$(z)}
$execute if data entity @s respawn.forced run function event_rebalance:items/totem_of_warping/forced_warp {x:$(x),y:$(y),z:$(z)}
$execute if score COUNT_A temp matches 1 run forceload remove $(x) $(z)