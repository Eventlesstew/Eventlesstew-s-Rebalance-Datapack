execute if entity @s[tag=balance.borer,predicate=event_rebalance:enchant/felling/check] run playsound enchant.felling.deactivate master @a ~ ~ ~ 0.3 0.7
attribute @s block_interaction_range modifier remove balance.borer_increase
#attribute @s mining_efficiency modifier remove balance.borer_increase
#attribute @s gravity modifier remove balance.borer_increase
tag @s remove balance.borer