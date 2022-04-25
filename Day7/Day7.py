input = open("Day7/mini.txt", "r")
inputData = input.readlines()

reg = []

for each in inputData:
    inst = each.split(" -> ")
    reg.append(
        (inst[1].strip(), int(inst[0]) if inst[0].isnumeric() else inst[0].strip())
    )


print(reg)
