execute if entity @s[tag=event.magnet_marker_active] run return fail
$execute at @s unless block ~$(x) ~$(y) ~$(z) #event_rebalance:magnetic run return fail
$tp @s ~$(x) ~$(y) ~$(z)
$say X:$(x), Y:$(y), Z:$(z)
tag @s add event.magnet_marker_active