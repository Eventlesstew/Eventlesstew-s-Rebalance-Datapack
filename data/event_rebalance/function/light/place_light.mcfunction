$execute unless predicate event_rebalance:light/level/$(level) run return fail
$fill ^ ^ ^ ^ ^ ^ light[level=$(level)] replace #air
$fill ^ ^ ^ ^ ^ ^ light[level=$(level),waterlogged=true] replace water[level=0]