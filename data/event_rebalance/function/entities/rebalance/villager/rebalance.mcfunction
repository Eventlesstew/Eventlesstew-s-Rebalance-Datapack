execute if entity @s[tag=spawn_villager] run function event_rebalance:entities/rebalance/villager/respawn
execute if entity @s[tag=spawn_villager] run return fail

attribute @s armor modifier add balance 8 add_value