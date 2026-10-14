execute if entity @n[type=illusioner,distance=..32] run tag @s add illusioner_bossbar
execute unless entity @n[type=illusioner,distance=..32] run tag @s remove illusioner_bossbar

execute if entity @n[type=blaze,tag=wildfire,distance=..32] run tag @s add wildfire_bossbar
execute unless entity @n[type=blaze,tag=wildfire,distance=..32] run tag @s remove wildfire_bossbar