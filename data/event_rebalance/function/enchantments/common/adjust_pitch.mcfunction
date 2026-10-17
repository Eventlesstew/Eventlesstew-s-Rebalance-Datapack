execute store result score MOVE_Y temp run data get entity @s Motion[1] 10000

scoreboard players set SCALE_N temp 500
scoreboard players set SCALE_D temp 90

# scoreboard players remove @s OFFSET_PITCH 45

scoreboard players operation RIGHT_Y temp = OFFSET_PITCH temp
scoreboard players operation RIGHT_Y temp *= SCALE_N temp
scoreboard players operation RIGHT_Y temp /= SCALE_D temp

scoreboard players operation MOVE_Y temp += RIGHT_Y temp
execute store result entity @s Motion[1] double 0.0001 run scoreboard players get MOVE_Y temp