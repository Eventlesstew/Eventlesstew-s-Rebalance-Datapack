execute on owner if entity @s[type=#skeletons] run return fail
execute store result storage arrow_damage temp double 1 run data get entity @s damage

data modify entity @s damage set compute default float event_rebalance:entities/arrow/skeleton_mod