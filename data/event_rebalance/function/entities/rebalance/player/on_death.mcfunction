advancement revoke @s only event_rebalance:function/on_player_hurt

execute unless score @s event.player_deaths >= 1 static run return fail

# function event_rebalance:player_death/drop_items_in_inventory