execute store result score DEATH_X temp run data get entity @s Pos[0] 1
execute store result score DEATH_Y temp run data get entity @s Pos[1] 1
execute store result score DEATH_Z temp run data get entity @s Pos[2] 1
execute at @s as @e[type=item] run function event_enchants:bonding