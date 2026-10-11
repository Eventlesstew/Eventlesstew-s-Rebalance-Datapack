tag @s add event.used_crystal_heart
schedule function event_rebalance:items/crystal_heart/revoke_advancement 10 append

execute if score @s extra_hearts >= max_extra_hearts static run return fail
scoreboard players add @s extra_hearts 1
function event_rebalance:items/crystal_heart/update
effect give @s regeneration 1 3 true
playsound block.enchantment_table.use player @a ~ ~ ~
clear @s *[minecraft:item_model="event:crystal_heart"] 1