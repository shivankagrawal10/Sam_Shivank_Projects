import sys
import math

        
def get_neighbors(i,j):
    #print(i,j,end=': ')
    if(grid[i][j]==0):
        return (0,0)
    card=0
    adj=0
    if(i<n_rows-1):
        if(j!=0):
            adj+=check(i+1,j-1)
        adj+=check(i+1,j)
        card+=check(i+1,j)
        if(j<n_cols-1):
            adj+=check(i+1,j+1)
            card+=check(i,j+1) 
            adj+=check(i,j+1)  
    elif(j<n_cols-1):
        adj+=check(i,j+1)
        card+=check(i,j+1) 
    return (card,adj)
def check(i,j):
    if(grid[i][j]==1):
        return 1
    return 0

dim = sys.stdin.readline().split()
n_rows=int(dim[0])
n_cols=int(dim[1])
grid=[]
for i in range(n_rows):
    grid.append(sys.stdin.readline().split())
    grid[-1]=[int(j) for j in grid[-1]]
c=0
a=0
for i in range(n_rows):
    for j in range(n_cols):
        temp = get_neighbors(i,j)
        #print(temp)
        c+=temp[0]
        a+=temp[1]
print(f'{c} {a}')

'''
5 5
1 0 0 1 0
0 1 1 0 1
0 1 0 1 1
1 0 1 1 1
0 1 1 1 1
'''