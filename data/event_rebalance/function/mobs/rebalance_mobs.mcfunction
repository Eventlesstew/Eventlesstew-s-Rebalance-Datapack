tag @s add rebalanced

execute if entity @s[type=#event_rebalance:spawns_with_armor] run function event_rebalance:mobs/modify_armor

execute if entity @s[type=husk] run function event_rebalance:mobs/entities/husk
execute if entity @s[type=zombie_villager] run function event_rebalance:mobs/entities/zombie_villager

execute if entity @s[type=piglin_brute] run function event_rebalance:mobs/entities/piglin_brute

execute if entity @s[type=wither_skeleton] run function event_rebalance:mobs/entities/wither_skeleton