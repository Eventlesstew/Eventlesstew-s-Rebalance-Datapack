execute as @a run execute if score @s timer > 0 static run function ranged_weapons:timer_tick
execute as @a run execute if score @s timer <= 0 static run function ranged_weapons:timer_timeout