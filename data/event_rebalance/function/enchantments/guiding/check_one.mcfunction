execute unless entity @s[tag=guide_init] run function event_rebalance:enchantments/guiding/init

# If we're in the ground for 1 tick, ignore functionality (for ricochet compat)
# If we're in the ground for 2 ticks, remove tag
execute if entity @s[nbt={life:2s}] run kill @n[tag=guiding_marker]
execute if entity @s[nbt={life:2s}] run return run tag @s remove guide_arrow
execute if entity @s[nbt={inGround:1b}] run return 0
execute unless entity @s[nbt={LeftOwner:1b}] run return run function event_rebalance:enchantments/guiding/store_pos

scoreboard players set SCALE temp 0

function event_rebalance:enchantments/guiding/fix_angle with entity @s data
function event_rebalance:enchantments/guiding/store_pos

execute store result score CURRENT_YAW temp run data get entity @n[tag=guiding_marker] Rotation[0]
execute on origin if entity @s[type=player] store result score TARGET_YAW temp run data get entity @s Rotation[0]
execute on origin unless entity @s[type=player] on origin store result score TARGET_YAW temp run data get entity @s Rotation[0]

function event_rebalance:enchantments/common/calculate_yaw
function event_rebalance:enchantments/common/adjust_yaw

execute store result score CURRENT_PITCH temp run data get entity @n[tag=guiding_marker] Rotation[1]
execute on origin store result score TARGET_PITCH temp run data get entity @s Rotation[1]

function event_rebalance:enchantments/common/calculate_pitch
function event_rebalance:enchantments/common/adjust_pitch
