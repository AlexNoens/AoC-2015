from PIL import Image
import numpy as np

keywords = ["toggle ", "turn off ", "turn on "]

lights = [[0 for i in range(1000)] for j in range(1000)]


def load_input():
    f = open("Day6/fernie.txt", "r")
    return f


def split_content(line):
    sides = line.split(" through ")
    lhs = sides[0].split(",")
    rhs = sides[1].split(",")

    return int(lhs[0]), int(lhs[1]), int(rhs[0]), int(rhs[1])


def toggle(line):
    x1, y1, x2, y2 = split_content(line)

    x = x1
    y = y1

    while x <= x2:
        while y <= y2:
            lights[x][y] += 2
            # if lights[x][y] == 0:
            # lights[x][y] = 1
            # else:
            # lights[x][y] = 0

            y += 1

        y = y1
        x += 1


def turn_off(line):
    x1, y1, x2, y2 = split_content(line)

    x = x1
    y = y1

    while x <= x2:
        while y <= y2:
            if lights[x][y] > 0:
                lights[x][y] -= 1

            y += 1

        y = y1
        x += 1


def turn_on(line):
    x1, y1, x2, y2 = split_content(line)

    x = x1
    y = y1

    while x <= x2:
        while y <= y2:
            lights[x][y] += 1
            y += 1

        y = y1
        x += 1

    # print(lights)


def parse_command(line):
    if keywords[0] in line:
        toggle(line.split(keywords[0])[1])
    elif keywords[1] in line:
        turn_off(line.split(keywords[1])[1])
    elif keywords[2] in line:
        turn_on(line.split(keywords[2])[1])
    else:
        print("help")


def calculate_fire_hazard(file):

    lines = file.readlines()

    for line in lines:
        parse_command(line)


def fire_hazard():
    f = load_input()

    calculate_fire_hazard(f)

    # print(lights[0].count(1), lights[1].count(1))
    count = 0
    for x in range(len(lights[0])):
        for y in range(len(lights[1])):
            lights[x][y] *= 5
            if lights[x][y] == 1:
                count += 1
    print(count)
    l_arr = np.asarray(lights)
    img = Image.fromarray(l_arr, "L")
    img.save("Day6/my.png")
    img.show()


if __name__ == "__main__":
    fire_hazard()
