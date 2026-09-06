#gamerule keep_inventory true

# Add scoreboards if they don't exist
scoreboard objectives add event.player_deaths deathCount
scoreboard objectives add temp dummy
scoreboard objectives add timer dummy
scoreboard objectives add static dummy

# Add values if they don't exist
scoreboard players add armor_stand_eye_height static 0
scoreboard players add 0 static 0
scoreboard players add 1 static 0
scoreboard players add 180_arrow static 0

# Set values
scoreboard players set armor_stand_eye_height static 15415
scoreboard players set 0 static 0
scoreboard players set 1 static 1
scoreboard players set 180_arrow static 1800000