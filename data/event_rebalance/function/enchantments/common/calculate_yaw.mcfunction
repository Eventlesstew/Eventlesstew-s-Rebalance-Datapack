scoreboard players set MODULO temp 360
scoreboard players operation OFFSET_YAW temp = TARGET_YAW temp
scoreboard players operation OFFSET_YAW temp -= CURRENT_YAW temp

scoreboard players add OFFSET_YAW temp 180
scoreboard players operation OFFSET_YAW temp %= MODULO temp
scoreboard players remove OFFSET_YAW temp 180