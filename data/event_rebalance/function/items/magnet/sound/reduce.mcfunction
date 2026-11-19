execute if entity @s[tag=balance.magnet_sound] run playsound item.magnet.use master @a ~ ~ ~ 1 1
execute if entity @s[tag=balance.netherite_magnet_sound] run playsound item.magnet.use master @a ~ ~ ~ 2 0.7

execute if score @s event_rebalance.magnet_sound matches 1.. run scoreboard players remove @s event_rebalance.magnet_sound 1
execute if score @s event_rebalance.magnet_sound matches 0 run scoreboard players reset @s event_rebalance.magnet_sound

tag @s remove balance.magnet_sound
tag @s remove balance.netherite_magnet_sound