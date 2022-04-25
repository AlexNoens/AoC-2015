import numpy as np
import re

input = np.array([1, 1, 1, 3, 1, 2, 2, 1, 1, 3])
# input = np.array([1])
temp = np.array([])

for i in range(0, 30):
    try:
        c_val = input[0]
    except:
        c_val = 1
    count = 1

    for x in range(1, len(input)):
        if input[x] == c_val:
            count += 1
        else:
            temp = np.append(temp, count)
            temp = np.append(temp, c_val)
            c_val = input[x]
            count = 1
    print("run: ", i)
    temp = np.append(temp, count)
    temp = np.append(temp, c_val)
    input = temp.copy()
    temp = []

print(input)
