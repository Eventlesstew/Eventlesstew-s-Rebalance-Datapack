$ execute if items entity @s $(inventory_slot) *[event_rebalance:item/has_durability] run item modify entity @s $(inventory_slot) event_rebalance:function/death_damage
$ execute if items entity @s $(inventory_slot) *[event_rebalance:item/has_durability] run return fail

