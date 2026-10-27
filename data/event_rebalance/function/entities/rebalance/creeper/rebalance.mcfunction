execute unless predicate event_rebalance:mobs/can_see_sky run return fail
execute store result score creeper_y temp run data get entity @s Pos[1]
execute if score creeper_y temp < 60 static run return fail

execute at @s run summon zombie_villager ~ ~ ~
tp @s ~ ~-10000 ~