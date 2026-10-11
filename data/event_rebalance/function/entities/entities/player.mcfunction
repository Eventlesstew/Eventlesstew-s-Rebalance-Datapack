function event_rebalance:advancements/castaway/timer_tick

execute unless score @s event.player_deaths >= 1 static run return fail
scoreboard players reset @s event.player_deaths
function event_rebalance:items/crystal_heart/on_death