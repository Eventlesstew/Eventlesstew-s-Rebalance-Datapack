scoreboard players set felling temp 0
execute if entity @s[x_rotation=70..90] run scoreboard players set felling temp 1
execute if entity @s[x_rotation=-90..-70] run scoreboard players set felling temp 1

execute if score felling temp = 1 static run function event_rebalance:enchantments/felling/activate
execute unless score felling temp = 1 static run function event_rebalance:enchantments/felling/deactivate