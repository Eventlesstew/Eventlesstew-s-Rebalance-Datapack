execute if score @s event_rebalance.acceleration_count matches 20..40 run playsound enchant.acceleration.stop.soft master @a
execute if score @s event_rebalance.acceleration_count matches 41..80 run playsound enchant.acceleration.stop.medium master @a
execute if score @s event_rebalance.acceleration_count matches 81.. run playsound enchant.acceleration.stop.hard master @a
scoreboard players reset @s event_rebalance.acceleration_count
attribute @s movement_speed modifier remove balance.acceleration
tag @s remove balance.acceleration