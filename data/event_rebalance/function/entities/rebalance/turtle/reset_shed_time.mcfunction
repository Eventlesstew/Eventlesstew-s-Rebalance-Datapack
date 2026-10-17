execute store result score turtle_time temp run time query gametime
scoreboard players add turtle_time temp 6000
execute store result entity @s data.ticks_since_last_shed int 1 run scoreboard players get turtle_time temp