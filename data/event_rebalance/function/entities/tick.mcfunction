execute if entity @s[type=wolf] run function event_rebalance:entities/entities/wolf
execute if entity @s[type=husk] run function event_rebalance:entities/entities/husk
execute if entity @s[type=player] run function event_rebalance:entities/entities/player
execute if entity @s[type=spider] run function event_rebalance:entities/entities/spider
execute if entity @s[type=#event_rebalance:can_wear_animal_armor] run function event_rebalance:entities/entities/animal_armor

execute at @s if entity @s[tag=balance.borer] unless predicate event_rebalance:enchant/felling/check run function event_rebalance:enchantments/felling/deactivate