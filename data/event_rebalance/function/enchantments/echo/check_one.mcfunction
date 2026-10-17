execute store result entity @s data.repeat_time int 1 run data get entity @s data.repeat_time 0.99
execute unless entity @s[nbt={data:{repeat_time:0}}] run return 0
data modify entity @s data.repeat_time set value 11

execute if entity @s[nbt={data:{repeat_count:0}}] run return run function event_rebalance:enchantments/echo/remove_bow
execute store result entity @s data.repeat_count int 1 run data get entity @s data.repeat_count 0.99

# Summon the new arrow
summon arrow ~ ~ ~ {Tags:["new_arrow"]}
data modify entity @n[tag=new_arrow] Pos set from entity @s data.Pos
data modify entity @n[tag=new_arrow] Motion set from entity @s data.Motion
data modify entity @n[tag=new_arrow] Rotation set from entity @s data.Rotation
data modify entity @n[tag=new_arrow] Owner set from entity @s data.Owner
data modify entity @n[tag=new_arrow] damage set from entity @s data.damage
data modify entity @n[tag=new_arrow] item set from entity @s data.item
data modify entity @n[tag=new_arrow] weapon set from entity @s data.weapon
data modify entity @n[tag=new_arrow] Fire set from entity @s data.Fire
data modify entity @n[tag=new_arrow] NoGravity set from entity @s data.NoGravity
data modify entity @n[tag=new_arrow] data set from entity @s data.data

# Add a bit of jitter and then reset the tags
execute as @n[tag=new_arrow] run function event_rebalance:enchantments/common/add_jitter_a
data modify entity @n[tag=new_arrow] Tags set from entity @s data.Tags