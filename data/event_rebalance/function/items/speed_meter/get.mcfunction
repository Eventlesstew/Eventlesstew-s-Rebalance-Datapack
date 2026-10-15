summon marker ~ ~ ~ {Tags:[event.speed_meter]}
execute store result storage event_rebalance:speed_meter x double 1 run data get entity @s Motion[0] 1
execute store result storage event_rebalance:speed_meter y double 1 run data get entity @s Motion[1] 1
execute store result storage event_rebalance:speed_meter z double 1 run data get entity @s Motion[2] 1

data modify entity @n[type=marker, tag=event.speed_meter] data.x set compute default float event_rebalance:speed_meter_x
data modify entity @n[type=marker, tag=event.speed_meter] data.y set compute default float event_rebalance:speed_meter_y


function event_rebalance:items/speed_meter/display with entity @n[type=marker, tag=event.speed_meter] data
kill @n[type=marker, tag=event.speed_meter]