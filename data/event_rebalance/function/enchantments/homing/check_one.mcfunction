# If we're in the ground for 1 tick, ignore functionality (for ricochet compat)
# If we're in the ground for 2 ticks, remove tag
execute if entity @s[nbt={life:2s}] run kill @n[tag=homing_marker]
execute if entity @s[nbt={life:2s}] run return run tag @s remove homing_arrow
execute if entity @s[nbt={inGround:1b}] run return 0
execute unless entity @s[nbt={LeftOwner:1b}] run return 0

function event_rebalance:enchantments/homing/fix_angle with entity @s data
data modify entity @s data.old_x set from entity @s Pos[0]
data modify entity @s data.old_y set from entity @s Pos[1]
data modify entity @s data.old_z set from entity @s Pos[2]

#Home
$execute as @s unless entity @n[tag=homing_target] rotated as @n[tag=homing_marker] positioned ^ ^ ^1 run tag @n[type=#mobs,distance=..$(homing_distance_1)] add homing_target
$execute as @s unless entity @n[tag=homing_target] rotated as @n[tag=homing_marker] positioned ^ ^ ^2 run tag @n[type=#mobs,distance=..$(homing_distance_2)] add homing_target
$execute as @s unless entity @n[tag=homing_target] rotated as @n[tag=homing_marker] positioned ^ ^ ^3 run tag @n[type=#mobs,distance=..$(homing_distance_3)] add homing_target
$execute as @s unless entity @n[tag=homing_target] rotated as @n[tag=homing_marker] positioned ^ ^ ^4 run tag @n[type=#mobs,distance=..$(homing_distance_4)] add homing_target
$execute as @s unless entity @n[tag=homing_target] rotated as @n[tag=homing_marker] positioned ^ ^ ^5 run tag @n[type=#mobs,distance=..$(homing_distance_5)] add homing_target


execute unless entity @n[tag=homing_target] run return 0

# Get offset
execute store result score CURRENT_YAW temp run data get entity @n[tag=homing_marker] Rotation[0]
execute store result score CURRENT_PITCH temp run data get entity @n[tag=homing_marker] Rotation[1]
execute facing entity @n[tag=homing_target] eyes run rotate @n[tag=homing_marker] ~ ~
execute store result score TARGET_YAW temp run data get entity @n[tag=homing_marker] Rotation[0]
execute store result score TARGET_PITCH temp run data get entity @n[tag=homing_marker] Rotation[1]
scoreboard players remove TARGET_PITCH temp 0

function event_rebalance:enchantments/common/calculate_yaw
scoreboard players operation OFFSET_YAW temp += OFFSET_YAW temp
function event_rebalance:enchantments/common/adjust_yaw

scoreboard players operation OFFSET_PITCH temp = CURRENT_PITCH temp
scoreboard players operation OFFSET_PITCH temp -= TARGET_PITCH temp
function event_rebalance:enchantments/common/adjust_pitch

tag @n[tag=homing_target] remove homing_target