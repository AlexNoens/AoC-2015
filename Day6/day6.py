keywords = ["toggle ", "turn off ", "turn on "]

lights = [[0 for i in range(999)] for j in range(999)]


def load_input():
    f = open("Day6/lights.txt", "r")
    return f


def toggle(line):
    # toggle range
    sides = line.split(" through ")
    left_side = sides[0].split(",")
    right_side = sides[1].split(",")

    for x in range(int(left_side[0]), int(right_side[0])):
        for y in range(int(left_side[1]), int(right_side[1])):
            if lights[x][y] == 0:
                lights[x][y] = 1
            else:
                lights[x][y] = 0


def turn_off(line):
    # off range
    sides = line.split(" through ")
    left_side = sides[0].split(",")
    right_side = sides[1].split(",")

    for x in range(int(left_side[0]), int(right_side[0])):
        for y in range(int(left_side[1]), int(right_side[1])):
            lights[x][y] = 0


def turn_on(line):
    # on range
    sides = line.split(" through ")
    left_side = sides[0].split(",")
    right_side = sides[1].split(",")

    for x in range(int(left_side[0]), int(right_side[0])):
        for y in range(int(left_side[1]), int(right_side[1])):
            lights[x][y] = 1


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
    count = 0
    calculate_fire_hazard(f)

    for x in range(0,999):
        for y in range(0,999):
            if lights[x][y] == 1:
                count += 1
    print(count)


if __name__ == "__main__":
    fire_hazard()
