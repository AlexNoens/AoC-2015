import hashlib

s = "yzbqklnj"
exit = False
num = 0
while exit == False:
    num += 1
    temp = s + str(num)

    result = hashlib.md5(temp.encode("utf-8"))
    if result.hexdigest()[:6] == "000000":
        exit = True

print(num)
