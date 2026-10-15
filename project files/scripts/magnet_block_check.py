temp = "function event_rebalance:items/magnet/check_block {x:X,y:Y,z:Z}"

radius = 5

mcfunction = ""


def add_block(x, y, z):
    command = temp
    command = command.replace("X", str(x))
    command = command.replace("Y", str(y))
    command = command.replace("Z", str(z))
    command += "\n"

    return command


for i in range(0, 5):
    i += 1
    print(i + 1)
    mcfunction += add_block(0, 0, i)
    mcfunction += add_block(i, 0, 0)
    mcfunction += add_block(0, 0, -i)
    mcfunction += add_block(-i, 0, 0)
print(temp)

with open(
    "data/event_rebalance/function/items/magnet/find_block.mcfunction", "w"
) as file:
    file.write(mcfunction)
