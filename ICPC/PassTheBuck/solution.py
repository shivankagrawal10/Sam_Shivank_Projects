'''
import numpy as np
states = 
with open('input.txt') as r:
    line = r.readLine().split(' ')
    nodes = int(line[0])
    for n in range(nodes):
'''
#recursively call neighbors multiplying probability by 1/n+1 n = neighbors
#when current is the winner we want add 1/n+1 * current probability to total
#recurse until sufficient precision

#unrelated problem

def subset_sum(a,M):
    m = [0 for i in range(0,M)]
    m[0] = 1
    for i in range(len(a)):
        for j in range(M,a[i]-1,-1):
            m[j] += m[j-a[i]]
    for i,x in enumerate(m):
        print(f'{i} {x}')

a = [2,4,6,8,10]

#subset_sum(a,sum(a))

def longest_inc_subsequence(a):
    n = len(a)
    m = [1 for i in range(0,n)]
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if(a[j] > a[i]):
                m[i] = max(m[i],m[j]+1)
    ans = 0
    for i in range(0,n):
        ans = max(ans,m[i])
    return(ans)
a = [1,2,3,4,22,6,7,8,9]
print(longest_inc_subsequence(a))
