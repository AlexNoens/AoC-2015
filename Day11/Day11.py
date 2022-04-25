import numpy as np
import re

input_alex = "hxbxwxba"
input2 = "hxbxxyzz"
input_fernie = ""
illegal = ["i", "o", "l"]

doubles_pattern = re.compile(r"([a-z])\1.*([a-z])\2")
invalid_pattern = re.compile(r"[ilo]")


def has_straight(input):
    for i in range(len(input) - 2):
        if (
            ord(input[i]) == ord(input[i + 1]) - 1
            and ord(input[i]) == ord(input[i + 2]) - 2
        ):
            return True
    return False


def check_for_bad(input):
    for i in range(0, len(input)):
        if input[i] == 105 or input[i] == 108 or input[i] == 111:
            input[i] += 1
    return input


def is_valid(input):
    if len(input) != 8:
        return False

    if not doubles_pattern.search(input):
        return False

    if invalid_pattern.search(input):
        return False

    if not has_straight(input):
        return False

    return True


def asciitize(input):
    return [ord(charecter) for charecter in input]


def increase(input):
    input = asciitize(input)
    input[-1] += 1
    if input[-1] > 122:
        input[-1] = 97
        input[-2] += 1
        if input[-2] > 122:
            input[-2] = 97
            input[-3] += 1
            if input[-3] > 122:
                input[-3] = 97
                input[-4] += 1
                if input[-4] > 122:
                    input[-4] = 97
                    input[-5] += 1
                    if input[-5] > 122:
                        input[-5] = 97
                        input[-6] += 1
                        if input[-7] > 122:
                            input[-7] = 97
                            input[-8] += 1

    return [chr(charecter) for charecter in check_for_bad(input)]


def check_valid(input):
    if 105 in input or 108 in input or 111 in input:
        return False

    return True


dat = increase(input_alex)

while not is_valid("".join(dat)):
    dat = increase(dat)
    # print("".join(dat))

print("".join(dat))
