# Set the cooldown
scoreboard players set @s timer 10

# Consume the arrow from the player's inventory and check if it is there.
execute store success score crossbow_result temp run clear @s arrow 1
execute if score crossbow_result temp = 0 static run function ranged_weapons:auto_crossbow_fail
execute if score crossbow_result temp = 0 static run return 0

# Apply 1 damage to the item in the main hand
item modify entity @s weapon.mainhand ranged_weapons:auto_crossbow_damage

# Play the sound
playsound block.dispenser.launch player @s ~ ~ ~ 1.0 1.2

# Summon the armor stand.
execute at @s anchored eyes run summon armor_stand ^ ^ ^2 {Tags:["launched_velocity"],NoGravity:true}

# Store armor stand position
execute store result score MOTION_X temp run data get entity @n[type=armor_stand,tag=launched_velocity] Pos[0] 10000
execute store result score MOTION_Y temp run data get entity @n[type=armor_stand,tag=launched_velocity] Pos[1] 10000
execute store result score MOTION_Z temp run data get entity @n[type=armor_stand,tag=launched_velocity] Pos[2] 10000

# Store player position
execute store result score POS_X temp run data get entity @s Pos[0] 10000
execute store result score POS_Y temp run data get entity @s Pos[1] 10000
execute store result score POS_Z temp run data get entity @s Pos[2] 10000

# Store player momentum
execute store result score PLAYER_MOTION_X temp run data get entity @s Motion[0] 10000
execute store result score PLAYER_MOTION_Y temp run data get entity @s Motion[1] 10000
execute store result score PLAYER_MOTION_Z temp run data get entity @s Motion[2] 10000

# Store player rotation
execute store result score PLAYER_ROTATION_YAW temp run data get entity @s Rotation[0] 10000
execute store result score PLAYER_ROTATION_PITCH temp run data get entity @s Rotation[1] 10000

# Flip rotation because apparently arrows are rotated oppositely from what I can tell.
scoreboard players operation PLAYER_ROTATION_YAW temp += 180_arrow static
scoreboard players operation PLAYER_ROTATION_PITCH temp += 180_arrow static

# Subtract Motion by Position
scoreboard players operation MOTION_X temp -= POS_X temp
scoreboard players operation MOTION_Y temp -= POS_Y temp
scoreboard players operation MOTION_Z temp -= POS_Z temp

# Add Motion by Player Motion
scoreboard players operation MOTION_X temp += PLAYER_MOTION_X temp
scoreboard players operation MOTION_Y temp += PLAYER_MOTION_Y temp
scoreboard players operation MOTION_Z temp += PLAYER_MOTION_Z temp

# Remove the fucking annoying offset in the Y motion
scoreboard players operation MOTION_Y temp -= armor_stand_eye_height static

# Summon the arrow.
execute rotated as @s at @s anchored eyes run summon arrow ^ ^ ^1 {Tags:["launched"]}

# Set arrow rotation
execute store result entity @n[type=arrow,tag=launched] Rotation[0] double 0.0001 run scoreboard players get PLAYER_ROTATION_YAW temp
execute store result entity @n[type=arrow,tag=launched] Rotation[0] double 0.0001 run scoreboard players get PLAYER_ROTATION_PITCH temp

# Set arrow motion
execute store result entity @n[type=arrow,tag=launched] Motion[0] double 0.0001 run scoreboard players get MOTION_X temp
execute store result entity @n[type=arrow,tag=launched] Motion[1] double 0.0001 run scoreboard players get MOTION_Y temp
execute store result entity @n[type=arrow,tag=launched] Motion[2] double 0.0001 run scoreboard players get MOTION_Z temp

# Kill armor stand and remove tags.
execute as @e[type=armor_stand,tag=launched_velocity] run kill
execute as @e[type=armor_stand,tag=launched_velocity] run tag @s remove launched_velocity
execute as @e[type=arrow,tag=launched] run tag @s remove launched