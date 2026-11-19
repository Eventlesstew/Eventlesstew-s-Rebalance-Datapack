execute if predicate event_rebalance:mobs/can_see_sky run tag @s add event.replace
execute store result score creeper_y temp run data get entity @s Pos[1]
execute if score creeper_y temp >= 60 static run tag @s add event.replace

execute unless entity @s[tag=event.replace] run return fail
summon zombie_villager ~ ~ ~
tp @s ~ ~-10000 ~