playsound block.respawn_anchor.deplete master @a ~ ~ ~
execute if block ~ ~ ~ respawn_anchor[charges=1] run setblock ~ ~ ~ respawn_anchor[charges=0]
execute if block ~ ~ ~ respawn_anchor[charges=2] run setblock ~ ~ ~ respawn_anchor[charges=1]
execute if block ~ ~ ~ respawn_anchor[charges=3] run setblock ~ ~ ~ respawn_anchor[charges=2]
execute if block ~ ~ ~ respawn_anchor[charges=4] run setblock ~ ~ ~ respawn_anchor[charges=3]