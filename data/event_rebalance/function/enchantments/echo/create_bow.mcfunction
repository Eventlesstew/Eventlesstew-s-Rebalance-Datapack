summon item_display ~ ~ ~ {item:{id:"minecraft:bow",components:{"minecraft:enchantment_glint_override":true}},item_display:"thirdperson_righthand",Tags:["echo_item","new_item"]}
data modify entity @n[tag=new_item] item.id set from entity @s weapon.id

data modify entity @n[tag=new_item] Pos set from entity @s data.bow_pos
data modify entity @n[tag=new_item] Rotation set from entity @s data.bow_rot

data remove entity @s data.bow_pos
data remove entity @s data.bow_rot

# Copy arrow data to the bow
tag @s remove echo_arrow
tag @s add spawned_arrow

tag @s[tag=warping_arrow] add warping_suppressed
tag @s[tag=warping_arrow] remove warping_arrow

data modify entity @n[tag=new_item] data.Owner set from entity @s data.Owner
data remove entity @s data.Owner

data modify entity @n[tag=new_item] data.Pos set from entity @s Pos
data modify entity @n[tag=new_item] data.Motion set from entity @s Motion
data modify entity @n[tag=new_item] data.Rotation set from entity @s Rotation
data modify entity @n[tag=new_item] data.damage set from entity @s damage
data modify entity @n[tag=new_item] data.item set from entity @s item
data modify entity @n[tag=new_item] data.weapon set from entity @s weapon
data modify entity @n[tag=new_item] data.Fire set from entity @s Fire
data modify entity @n[tag=new_item] data.NoGravity set from entity @s NoGravity
data modify entity @n[tag=new_item] data.Tags set from entity @s Tags

data modify entity @n[tag=new_item] data.data set from entity @s data
data modify entity @n[tag=new_item] data.repeat_count set from entity @s weapon.components."minecraft:enchantments"."event_rebalance:echo"
data modify entity @n[tag=new_item] data.repeat_time set value 11

tag @s[tag=warping_suppressed] add warping_arrow
tag @s[tag=warping_suppressed] remove warping_suppressed

tag @n[tag=new_item] remove new_item