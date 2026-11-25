execute unless entity @s[nbt={active_effects:[{id:"minecraft:darkness"}]}] run playsound entity.creaking.darkness ambient @s ~ ~ ~ 1 1
effect give @s darkness 10 0
advancement revoke @s only event_rebalance:function/entities/creaking_attack