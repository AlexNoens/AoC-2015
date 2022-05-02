import re
from turtle import st

molecule_re = re.compile(r"[A-Z][a-z]*")


def load_input(file):
    f = open(file, "r")
    return f.readlines()


def parse(file):
    swaps = {}
    start_molecule = []
    for each in load_input(file):
        if "=>" in each:
            # print(each)
            line = each.split("=>")
            line[0] = line[0].strip()
            if line[0] in swaps.keys():
                swaps[line[0]].append(line[1].strip())
            else:
                swaps[line[0]] = [line[1].strip()]
        elif each != "\n":
            start_molecule = molecule_re.findall(each.strip())

    return start_molecule, swaps


def make_swap(start, idx, swaps, Moleculies):
    temp = start.copy()
    for thing in swaps[start[idx]]:
        temp[idx] = thing
        temp2 = "".join(temp)
        if temp2 not in Moleculies:
            Moleculies.append(temp2)
        temp = start.copy()
    return Moleculies


start, swaps = parse("Day19/input.txt")

Moleculies = []

# 1. iterate through Atoms in start
# 2. Check if Atom is a key
# 3. Make the swaps for that key's list, record all unique molecules
# 4. Profit

for i in range(0, len(start)):
    if start[i] in swaps.keys():
        Moleculies = make_swap(start, i, swaps, Moleculies)

print("Part 1:", len(Moleculies))

# print(start)

num_atoms = len(start)
num_y = 0
num_Rn = 0
num_Ar = 0

for each in start:
    if each == "Y":
        num_y += 1
    elif each == "Rn":
        num_Rn += 1
    elif each == "Ar":
        num_Ar += 1


# print(num_atoms, num_Ar, num_Rn, num_y)
print("Part 2:", num_atoms - num_Ar - num_Rn - 2 * num_y - 1)
