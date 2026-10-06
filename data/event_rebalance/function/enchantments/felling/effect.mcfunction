#attribute @s mining_efficiency modifier remove balance.borer_increase
attribute @s block_interaction_range modifier remove balance.borer_increase
#attribute @s gravity modifier remove balance.borer_increase
#$attribute @s mining_efficiency modifier add balance.borer_increase $(mining_speed) add_value
$attribute @s block_interaction_range modifier add balance.borer_increase $(block_range) add_value
#attribute @s gravity modifier add balance.borer_increase 5 add_multiplied_base