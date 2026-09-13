execute if entity @s[tag=!focusing] run playsound enchant.focusing.activate ambient @a ~ ~ ~ 0.5 1
tag @s[tag=!focusing] add focusing
attribute @s mining_efficiency modifier add focusing4 16 add_value
attribute @s block_interaction_range modifier add focusing4 4 add_value

attribute @s mining_efficiency modifier remove focusing1
attribute @s block_interaction_range modifier remove focusing1
attribute @s mining_efficiency modifier remove focusing2
attribute @s block_interaction_range modifier remove focusing2
attribute @s mining_efficiency modifier remove focusing3
attribute @s block_interaction_range modifier remove focusing3
attribute @s mining_efficiency modifier remove focusing5
attribute @s block_interaction_range modifier remove focusing5