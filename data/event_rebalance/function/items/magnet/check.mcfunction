function event_rebalance:items/magnet/apply {magnet_power:10}
function event_rebalance:items/magnet/modifier_remove
scoreboard players set @s balance.magnet_pull_time 0
function event_rebalance:items/magnet/pull/forward {distance:0}
execute as @s unless score @s balance.magnet_sound matches 0.. run tag @s add balance.magnet_sound
execute as @s unless score @s balance.magnet_pull_sound matches 0.. run tag @s add balance.magnet_pull_sound
execute as @s[tag=!balance.magnet_pull_detect] unless score @s balance.magnet_sound matches 0.. run scoreboard players set @s balance.magnet_sound 12
execute as @s[tag=balance.magnet_pull_detect] unless score @s balance.magnet_pull_sound matches 0.. run scoreboard players set @s balance.magnet_pull_sound 8
execute if entity @s[tag=balance.magnet_sound] run function event_rebalance:items/magnet/sound/check_all
execute if entity @s[tag=balance.magnet_pull_sound] run function event_rebalance:items/magnet/sound/check_all_pull
execute as @s[tag=balance.magnet_pull_detect,advancements={event_rebalance:construction/magnet_up=false}] run advancement grant @s only event_rebalance:construction/magnet_up
execute as @s[tag=balance.magnet_pull_detect,advancements={event_rebalance:construction/magnet_netherite=false}] run function event_rebalance:items/magnet/pull/ancient_debris_check {distance:0}
tag @s[tag=balance.magnet_pull_detect] remove balance.magnet_pull_detect
tag @s[tag=!balance.magnet_holder] add balance.magnet_holder
advancement revoke @s only event_rebalance:function/use_magnet