tag @s add balance.hammer_attacker
function event_rebalance:items/hammer/enchantments/reset
function event_rebalance:items/hammer/sweep_radius_calculate
function event_rebalance:items/hammer/base_radius with storage balance.hammer_attack
function event_rebalance:items/hammer/sweep_calculate
execute if predicate event_rebalance:item/hammer/enchantment/sharpness run function event_rebalance:items/hammer/enchantments/sharpness
execute if predicate event_rebalance:item/hammer/enchantment/smite run function event_rebalance:items/hammer/enchantments/smite
data modify storage balance.hammer_attack enchanted_damage set compute default float event_rebalance:items/hammer/enchanted_damage
data modify storage balance.hammer_attack enchanted_undead_damage set compute default float event_rebalance:items/hammer/enchanted_undead_damage
function event_rebalance:items/hammer/damage with storage balance.hammer_attack
kill @e[type=marker,tag=balance.hammer_area]
tag @s remove balance.hammer_attacker
execute anchored eyes run particle sweep_attack ^ ^-0.5 ^1
playsound item.hammer.swing master @a ^ ^ ^1
advancement revoke @s only event_rebalance:function/items/hammer/attack