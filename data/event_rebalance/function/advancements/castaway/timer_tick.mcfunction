execute if score @s event_rebalance.castaway_timer >= 0 static run scoreboard players add @s event_rebalance.castaway_timer 1

execute if score @s event_rebalance.castaway_timer >= 3_days_in_ticks static run advancement grant @s only event_rebalance:food/castaway