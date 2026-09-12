tag @s add lasting
execute as @e[type=item] if data entity @s Item.components."minecraft:enchantments"."event_rebalance:lasting" run function event_rebalance:player_death/lasting_give_item

tag @s remove lasting