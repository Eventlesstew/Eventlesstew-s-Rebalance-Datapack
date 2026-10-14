execute at @s anchored eyes run summon item_display ^ ^ ^ {item_display:"ground", item:{id:music_disc_13,components:{item_model:"event:wildfire/head"}},Tags:["event.wildfire.head"]}

attribute @s max_health modifier add event_rebalance 180 add_value
attribute @s scale base set 2

data modify entity @s Silent set value true
effect give @s invisibility infinite 2 true 