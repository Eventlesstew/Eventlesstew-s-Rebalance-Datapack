execute as @a[scores={time_since_death=1}] at @s run function event_enchants:on_respawn
scoreboard players reset * time_since_death