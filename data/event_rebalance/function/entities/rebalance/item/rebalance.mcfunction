data modify entity @s Age set value -30000

execute unless data entity @s Item.components."minecraft:custom_data".emit_particles run return fail
data remove entity @s Item.components."minecraft:custom_data".emit_particles
tag @s add event_rebalance.emitting_ender_eye_particles