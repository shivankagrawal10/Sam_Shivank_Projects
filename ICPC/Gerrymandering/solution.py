with open('input.txt', 'r') as file:
    vnum = int(file.readline())
    vertices = []
    for i in range((vnum+3)//4):
        line = file.readline()
        line = [int(x) for x in line.split(' ')]
        for j in range(4):
            vertices.append((line[j],line[j+1]))
print(vnum)
print(vertices)

#get area
cx = 0
cy = 0
area = 0
for i in range(vnum-1):
    v1 = vertices[i]
    v2 = vertices[i+1]
    area += v1[0]*v2[1] - v2[0]*v1[1]
    cx += (v1[0]+v2[0])*(v1[0]*v2[1] - v2[0]*v1[1])
    cy += (v1[1]+v2[1])*(v1[0]*v2[1] - v2[0]*v1[1])

area*=.5
cx /= (6*area)
cy /= (6*area)

