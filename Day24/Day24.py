from numpy import product
from regex import E
import numpy


def load_input(file):
    f = open(file, "r")
    lines = []
    for each in f.readlines():
        lines.append(int(each.strip()))
    return lines


def subset_sum(numbers, target, solutions, partial=[]):
    s = sum(partial)
    # check if the partial sum is equals to target
    if s == target:
        solutions.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1 :]
        subset_sum(remaining, target, solutions, partial + [n])
    return solutions


def validate_solution(numbers, target, solutions, partial=[]):
    s = sum(partial)
    # check if the partial sum is equals to target
    if s == target:
        solutions.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1 :]
        validate_solution(remaining, target, solutions, partial + [n])
    return solutions


packages = load_input("Day24/input.txt")

weight_goal = int(sum(packages) / 3)

possibilies = []
possibilies = subset_sum(packages, weight_goal, possibilies)

possibilies.sort(reverse=True)

min_length = len(packages)
min_qe = numpy.prod(possibilies[1])
smol_solutions = []

for each in possibilies:
    if len(each) <= min_length:
        min_length = len(each)
        smol_solutions.append(each)
        if numpy.prod(each) <= min_qe:
            min_qe = numpy.prod(each)

print("Part 1:", min_qe)


## JUST DO IT AGAIN FOR PART 2 HAHAHA

weight_goal = int(sum(packages) / 4)

possibilies = []
possibilies = subset_sum(packages, weight_goal, possibilies)

possibilies.sort(reverse=True)

min_length = len(packages)
min_qe = numpy.prod(possibilies[1])
smol_solutions = []

for each in possibilies:
    if len(each) <= min_length:
        min_length = len(each)
        smol_solutions.append(each)
        if numpy.prod(each) <= min_qe:
            min_qe = numpy.prod(each)

print("Part 2:", min_qe)

# for each in possibilies:
# print("validating", each)
# if validate(each, packages):
# print("Lowest QE:", product(each))
