# Checks to make sure the player hasn't exited the Minecart
execute unless entity @s[predicate=event_rebalance:item/minecart/riding] run tag @s remove event.advancement.on_a_rail
execute unless entity @s[tag=event.advancement.on_a_rail] run return fail

execute store result storage event_rebalance:advancement on_a_rail.current.x int 1 run data get entity @s Pos[0] 1
execute store result storage event_rebalance:advancement on_a_rail.current.y int 1 run data get entity @s Pos[1] 1
execute store result storage event_rebalance:advancement on_a_rail.current.z int 1 run data get entity @s Pos[2] 1
execute store result storage event_rebalance:advancement on_a_rail.starting.x int 1 run scoreboard players get @s on_a_rail.start.x
execute store result storage event_rebalance:advancement on_a_rail.starting.y int 1 run scoreboard players get @s on_a_rail.start.y
execute store result storage event_rebalance:advancement on_a_rail.starting.z int 1 run scoreboard players get @s on_a_rail.start.z

# If the player has moved far enough in one of the directions, they get the advancement
execute store result score @s on_a_rail.start.dist run compute default float event_rebalance:advancement/on_a_rail/distance 1
execute if score @s on_a_rail.start.dist >= 500 static run advancement grant @s only event_rebalance:construction/on_a_rail
