def load_input(file):
    f = open(file, "r")
    boxes = []
    for each in f.readlines():
        sides = each.strip().split("x")
        boxes.append([int(sides[0]), int(sides[1]), int(sides[2])])
    return boxes


boxes = load_input("Day2/input.txt")

paper = 0
ribbon = 0

for each in boxes:
    each.sort()
    print(each)
    area_of_side_1 = each[0] * each[1]
    area_of_side_2 = each[1] * each[2]
    area_of_side_3 = each[0] * each[2]
    slack = min(area_of_side_1, area_of_side_2, area_of_side_3)
    paper += 2 * area_of_side_1 + 2 * area_of_side_2 + 2 * area_of_side_3 + slack
    ribbon += (2 * (each[0] + each[1])) + each[0] * each[1] * each[2]

print(
    "The elves need to odrder",
    paper,
    "square feet of wrapping paper",
    "and",
    ribbon,
    "feet of ribbon",
)
