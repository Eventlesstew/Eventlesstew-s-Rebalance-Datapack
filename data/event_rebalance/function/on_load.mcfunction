#gamerule keep_inventory true

# Add scoreboards if they don't exist
scoreboard objectives add event.player_deaths deathCount
scoreboard objectives add temp dummy
scoreboard objectives add timer dummy
scoreboard objectives add static dummy
scoreboard objectives add event_rebalance.flat_damage_enchantment_cooldown dummy
scoreboard objectives add event_rebalance.acceleration_count dummy
scoreboard objectives add event_rebalance.combo_timer dummy
scoreboard objectives add event_rebalance.castaway_timer dummy
scoreboard objectives add extra_hearts dummy
scoreboard objectives add on_a_rail.start.x dummy
scoreboard objectives add on_a_rail.start.y dummy
scoreboard objectives add on_a_rail.start.z dummy
scoreboard objectives add on_a_rail.start.dist dummy

# Add values if they don't exist
scoreboard players add armor_stand_eye_height static 0
scoreboard players add -1575 static 0
scoreboard players add -1125 static 0
scoreboard players add -675 static 0
scoreboard players add -225 static 0
scoreboard players add 0 static 0
scoreboard players add 1 static 0
scoreboard players add 2 static 0
scoreboard players add 3 static 0
scoreboard players add 4 static 0
scoreboard players add 5 static 0
scoreboard players add 6 static 0
scoreboard players add 7 static 0
scoreboard players add 8 static 0
scoreboard players add 9 static 0
scoreboard players add 10 static 0
scoreboard players add 20 static 0
scoreboard players add 225 static 0
scoreboard players add 500 static 0
scoreboard players add 675 static 0
scoreboard players add 1000 static 0
scoreboard players add 1125 static 0
scoreboard players add 1575 static 0
scoreboard players add 180_arrow static 0
scoreboard players add max_extra_hearts static 0
execute as @a run scoreboard players add @s extra_hearts 0

# Set values
scoreboard players set armor_stand_eye_height static 15415
scoreboard players set -1575 static -1575
scoreboard players set -1125 static -1125
scoreboard players set -675 static -675
scoreboard players set -225 static -225
scoreboard players set 0 static 0
scoreboard players set 1 static 1
scoreboard players set 2 static 2
scoreboard players set 3 static 3
scoreboard players set 4 static 4
scoreboard players set 5 static 5
scoreboard players set 6 static 6
scoreboard players set 7 static 7
scoreboard players set 8 static 8
scoreboard players set 9 static 9
scoreboard players set 10 static 10
scoreboard players set 20 static 20
scoreboard players set 225 static 225
scoreboard players set 500 static 500
scoreboard players set 675 static 675
scoreboard players set 1000 static 1000
scoreboard players set 1125 static 1125
scoreboard players set 1575 static 1575
scoreboard players set max_extra_hearts static 10
scoreboard players set 180_arrow static 1800000

gamerule spawn_phantoms false
gamerule keep_inventory true
gamerule max_minecart_speed 1000

execute as @a run function event_rebalance:items/crystal_heart/update

bossbar add event_rebalance:illusioner {translate:entity.minecraft.illusioner}
bossbar set event_rebalance:illusioner color blue
bossbar add event_rebalance:wildfire {translate:entity.event.wildfire}
bossbar set event_rebalance:wildfire color yellow