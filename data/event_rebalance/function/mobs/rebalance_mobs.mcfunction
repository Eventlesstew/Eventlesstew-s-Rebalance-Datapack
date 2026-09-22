tag @s add rebalanced

# Removes Chainmail Armor from spawned mobs.
execute if entity @s[type=#event_rebalance:spawns_with_armor] run function event_rebalance:mobs/modify_armor

# General
execute if entity @s[type=item] run function event_rebalance:mobs/entities/item

# Overworld
execute if entity @s[type=husk] run function event_rebalance:mobs/entities/husk
execute if entity @s[type=zombie_villager] run function event_rebalance:mobs/entities/zombie_villager
execute if entity @s[type=creeper] run function event_rebalance:mobs/entities/creeper

# Nether
execute if entity @s[type=piglin_brute] run function event_rebalance:mobs/entities/piglin_brute
execute if entity @s[type=wither_skeleton] run function event_rebalance:mobs/entities/wither_skeleton