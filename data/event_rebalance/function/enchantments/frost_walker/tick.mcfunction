execute store result score fall_distance temp run data get entity @s fall_distance 1
execute store result score safe_fall_distance temp run attribute @s safe_fall_distance get 1
tag @s remove event.frost_walker.falling
execute if score fall_distance temp > safe_fall_distance temp run tag @s add event.frost_walker.falling