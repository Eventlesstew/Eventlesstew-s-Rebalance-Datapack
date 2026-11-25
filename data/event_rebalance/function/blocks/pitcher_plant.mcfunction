execute unless entity @s[nbt={active_effects:[{id:"minecraft:glowing"}]}] run playsound block.pitcher_plant.night_vision ambient @s ~ ~ ~ 1 1
effect give @s night_vision 10 2
advancement revoke @s only event_rebalance:function/blocks/pitcher_plant