summon marker ^ ^ ^10 {Tags:[fireball]}
#summon fireball ^ ^ ^10 {Tags:[fireball]}
execute store result storage event_rebalance:fireball origin_x float 1 run data get entity @s Pos[0]
execute store result storage event_rebalance:fireball origin_y float 1 run data get entity @s Pos[1]
execute store result storage event_rebalance:fireball origin_z float 1 run data get entity @s Pos[2]
execute store result storage event_rebalance:fireball shoot_x float 1 run data get entity @n[tag=fireball] Pos[0]
execute store result storage event_rebalance:fireball shoot_y float 1 run data get entity @n[tag=fireball] Pos[1]
execute store result storage event_rebalance:fireball shoot_z float 1 run data get entity @n[tag=fireball] Pos[2]
kill @n[type=marker,tag=fireball]

$execute anchored eyes run summon $(fireball) ^ ^ ^
$tag @n[type=$(fireball)] add player_summoned

data modify entity @n[tag=player_summoned] Owner set from entity @s UUID
execute store result entity @n[tag=player_summoned] Motion[0] float 0.0001 run compute default float event_rebalance:items/motion/x 1
execute store result entity @n[tag=player_summoned] Motion[1] float 0.0001 run compute default float event_rebalance:items/motion/y 1
execute store result entity @n[tag=player_summoned] Motion[2] float 0.0001 run compute default float event_rebalance:items/motion/z 1
tag @n[tag=player_summoned] remove player_summoned