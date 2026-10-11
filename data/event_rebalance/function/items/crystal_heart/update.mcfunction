execute if score @s extra_hearts > max_extra_hearts static store result score @s extra_hearts run scoreboard players get max_extra_hearts static
execute if score @s extra_hearts < 0 static store result score @s extra_hearts run scoreboard players get 0 static

attribute @s max_health modifier remove event.extra_hearts
execute if score @s extra_hearts = 1 static run attribute @s max_health modifier add event.extra_hearts 2 add_value
execute if score @s extra_hearts = 2 static run attribute @s max_health modifier add event.extra_hearts 4 add_value
execute if score @s extra_hearts = 3 static run attribute @s max_health modifier add event.extra_hearts 6 add_value
execute if score @s extra_hearts = 4 static run attribute @s max_health modifier add event.extra_hearts 8 add_value
execute if score @s extra_hearts = 5 static run attribute @s max_health modifier add event.extra_hearts 10 add_value
execute if score @s extra_hearts = 6 static run attribute @s max_health modifier add event.extra_hearts 12 add_value
execute if score @s extra_hearts = 7 static run attribute @s max_health modifier add event.extra_hearts 14 add_value
execute if score @s extra_hearts = 8 static run attribute @s max_health modifier add event.extra_hearts 16 add_value
execute if score @s extra_hearts = 9 static run attribute @s max_health modifier add event.extra_hearts 18 add_value
execute if score @s extra_hearts = 10 static run attribute @s max_health modifier add event.extra_hearts 20 add_value