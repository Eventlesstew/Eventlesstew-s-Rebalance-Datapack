execute if entity @s[tag=!rebalanced] run function event_rebalance:entities/rebalance_entities
function event_rebalance:entities/tick

execute if entity @s[tag=event_rebalance.emitting_light] at @s anchored eyes run function event_rebalance:light/clear