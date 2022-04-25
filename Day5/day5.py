def find_double_double(string):
    for x in range(0, len(string) - 2):
        if str(string[x] + string[x + 1]) in string[(x + 2) :]:
            return True
    return False


def find_gapped_double(string):
    for x in range(0, len(string) - 2):
        if string[x] == string[x + 2]:
            return True
    return False


def find_double(str):
    for char in str:
        if char == old:
            return True
        old = char
    return False


def find_three_vowels(str):
    count = 0
    for char in str:
        if (
            (char == "a")
            or (char == "e")
            or (char == "i")
            or (char == "o")
            or (char == "u")
        ):
            count += 1
        if count >= 3:
            return True
    return False


def find_naughty(str):
    if ("ab" in str) or ("cd" in str) or ("pq" in str) or ("xy" in str):
        return True
    return False


def find_nice(str):
    if not find_naughty(str) and find_double(str) and find_three_vowels(str):
        return True
    return False


def find_really_nice(string):
    if find_double_double(string) and find_gapped_double(string):
        return True
    return False


nice_count = 0

input = open("Day5/list2.txt", "r")
inputData = input.read()
input.close
inputData = inputData.split()

for line in inputData:
    if find_really_nice(line):
        nice_count += 1

print(nice_count)
