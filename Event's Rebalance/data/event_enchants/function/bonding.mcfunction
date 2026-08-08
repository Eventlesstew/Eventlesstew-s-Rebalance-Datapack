execute unless data entity @s Item.components."minecraft:enchantments"."event_enchants:bonding" run return fail
execute store result entity @s Pos[0] float 1 run scoreboard players get DEATH_X temp
execute store result entity @s Pos[1] float 1 run scoreboard players get DEATH_Y temp
execute store result entity @s Pos[2] float 1 run scoreboard players get DEATH_Z temp