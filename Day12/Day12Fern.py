import json

def iterlist(l):
    array_sum = 0
    dict_sum = 0
    sum = 0
    for v in l:
        if isinstance(v, dict):
            dict_sum += iterdict(v)
        elif isinstance(v, list):
            array_sum += iterlist(v)
        elif isinstance(v, int):
            sum += v
    return sum + array_sum + dict_sum

def iterdict(d):
    tracking_sum = 0
    remove = False
    array_sum = 0
    dict_sum = 0
    for k, v in d.items():
        if isinstance(v, dict):
            dict_sum += iterdict(v)
        elif isinstance(v, list):
            array_sum += iterlist(v)
        elif isinstance(v, int):
            tracking_sum += v
        elif isinstance(v, str) and v == "red":
            remove = True
            print("remove", k, v)
    if remove:
        print(tracking_sum, array_sum, dict_sum)
        return 0
    return tracking_sum + array_sum + dict_sum

def js_abacus():
    f = open('Day12/input.json')
    data = json.load(f)
    total =0
    if isinstance(data, dict):
        total = iterdict(data)
    elif isinstance(data, list):
        total = iterlist(data)
    print(total)

if __name__ == "__main__":
    js_abacus()
