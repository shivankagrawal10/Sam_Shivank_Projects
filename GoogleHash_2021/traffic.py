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
        intersections[int(line[1])][int(line[0])] = line[2]#something
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
        
unused = {}
for i in range(0,num_i):
    unused[i] = 1
for c in cars:
    for name in c[1:-1]:
        if street_hash[name[0]][0] in unused:
            del unused[street_hash[name[0]][0]]
        if street_hash[name[0]][1] in unused:
            del unused[street_hash[name[0]][1]]
    if len(c) == 2:
        name = c[1]
        if street_hash[name[0]][0] in unused:
            del unused[street_hash[name[0]][0]]
schedule  = []
for i,x in enumerate(intersections):
    if len(x) == 1 or len(x) >1 and i not in unused:
        schedule.append(i)
        schedule.append(1)
        schedule.append(f'{list(x.values())[0]} 1')

with open('a_submission.txt', 'w') as f:
    f.write(f'{len(schedule)//3}\n')
    for s in schedule:
        f.write(f'{s}\n')
