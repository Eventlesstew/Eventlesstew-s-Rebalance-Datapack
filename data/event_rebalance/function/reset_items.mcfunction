scoreboard players reset @a event.reset_items
scoreboard players enable @a event.reset_items

execute as @a run item modify entity @s event_rebalance:all event_rebalance:reset_item
execute as @a run function event_rebalance:apply_rebalance