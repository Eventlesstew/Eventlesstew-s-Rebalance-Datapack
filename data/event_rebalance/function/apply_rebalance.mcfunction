advancement revoke @s only event_rebalance:apply_rebalance
execute store result score PLAYER_MODE temp run data get entity @s playerGameType
execute if score PLAYER_MODE temp = 1 static run schedule function event_rebalance:balance_items_for_everyone 1 append
execute unless score PLAYER_MODE temp = 1 static run function event_rebalance:balance_items