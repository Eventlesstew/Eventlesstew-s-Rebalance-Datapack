tag @s add rebalanced

# Removes Chainmail Armor from spawned mobs.
execute if entity @s[type=#event_rebalance:spawns_with_armor] run function event_rebalance:entities/modify_armor

# General
execute if entity @s[type=item] run function event_rebalance:entities/rebalance/item
execute if entity @s[type=arrow] run function event_rebalance:entities/rebalance/arrow

# Overworld
execute if entity @s[type=zombie] run function event_rebalance:entities/rebalance/zombie
execute if entity @s[type=skeleton] run function event_rebalance:entities/rebalance/skeleton
execute if entity @s[type=husk] run function event_rebalance:entities/rebalance/husk
execute if entity @s[type=spider] run function event_rebalance:entities/rebalance/spider
execute if entity @s[type=cave_spider] run function event_rebalance:entities/rebalance/cave_spider
execute if entity @s[type=zombie_villager] run function event_rebalance:entities/rebalance/zombie_villager
execute if entity @s[type=creeper] run function event_rebalance:entities/rebalance/creeper

# Nether
execute if entity @s[type=piglin_brute] run function event_rebalance:entities/rebalance/piglin_brute
execute if entity @s[type=wither_skeleton] run function event_rebalance:entities/rebalance/wither_skeleton