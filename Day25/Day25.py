input = [2981, 3075]

coord = [1, 1]
ans = 20151125

while coord != input:
    coord[0] += 1
    ans = (ans * 252533) % 33554393
    first_indx = coord[0]
    for i in range(0, coord[0] - 1):
        if coord == input:
            break
        coord[0] -= 1
        coord[1] += 1
        ans = (ans * 252533) % 33554393
    if coord == input:
        break
    coord = [first_indx, 1]

print("Machine code:", ans)
