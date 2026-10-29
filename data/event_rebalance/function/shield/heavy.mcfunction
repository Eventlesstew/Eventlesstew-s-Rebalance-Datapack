attribute @s knockback_resistance modifier add heavy_shield 0.75 add_value
attribute @s explosion_knockback_resistance modifier add heavy_shield 0.75 add_value
advancement revoke @s only event_rebalance:heavy_shield
schedule function event_rebalance:shield/heavy_reset 2t