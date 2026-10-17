# If we're not in the ground, store motion then return
execute unless entity @s[nbt={inGround:1b}] run return run function event_rebalance:enchantments/ricochet/store_motion
execute unless entity @s[nbt={LeftOwner:1b}] run return 0

particle item{item:"slime_ball"} ~ ~0.125 ~ 0.125 0.125 0.125 0.125 5

scoreboard players set MOD temp 625
scoreboard players set NEG temp -1

execute store result score POS_X temp run data get entity @s Pos[0] 10000
execute store result score POS_Y temp run data get entity @s Pos[1] 10000
execute store result score POS_Z temp run data get entity @s Pos[2] 10000

scoreboard players operation POS_X temp %= MOD temp
scoreboard players operation POS_Y temp %= MOD temp
scoreboard players operation POS_Z temp %= MOD temp

execute store result score MOVE_X temp run data get entity @s data.motion_x 9000
execute store result score MOVE_Y temp run data get entity @s data.motion_y 9000
execute store result score MOVE_Z temp run data get entity @s data.motion_z 9000

# Check the direction to ricochet
execute if score POS_X temp matches 500 run scoreboard players operation MOVE_X temp *= NEG temp
execute if score POS_Y temp matches 500 run scoreboard players operation MOVE_Y temp *= NEG temp
execute if score POS_Z temp matches 500 run scoreboard players operation MOVE_Z temp *= NEG temp

execute if score POS_X temp matches 124 run scoreboard players operation MOVE_X temp *= NEG temp
execute if score POS_Y temp matches 124 run scoreboard players operation MOVE_Y temp *= NEG temp
execute if score POS_Z temp matches 124 run scoreboard players operation MOVE_Z temp *= NEG temp

# Apply the motion and unstick the arrow
execute store result entity @s Motion[0] double 0.0001 run scoreboard players get MOVE_X temp
execute store result entity @s Motion[1] double 0.0001 run scoreboard players get MOVE_Y temp
execute store result entity @s Motion[2] double 0.0001 run scoreboard players get MOVE_Z temp
data modify entity @s inGround set value 0b

function event_rebalance:enchantments/ricochet/store_motion
playsound minecraft:enchant.ricochet ambient @a ~ ~ ~

# Decrease our ricochet counter
execute store result entity @s data.ricochets int 1 run data get entity @s data.ricochets 0.99
tag @s[nbt={data:{ricochets:0}}] remove ricochet_arrow