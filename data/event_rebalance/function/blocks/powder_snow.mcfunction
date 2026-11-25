#execute unless entity @s[nbt={active_effects:[{id:"minecraft:glowing"}]}] run playsound block.torchflower.glowing ambient @s ~ ~ ~ 1 1
effect give @s freezing 10 2
advancement revoke @s only event_rebalance:function/blocks/powder_snow