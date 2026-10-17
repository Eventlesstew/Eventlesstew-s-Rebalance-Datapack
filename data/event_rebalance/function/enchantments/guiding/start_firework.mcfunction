tag @e[type=firework_rocket,distance=..2] add guide_arrow
execute if entity @e[type=firework_rocket,distance=..2] run schedule function event_rebalance:enchantments/guiding/check_all 1t append
advancement revoke @s only event_rebalance:function/enchantments/guiding_firework