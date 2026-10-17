execute as @s[tag=!ricochet_arrow,tag=!balance.fuse] run particle minecraft:poof ~ ~ ~
execute as @s[tag=!ricochet_arrow,tag=!balance.fuse] run playsound minecraft:enchant.common.destroy ambient @a ~ ~ ~
execute as @s[tag=!ricochet_arrow,tag=!balance.fuse] run kill @s[type=#arrows]