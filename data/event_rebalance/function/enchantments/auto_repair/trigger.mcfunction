advancement revoke @s only event_rebalance:function/enchantments/auto_repair

function event_rebalance:enchantments/auto_repair/repair {"slot":"armor.head"}
function event_rebalance:enchantments/auto_repair/repair {"slot":"armor.chest"}
function event_rebalance:enchantments/auto_repair/repair {"slot":"armor.legs"}
function event_rebalance:enchantments/auto_repair/repair {"slot":"armor.feet"}
function event_rebalance:enchantments/auto_repair/repair {"slot":"weapon.mainhand"}
function event_rebalance:enchantments/auto_repair/repair {"slot":"weapon.offhand"}

execute if score auto_repair_used temp >= 1 static run function event_rebalance:enchantments/auto_repair/sound