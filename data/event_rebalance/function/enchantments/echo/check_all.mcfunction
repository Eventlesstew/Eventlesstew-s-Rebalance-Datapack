execute as @e[tag=echo_arrow] at @s run function event_rebalance:enchantments/echo/create_bow
execute as @e[tag=echo_item] at @s run function event_rebalance:enchantments/echo/check_one

execute if entity @e[tag=echo_arrow] run schedule function event_rebalance:enchantments/echo/check_all 1t append
execute if entity @e[tag=echo_item] run schedule function event_rebalance:enchantments/echo/check_all 1t append