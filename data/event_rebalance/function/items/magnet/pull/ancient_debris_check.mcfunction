$execute anchored eyes if block ^ ^ ^$(distance) ancient_debris run advancement grant @s only event_rebalance:construction/magnet_netherite
$scoreboard players set COUNT_A temp $(distance)
execute store result storage balance.magnet_raycast distance int 1 run scoreboard players add COUNT_A temp 1
execute if entity @s[advancements={event_rebalance:construction/magnet_netherite=false}] unless score COUNT_A temp matches 11.. run function event_rebalance:items/magnet/pull/ancient_debris_check with storage balance.magnet_raycast