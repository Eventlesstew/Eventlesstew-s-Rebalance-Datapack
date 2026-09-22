advancement revoke @s only event_rebalance:function/on_player_death

execute unless score @s event.player_deaths >= 1 static run return fail
scoreboard players reset @s event.player_deaths

function event_rebalance:player_death/drop_items_in_inventory