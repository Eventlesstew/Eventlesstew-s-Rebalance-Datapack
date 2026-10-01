execute unless predicate event_rebalance:has_totem_of_warping run return fail
damage @s 100
advancement revoke @s only event_rebalance:function/totem_of_warping_void
advancement grant @s only event_rebalance:end/use_totem_of_warping_in_end