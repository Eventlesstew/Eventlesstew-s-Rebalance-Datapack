# Add a bit of jitter, so the echo arrows aren't identical
execute store result score MOVE_X temp run data get entity @s Motion[0] 10000
execute store result score MOVE_Y temp run data get entity @s Motion[1] 10000
execute store result score MOVE_Z temp run data get entity @s Motion[2] 10000

# Add some jitter, with lower amounts of jitter for higher levels
scoreboard players set MAX_JITTER temp 240
scoreboard players operation MAX_JITTER temp -= JITTER temp
execute if score MAX_JITTER temp matches ..0 run scoreboard players set MAX_JITTER temp 0
execute store result storage balance:tmp jitter int 1 run scoreboard players get MAX_JITTER temp
function event_rebalance:enchantments/common/add_jitter_b with storage balance:tmp

scoreboard players operation MOVE_X temp += JITTER_X temp
scoreboard players operation MOVE_Y temp += JITTER_Y temp
scoreboard players operation MOVE_Z temp += JITTER_Z temp

# Apply the final motion
execute store result entity @s Motion[0] double 0.0001 run scoreboard players get MOVE_X temp
execute store result entity @s Motion[1] double 0.0001 run scoreboard players get MOVE_Y temp
execute store result entity @s Motion[2] double 0.0001 run scoreboard players get MOVE_Z temp

data modify entity @n[tag=new_arrow] Tags set from entity @s data.Tags
