def load_input(file):
    f = open(file, "r")
    return f.readlines()

def make_list(file):
    list = []
    for number in load_input(file):
        list.append(int(number.strip()))
    return list

def check_children(list,in_total):
    child_count = 0
    for j in range(0,len(list)):
        total = in_total + list[j]
        if total < 150:
            child_count += check_children(list[j+1:], total)
        elif total == 150:
            child_count += 1
        elif total > 150:
            continue
    return child_count

nums = make_list("Day17/fern.txt")

nums.sort()
print(nums)
count = 0
min = 5000
stop = False
max_depth = 6

for i in range(0,len(nums)):
    count += check_children(nums[i+1:],nums[i])

print(count)
