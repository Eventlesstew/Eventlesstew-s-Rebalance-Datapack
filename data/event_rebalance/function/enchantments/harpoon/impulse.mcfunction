data modify storage event_rebalance:harpoon SELF_X set from entity @s Pos[0]
data modify storage event_rebalance:harpoon SELF_Y set from entity @s Pos[1]
data modify storage event_rebalance:harpoon SELF_Z set from entity @s Pos[2]

data modify storage event_rebalance:harpoon SELF_MOTION_X set from entity @s Motion[0]
data modify storage event_rebalance:harpoon SELF_MOTION_Y set from entity @s Motion[1]
data modify storage event_rebalance:harpoon SELF_MOTION_Z set from entity @s Motion[2]

data modify entity @s Motion[0] set compute default float event_rebalance:harpoon_x
data modify entity @s Motion[1] set compute default float event_rebalance:harpoon_y
data modify entity @s Motion[2] set compute default float event_rebalance:harpoon_z

playsound enchant.harpoon player @a ~ ~ ~