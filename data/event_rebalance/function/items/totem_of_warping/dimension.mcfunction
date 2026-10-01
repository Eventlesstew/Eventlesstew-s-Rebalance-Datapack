execute store result storage balance.totem_of_warping data.x double 1 run data get entity @s respawn.pos[0]
execute store result storage balance.totem_of_warping data.y double 1 run data get entity @s respawn.pos[1]
execute store result storage balance.totem_of_warping data.z double 1 run data get entity @s respawn.pos[2]
$execute in $(dimension) run function event_rebalance:items/totem_of_warping/warp_check with storage balance.totem_of_warping data