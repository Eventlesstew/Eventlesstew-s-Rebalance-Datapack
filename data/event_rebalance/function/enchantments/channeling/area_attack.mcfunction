execute at @s unless predicate event_rebalance:mobs/in_water run return fail
execute store result score channeling temp run data get entity @s DealtDamage
execute if score channeling temp = 1 static run return fail

# Attack damaging the owner isn't intentional.
execute on owner run tag @s add event.channeling_owner
execute store result entity @s data.damage int 1 run data get entity @s item.components."minecraft:enchantments"."minecraft:channeling" 4
function event_rebalance:enchantments/channeling/damage with entity @s data
execute on owner run tag @s remove event.channeling_owner

playsound item.trident.thunder master @a ~ ~ ~
particle flash{color:-1} ~ ~ ~ 0.2 0.2 0.2 0 20
particle minecraft:firework ~ ~ ~ 0 0 0 1 50