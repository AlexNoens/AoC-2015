import numpy as np
import time

class Ingredient:
    def __init__(self,capacity = 0, durability = 0, flavour = 0, texture = 0,calories = 0):
        self.capacity = capacity
        self.durability = durability
        self.flavour = flavour
        self.calories = calories
        self.texture = texture
        self.tsp = 0

    def get_score(self):
            return  self.tsp*self.capacity, self.tsp*self.durability, self.tsp*self.flavour, self.tsp*self.texture
    def get_cal(self):
        return self.tsp*self.calories

def load_input(file):
    f = open(file, "r")
    return f.readlines()

def make_list(file):
    list = []
    for each in load_input(file):
        each = each.replace(",","")
        each = each.strip()
        split = each.split(" ")
        list.append(Ingredient(int(split[2]),int(split[4]),int(split[6]),int(split[8]),int(split[10])))
    return list

def get_score(tsp,list):
    score_l = []
    for i in range(0,len(list)):
        list[i].tsp = tsp[i]
    for each in list:
        score_l.append(np.array(each.get_cal()))
    score =  np.zeros(score_l[0].shape)
    for each in score_l:
        score += each
    if score != 500:
        return 0

    score = 0
    score_l = []
    for i in range(0,len(list)):
        list[i].tsp = tsp[i]
    for each in list:
        score_l.append(np.array(each.get_score()))
    score =  np.zeros(score_l[0].shape)
    for each in score_l:
        score += each
    final_score = 1
    for each in score:
        if each < 0:
            final_score = 0
            break
        final_score *= each
    return final_score

tsp = [97,1,1,1]
list = make_list("Day15/input.txt")
max =0
max_tsp = [0,0,0,0]
calorie_goal = 500
start = time.perf_counter()
# TIMER START
for i in range(0, len(list)):
    max_tsp[i] = 500/list[i].calories
final_score = get_score(tsp,list)
if final_score > max:
    max = final_score
while tsp[3] < 98:
    tsp[0] -= 1
    tsp[1] += 1
    if tsp[0] < 1:
        tsp[2] += 1
        tsp[1] = 1
        tsp[0] = 100 - tsp[1] - tsp[2] - tsp[3]
        if tsp[0] < 1:
            tsp[3] += 1
            tsp[2] = 1
            tsp[1] = 1
            tsp[0] = 98 - tsp[3]
    if max_tsp[3] < tsp[3] + tsp[2]:
        continue
    final_score = get_score(tsp,list)
    if final_score > max:
        max = final_score


print("Answer:",max, "Runtime:", round((time.perf_counter() - start)*1000), "ms")
