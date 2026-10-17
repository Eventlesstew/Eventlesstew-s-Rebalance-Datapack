function event_rebalance:enchantments/guiding/store_pos
summon marker ~ ~ ~ {Tags:["new_marker","guiding_marker"]}
ride @n[tag=new_marker] mount @s
tag @n[tag=new_marker] remove new_marker
tag @s add guide_init