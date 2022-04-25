import ntpath
import queue

import numpy as np

class node:
    right  = (-1,-1)
    down = (-1,-1)
    left  = (-1,-1)
    up = (-1,-1)
    cost = 0
    point = []
    end = []
    path = []
    def __init__(self,point,grid,in_cost,in_path,end,max):
        shape = grid.shape
        if(in_cost >= max):
            return
        self.path = in_path[:]
        self.path.append(point)
        if(point[0]+1 < shape[0]):
            if (point[0]+1,point[1]) not in self.path:
                self.right = (point[0]+1,point[1])
        if(point[1]+1 < shape[1]):
            if (point[0],point[1]+1) not in self.path:
                self.down = (point[0],point[1]+1)
        if(point[0]-1 < 0):
            if (point[0]-1,point[1]) not in self.path:
                self.up = (point[0]-1,point[1])
        if(point[1]-1 < 0):
            if (point[0],point[1]-1) not in self.path:
                self.left = (point[0],point[1]-1)
        self.cost = grid[point[0]][point[1]] + in_cost
        self.point = point
        self.end = end

    def check_solved(self):
        if self.point == self.end:
            return True
        return False

def open_input():
    f = open("mini.txt","r")
    clean_raw = []
    rows = 0
    for line in f:
        rows += 1
        clean_raw.append(line.strip())
    i = 0
    j = 0
    grid = np.zeros((rows, len(clean_raw[0])))
    for line in clean_raw:
        for point in line:
            if(point == "\n"):
                continue
            grid[i][j] = int(point)
            j +=1
        j = 0
        i += 1
    return grid


grid = open_input()
start =  (0,0)
end = (grid.shape[0]-1,grid.shape[1]-1)

total = 0
for row in grid:
    for each in row:
        total += each

max = total/2

queue = queue.Queue()
queue.put(node(start,grid,0,[],end,max))
solved = []


while(not queue.empty()):
    cur_node = queue.get()
    if cur_node.check_solved():
        solved.append(cur_node.cost)
    else:
        if cur_node.down[0] > 0:
            queue.put(node(cur_node.down, grid, cur_node.cost, cur_node.path, end,max))
        if cur_node.right[0] > 0:
            queue.put(node(cur_node.right, grid, cur_node.cost, cur_node.path, end,max))
        if cur_node.up[0] > 0:
            queue.put(node(cur_node.up, grid, cur_node.cost, cur_node.path, end,max))
        if cur_node.down[0] > 0:
            queue.put(node(cur_node.down, grid, cur_node.cost, cur_node.path, end,max))

    cur_node = []

print(min(solved)-grid[0][0])
