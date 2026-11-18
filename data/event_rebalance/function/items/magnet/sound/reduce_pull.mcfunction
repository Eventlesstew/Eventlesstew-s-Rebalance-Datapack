execute if entity @s[tag=balance.magnet_pull_sound] run playsound item.magnet.pull master @a ~ ~ ~ 1 1.2
execute if entity @s[tag=balance.netherite_magnet_pull_sound] run playsound item.magnet.pull master @a ~ ~ ~ 2 0.9

execute if score @s balance.magnet_pull_sound matches 1.. run scoreboard players remove @s balance.magnet_pull_sound 1
execute if score @s balance.magnet_pull_sound matches 0 run scoreboard players reset @s balance.magnet_pull_sound

tag @s remove balance.magnet_pull_sound
tag @s remove balance.netherite_magnet_pull_sound