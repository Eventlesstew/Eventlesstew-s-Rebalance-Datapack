summon marker ~ ~ ~ {Tags:[event.compass]}
data modify entity @n[type=marker, tag=event.speed_meter] data.x set from entity @s Motion[0]
data modify entity @n[type=marker, tag=event.speed_meter] data.y set from entity @s Motion[1]
data modify entity @n[type=marker, tag=event.speed_meter] data.z set from entity @s Motion[2]

execute store result score PLAYER_ROTATION_YAW temp run data get entity @s Rotation[0] 10

execute if score -225 static <= PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp <= 225 static run data modify entity @n[type=marker, tag=event.speed_meter] data.dir set value "n"
execute if score 225 static < PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp < 675 static run data modify entity @n[type=marker, tag=event.speed_meter] data.dir set value "ne"
execute if score 675 static <= PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp <= 1125 static run data modify entity @n[type=marker, tag=event.speed_meter] data.dir set value "e"
execute if score 1125 static < PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp < 1575 static run data modify entity @n[type=marker, tag=event.speed_meter] data.dir set value "se"
execute if score 1575 static <= PLAYER_ROTATION_YAW temp run data modify entity @n[type=marker, tag=event.speed_meter] data.dir set value "s"
execute if score PLAYER_ROTATION_YAW temp <= -1575 static run data modify entity @n[type=marker, tag=event.speed_meter] data.dir set value "s"
execute if score -1575 static < PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp < -1125 static run data modify entity @n[type=marker, tag=event.speed_meter] data.dir set value "sw"
execute if score -1125 static <= PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp <= -675 static run data modify entity @n[type=marker, tag=event.speed_meter] data.dir set value "w"
execute if score -675 static < PLAYER_ROTATION_YAW temp if score PLAYER_ROTATION_YAW temp < -225 static run data modify entity @n[type=marker, tag=event.speed_meter] data.dir set value "nw"

function event_rebalance:items/compass/display with entity @n[type=marker, tag=event.compass] data
kill @n[type=marker, tag=event.compass]