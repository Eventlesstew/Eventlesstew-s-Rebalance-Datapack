execute if entity @a[advancements={event_rebalance:husbandry/castaway=false}] run function event_rebalance:advancements/castaway/timer_tick

execute unless entity @s[tag=event.using_magnet] run attribute @s gravity modifier remove event.magnet
tag @s remove event.using_magnet

execute if score @s event.player_deaths >= 1 static run function event_rebalance:entities/rebalance/player/on_respawn