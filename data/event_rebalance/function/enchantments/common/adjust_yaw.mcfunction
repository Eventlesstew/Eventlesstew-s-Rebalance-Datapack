execute store result score MOVE_X temp run data get entity @s Motion[0] 10000
execute store result score MOVE_Z temp run data get entity @s Motion[2] 10000

execute store result score RIGHT_X temp run data get entity @s Motion[2] 10000
execute store result score RIGHT_Z temp run data get entity @s Motion[0] 10000

execute if score OFFSET_YAW temp matches ..-15 run scoreboard players set OFFSET_YAW temp -15
execute if score OFFSET_YAW temp matches 15.. run scoreboard players set OFFSET_YAW temp 15

scoreboard players set NEG temp -1
scoreboard players operation RIGHT_X temp *= NEG temp

scoreboard players operation RIGHT_X temp *= OFFSET_YAW temp
scoreboard players operation RIGHT_Z temp *= OFFSET_YAW temp

scoreboard players set SCALE_N temp 1
scoreboard players set SCALE_D temp 100

scoreboard players operation RIGHT_X temp *= SCALE_N temp
scoreboard players operation RIGHT_Z temp *= SCALE_N temp

scoreboard players operation RIGHT_X temp /= SCALE_D temp
scoreboard players operation RIGHT_Z temp /= SCALE_D temp

scoreboard players operation MOVE_X temp += RIGHT_X temp
scoreboard players operation MOVE_Z temp += RIGHT_Z temp

execute store result entity @s Motion[0] double 0.0001 run scoreboard players get MOVE_X temp
execute store result entity @s Motion[2] double 0.0001 run scoreboard players get MOVE_Z temp