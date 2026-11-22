execute store result score COUNT_A temp run data get storage balance.hammer_attack squeeze_count
execute if score COUNT_A temp matches 2..4 run playsound enchant.squeeze.soft ambient @a ~ ~ ~ 0.5 1.3
execute if score COUNT_A temp matches 5..9 run playsound enchant.squeeze.soft ambient @a ~ ~ ~ 1 1
execute if score COUNT_A temp matches 10.. run playsound enchant.squeeze.hard ambient @a ~ ~ ~ 1 1