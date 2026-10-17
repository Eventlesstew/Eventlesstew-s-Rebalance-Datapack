tag @s add echo_arrow

execute on origin run tag @s add echo_owner
data modify entity @s data.bow_rot set from entity @n[tag=echo_owner] Rotation
data modify entity @s data.bow_pos set from entity @s Pos
data modify entity @s data.Owner set from entity @s Owner
execute on origin run tag @s remove echo_owner

schedule function event_rebalance:enchantments/echo/check_all 1t append