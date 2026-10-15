execute unless entity @s[tag=event.speed_meter] run return fail

execute store result storage event_rebalance:speed_meter x_prev float 100 run data get entity @n[type=marker, tag=event.speed_meter] Pos[0] 100
execute store result storage event_rebalance:speed_meter y_prev float 100 run data get entity @n[type=marker, tag=event.speed_meter] Pos[1] 100
execute store result storage event_rebalance:speed_meter z_prev float 100 run data get entity @n[type=marker, tag=event.speed_meter] Pos[2] 100
kill @n[type=marker, tag=event.speed_meter]

execute unless predicate event_rebalance:item/speed_meter/holding run return fail

summon marker ~ ~ ~ {Tags:[event.speed_meter]}

execute store result storage event_rebalance:speed_meter x float 100 run data get entity @n[type=marker, tag=event.speed_meter] Pos[0] 100
execute store result storage event_rebalance:speed_meter y float 100 run data get entity @n[type=marker, tag=event.speed_meter] Pos[1] 100
execute store result storage event_rebalance:speed_meter z float 100 run data get entity @n[type=marker, tag=event.speed_meter] Pos[2] 100

data modify entity @n[type=marker, tag=event.speed_meter] data.x set compute default float event_rebalance:speed_meter/horizontal
data modify entity @n[type=marker, tag=event.speed_meter] data.y set compute default float event_rebalance:speed_meter/vertical

function event_rebalance:items/speed_meter/display with entity @n[type=marker, tag=event.speed_meter] data