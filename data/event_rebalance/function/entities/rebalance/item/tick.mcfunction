function event_rebalance:entities/rebalance/item/emit_ender_eye_particle

execute unless items entity @s contents #event_rebalance:slow_falling run return fail

execute store result storage event_rebalance:temp item_fall_speed float 1 run data get entity @s Motion[1] 100
execute store result entity @s Motion[1] float 0.01 run compute default float event_rebalance:items/slow_fall 1