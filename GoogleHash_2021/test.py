import numpy as np
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
streeth_hash = {}
with open("./a.txt", "r") as f:
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
        streeth_hash[line[2]] = (int(line[0]),int(line[1]),int(line[3]))
        intersections[int(line[0])][int(line[1])] = line[2]#something
    cars = []
    for i in range(num_c):
        path = []
        line = f.readline()
        line = line.split(' ')
        for street in line[1:]:
            path.append(street)
        path[-1] = path[-1][:-1]
        cars.append(path)
with open('demo.txt', 'w') as f:
    f.write('Now the file has more content!')
