execute if entity @s[tag=!rebalanced] run function event_rebalance:entities/rebalance/apply_changes

execute if entity @s[type=arrow] run function event_rebalance:entities/rebalance/arrow/tick
execute if entity @s[type=player] run function event_rebalance:entities/rebalance/player/tick
execute if entity @s[type=#event_rebalance:rideable] run function event_rebalance:entities/rebalance/ridable/tick

execute if entity @s[type=wolf] run function event_rebalance:entities/rebalance/wolf/tick
execute if entity @s[type=turtle] run function event_rebalance:entities/rebalance/turtle/tick
execute if entity @s[type=#event_rebalance:can_wear_animal_armor] run function event_rebalance:entities/rebalance/animal_armor/tick

#execute if entity @s[type=husk] run function event_rebalance:entities/rebalance/husk/fire
execute if entity @s[type=spider] run function event_rebalance:entities/rebalance/spider/tick
execute if entity @s[type=illusioner] run function event_rebalance:entities/rebalance/illusioner/tick
execute if entity @s[type=blaze] run function event_rebalance:entities/rebalance/blaze/tick

execute at @s if entity @s[tag=balance.borer] unless predicate event_rebalance:enchant/felling/check run function event_rebalance:enchantments/felling/deactivate
execute if entity @s[tag=event_rebalance.emitting_light] at @s anchored eyes run function event_rebalance:light/clear