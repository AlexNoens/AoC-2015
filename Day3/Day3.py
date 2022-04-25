houses = [(0, 0)]

input = open("Day3/Part3input.txt", "r")
inputData = input.read()
input.close

x = 0
y = 0
x_rbt = 0
y_rbt = 0
turn = 0
for dir in inputData:
    if turn == 0:
        if dir == "^":
            print("up")
            y += 1
        elif dir == "v":
            print("down")
            y -= 1
        elif dir == ">":
            print("left")
            x += 1
        elif dir == "<":
            print("right")
            x -= 1
        coord = (x, y)
        turn = 1
    else:
        if dir == "^":
            y_rbt += 1
        elif dir == "v":
            y_rbt -= 1
        elif dir == ">":
            x_rbt += 1
        elif dir == "<":
            x_rbt -= 1
        coord = (x_rbt, y_rbt)
        turn = 0
    if coord in houses:
        continue
    else:
        houses.append(coord)

print(len(houses))
