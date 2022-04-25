import re

def load_input(file):
    f = open(file, "r")
    return f.readlines()

def load_in(file):
    strip_pattern = re.compile(r"^Sue (\d+): (\w*): (\d+), (\w*): (\d+), (\w*): (\d+)")
    list = []
    for each in load_input(file):
        iterator = re.finditer(strip_pattern, each)
        this_sue = {}
        for match in iterator:
            this_sue["Sue_num"] = match.group(1)
            this_sue[match.group(2)] = int(match.group(3))
            this_sue[match.group(4)] = int(match.group(5))
            this_sue[match.group(6)] = int(match.group(7))
        list.append(this_sue)
    return list

input = {"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}

def solve_pt1(list, input):
    for each in input:
        remove = []
        for sue in list:
            try:
                if sue[each] != input[each]:
                    remove.append(sue)
            except:
                pass
        for each in remove:
            list.remove(each)
    return list

def solve_pt2(list, input):
    for each in input:
        remove = []
        for sue in list:
            try:
                if each == "cats" or each == "trees":
                    if sue[each] <= input[each]:
                        remove.append(sue)
                elif each == "pomeranians" or each == "goldfish":
                    if sue[each] >= input[each]:
                        remove.append(sue)
                elif sue[each] != input[each]:
                        remove.append(sue)
            except:
                pass
        for each in remove:
            list.remove(each)
    return list

list = load_in("Day16/input.txt")
print("Part 1:",solve_pt1(list,input))
list = load_in("Day16/input.txt")
print("Part 2:",solve_pt2(list,input))
