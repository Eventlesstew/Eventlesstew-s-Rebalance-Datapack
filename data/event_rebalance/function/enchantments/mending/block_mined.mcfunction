execute as @p run tag @s add event.mending_repair
schedule function event_rebalance:enchantments/mending/remove_tag 2t append
kill