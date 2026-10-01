summon marker ^ ^ ^1 {Tags:[balance.hammer_area]}
tag @s add balance.hammer_attacker
execute store result entity @n[type=marker,tag=balance.hammer_area] data.damage double 1 run attribute @s attack_damage get 1
function event_rebalance:items/hammer/damage with entity @n[type=marker,tag=balance.hammer_area] data
kill @e[type=marker,tag=balance.hammer_area]
tag @s remove balance.hammer_attacker
playsound item.hammer.swing master @a ^ ^ ^1
advancement revoke @s only event_rebalance:function/hammer_attack