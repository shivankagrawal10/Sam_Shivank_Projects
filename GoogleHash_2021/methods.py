import numpy as np
import os
import sys
#duration of simulation
dur = 0
#num of intersections o to I-1
num_i = 0
#num streets
num_s = 0
#num cars
num_c = 0
#bonus points for car that reaches before dur
bonus = 0
#street name is key, value: (start,end,length)
street_hash = {}
with open(os.path.join(sys.path[0],"a.txt"), "r") as f:
    first = f.readline()
    first = first.split(' ')
    dur = int(first[0])
    num_i = int(first[1])
    num_s = int(first[2])
    num_c = int(first[3])
    bonus = int(first[4])
    #2d array, 1st dimension is intersection id and 2nd is array of destinations from i
    intersections = []
    for i in range(num_i):
        intersections.append({})
    for i in range(num_s):
        line = f.readline()
        line = line.split(' ')
        street_hash[line[2]] = (int(line[0]),int(line[1]),int(line[3]))
        intersections[int(line[1])][int(line[0])] = 1 #outgoing edge -> key: incoming edge, val: delay
    cars = []
    for i in range(num_c):
        path = []
        line = f.readline()
        line = line.split(' ')
        line[-1] = line[-1][:-1]
        for street in line[1:]:
            path.append([street,street_hash[street][2]])
        #path[-1] = path[-1][:-1]
        cars.append(path)

def x_path(path:list()):
    return sum([i[1] for i in path])

def delay_time(timestamp:int,intersec_sum:int,currdelay:int):
    modval = timestamp % (intersec_sum + currdelay)
    if(timestamp % (intersec_sum+currdelay)>currdelay):
        return modval - currdelay
    return 0

def sum_of_intersections(curr_street, delay_dict):
    return sum([val for key,val in delay_dict.items() if key != curr_street])


print(x_path(cars[0]))
print(intersections[1])
print(sum_of_intersections(3,intersections[1]))