execute store result score game_time temp run time query gametime
execute store result score turtle_time_threshold temp run data get entity @s data.ticks_since_last_shed
execute if score game_time temp < turtle_time_threshold temp run return fail

summon item ~ ~ ~ {Item:{id:"turtle_scute"}}
playsound entity.turtle.shamble ambient @a ~ ~ ~

function event_rebalance:entities/rebalance/turtle/reset_shed_time