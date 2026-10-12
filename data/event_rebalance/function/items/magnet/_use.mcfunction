advancement revoke @s only event_rebalance:function/use_magnet
attribute @s gravity modifier remove event.magnet

tag @s add event.magnet_user
summon marker ~ ~ ~ {Tags:["event.magnet_marker"]}

execute as @n[tag=event.magnet_marker] run function event_rebalance:items/magnet/find_block
kill @e[type=marker,tag=event.magnet_marker]

execute as @e[type=marker,tag=event.magnet_pull_marker] run function event_rebalance:items/magnet/pull_user
tag @s remove event.magnet_user
kill @e[type=marker,tag=event.magnet_pull_marker]