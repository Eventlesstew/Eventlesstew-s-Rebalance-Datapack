execute if entity @s[tag=event.channeling_triggered] run return fail
tag @s add event.channeling_triggered
execute as @e[distance=..20,type=#event_rebalance:mobs] at @s if predicate event_rebalance:mobs/in_water run damage @s 8 event_rebalance:electricity at ~ ~ ~