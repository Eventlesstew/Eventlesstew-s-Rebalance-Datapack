advancement revoke @s only event_rebalance:function/interact_with_minecart
tag @s add event.advancement.on_a_rail

execute store result score @s on_a_rail.start.x run data get entity @s Pos.[0]
execute store result score @s on_a_rail.start.y run data get entity @s Pos.[1]
execute store result score @s on_a_rail.start.z run data get entity @s Pos.[2]