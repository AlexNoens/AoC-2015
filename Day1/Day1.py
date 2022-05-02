from yaml import load


def load_input(file):
    f = open(file, "r")
    instructions = []
    for each in f.readlines():
        for bracket in each:
            instructions.append(bracket)
    return instructions


steps = load_input("Day1/input.txt")

tracker = 0
first = True

for i in range(0, len(steps)):
    if steps[i] == "(":
        tracker += 1
    elif steps[i] == ")":
        tracker -= 1
    elif steps[i] == "\n":
        break
    else:
        print("wtf")
        break
    if tracker < 0 and first:
        first = False
        print("First trip to the basement at position:", i + 1)


print("Sants finally ends up on floor:", tracker)
