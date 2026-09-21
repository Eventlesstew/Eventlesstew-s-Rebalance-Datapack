tag @s add rebalanced

execute if entity @s[type=#event_rebalance:spawns_with_armor] run function event_rebalance:mobs/modify_armor

execute if entity @s[type=zombie_villager] run function event_rebalance:mobs/entities/zombie_villager