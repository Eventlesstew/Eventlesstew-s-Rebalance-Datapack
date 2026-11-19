$execute anchored eyes if block ^ ^ ^$(distance) #event_rebalance:magnetic run tag @s add balance.magnet_pull_detect
$scoreboard players set COUNT_A temp $(distance)
execute if score COUNT_A temp matches 0..4 run scoreboard players set @s[tag=balance.magnet_pull_detect] event_rebalance.magnet_pull_strength 5
execute if score COUNT_A temp matches 5..7 run scoreboard players set @s[tag=balance.magnet_pull_detect] event_rebalance.magnet_pull_strength 4
execute if score COUNT_A temp matches 8..10 run scoreboard players set @s[tag=balance.magnet_pull_detect] event_rebalance.magnet_pull_strength 3
execute if score COUNT_A temp matches 11..20 run scoreboard players set @s[tag=balance.magnet_pull_detect] event_rebalance.magnet_pull_strength 2
execute if score COUNT_A temp matches 21..30 run scoreboard players set @s[tag=balance.magnet_pull_detect] event_rebalance.magnet_pull_strength 1
execute store result storage balance.magnet_raycast distance int 1 run scoreboard players add COUNT_A temp 1
execute if entity @s[tag=!balance.magnet_pull_detect] unless score COUNT_A temp matches 31.. run function event_rebalance:items/magnet/pull/netherite_forward with storage balance.magnet_raycast