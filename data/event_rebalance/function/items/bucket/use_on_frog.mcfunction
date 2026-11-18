advancement revoke @s only event_rebalance:function/items/use_bucket_on_frog

# Store the frog data
data modify storage event_rebalance:bucket_data frog set from entity @n[type=frog,nbt={equipment:{body:{id:"minecraft:bucket"}}}]
data modify storage event_rebalance:bucket_data frog.id set value "frog"
data remove storage event_rebalance:bucket_data frog.equipment.body
data remove storage event_rebalance:bucket_data frog.Pos
data remove storage event_rebalance:bucket_data frog.Rotation
data remove storage event_rebalance:bucket_data frog.UUID

# Kill the frog
execute as @n[type=frog,nbt={equipment:{body:{id:"minecraft:bucket"}}}] run tp ~ ~-10000 ~

# Spawn the item
execute anchored eyes run summon item ^ ^ ^ {Tags:["event.bucket_item"],Item:{id:"frog_spawn_egg"}}
data modify entity @n[tag=event.bucket_item] Item.components."minecraft:entity_data" set from storage event_rebalance:bucket_data frog
data modify entity @n[tag=event.bucket_item] Item.components."minecraft:custom_model_data".strings append from storage event_rebalance:bucket_data frog.variant

# Momentum
summon marker ^ ^ ^10 {Tags:[fireball]}
#tp @n[tag=fireball] ~ ~4.14 ~

execute store result storage event_rebalance:fireball origin_x float 1 run data get entity @s Pos[0]
execute store result storage event_rebalance:fireball origin_y float 1 run data get entity @s Pos[1]
execute store result storage event_rebalance:fireball origin_z float 1 run data get entity @s Pos[2]
execute store result storage event_rebalance:fireball shoot_x float 1 run data get entity @n[tag=fireball] Pos[0]
execute store result storage event_rebalance:fireball shoot_y float 1 run data get entity @n[tag=fireball] Pos[1]
execute store result storage event_rebalance:fireball shoot_z float 1 run data get entity @n[tag=fireball] Pos[2]

kill @n[type=marker,tag=fireball]

execute store result entity @n[tag=event.bucket_item] Motion[0] float 0.04 run compute default float event_rebalance:items/motion/x 1
execute store result entity @n[tag=event.bucket_item] Motion[1] float 0.04 run compute default float event_rebalance:items/motion/y 1
execute store result entity @n[tag=event.bucket_item] Motion[2] float 0.04 run compute default float event_rebalance:items/motion/z 1