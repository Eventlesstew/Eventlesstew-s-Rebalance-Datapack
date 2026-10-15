summon marker ~ ~ ~ {Tags:[event.compass]}
execute store result storage event_rebalance:compass x double 1 run data get entity @s Pos[0] 1
execute store result storage event_rebalance:compass y double 1 run data get entity @s Pos[1] 1
execute store result storage event_rebalance:compass z double 1 run data get entity @s Pos[2] 1

data modify entity @n[type=marker, tag=event.compass] data.x set compute default float event_rebalance:compass/x
data modify entity @n[type=marker, tag=event.compass] data.y set compute default float event_rebalance:compass/y
data modify entity @n[type=marker, tag=event.compass] data.z set compute default float event_rebalance:compass/z

execute store result score PLAYER_ROTATION_YAW temp run data get entity @s Rotation[0] 10

execute if score PLAYER_ROTATION_YAW temp <= -1575 static run data modify entity @n[type=marker, tag=event.compass] data.dir set value "s"
execute if score -1575 static < PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp < -1125 static run data modify entity @n[type=marker, tag=event.compass] data.dir set value "sw"
execute if score -1125 static <= PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp <= -675 static run data modify entity @n[type=marker, tag=event.compass] data.dir set value "w"
execute if score -675 static < PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp < -225 static run data modify entity @n[type=marker, tag=event.compass] data.dir set value "nw"
execute if score -225 static <= PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp <= 225 static run data modify entity @n[type=marker, tag=event.compass] data.dir set value "n"
execute if score 225 static < PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp < 675 static run data modify entity @n[type=marker, tag=event.compass] data.dir set value "ne"
execute if score 675 static <= PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp <= 1125 static run data modify entity @n[type=marker, tag=event.compass] data.dir set value "e"
execute if score 1125 static < PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp < 1575 static run data modify entity @n[type=marker, tag=event.compass] data.dir set value "se"
execute if score 1575 static <= PLAYER_ROTATION_YAW temp run data modify entity @n[type=marker, tag=event.compass] data.dir set value "s"

function event_rebalance:items/compass/display with entity @n[type=marker, tag=event.compass] data
kill @n[type=marker, tag=event.compass]