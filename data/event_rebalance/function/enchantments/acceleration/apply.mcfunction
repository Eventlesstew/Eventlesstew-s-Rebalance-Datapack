attribute @s movement_speed modifier remove balance.acceleration
$attribute @s movement_speed modifier add balance.acceleration $(acceleration_count) add_multiplied_base
kill @e[type=marker,tag=balance.acceleration_marker]
tag @s add balance.acceleration