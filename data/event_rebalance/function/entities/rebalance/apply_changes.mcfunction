tag @s add rebalanced

function event_rebalance:entities/rebalance/common/inventory
execute if entity @s[tag=sits_on_cushion] run function event_rebalance:entities/rebalance/common/sit_on_cushion


# General
execute if entity @s[type=armor_stand] run function event_rebalance:entities/rebalance/armor_stand/rebalance
execute if entity @s[type=item] run function event_rebalance:entities/rebalance/item/rebalance
execute if entity @s[type=arrow] run function event_rebalance:entities/rebalance/arrow/rebalance

# Overworld Animals
execute if entity @s[type=goat] run function event_rebalance:entities/rebalance/goat/rebalance
execute if entity @s[type=turtle] run function event_rebalance:entities/rebalance/turtle/rebalance

# Overworld
execute if entity @s[type=villager] run function event_rebalance:entities/rebalance/zombie/rebalance

execute if entity @s[type=zombie] run function event_rebalance:entities/rebalance/zombie/rebalance
execute if entity @s[type=zombie_villager] run function event_rebalance:entities/rebalance/zombie_villager/rebalance
execute if entity @s[type=husk] run function event_rebalance:entities/rebalance/husk/rebalance
execute if entity @s[type=drowned] run function event_rebalance:entities/rebalance/drowned/rebalance

execute if entity @s[type=skeleton] run function event_rebalance:entities/rebalance/skeleton/rebalance
execute if entity @s[type=stray] run function event_rebalance:entities/rebalance/stray/rebalance
execute if entity @s[type=bogged] run function event_rebalance:entities/rebalance/bogged/rebalance
execute if entity @s[type=parched] run function event_rebalance:entities/rebalance/parched/rebalance

execute if entity @s[type=spider] run function event_rebalance:entities/rebalance/spider/rebalance
execute if entity @s[type=cave_spider] run function event_rebalance:entities/rebalance/cave_spider/rebalance

execute if entity @s[type=creeper] run function event_rebalance:entities/rebalance/creeper/rebalance

# Nether
execute if entity @s[type=blaze] run function event_rebalance:entities/rebalance/blaze/rebalance
execute if entity @s[type=piglin_brute] run function event_rebalance:entities/rebalance/piglin_brute/rebalance