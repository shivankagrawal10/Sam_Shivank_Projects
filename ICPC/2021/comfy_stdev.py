import sys
import math
numbers=[]

numbers = sys.stdin.readline().split()
numbers=[float(i) for i in numbers]
n=len(numbers)
sum=sum(numbers)
mean=sum/n
numerator=0
for i in numbers:
    numerator+=(i-mean)**2
numerator= math.sqrt(numerator/(n-1))
if(numerator<=1):
    print("COMFY")
else:
    print("NOT COMFY")
'''
num = str(sys.stdin.readline())
num = num.split(' ')
num[-1]=num[-1][:-2]
print(num)
68.2 68 69.0004 68 69.8 70.123 72 73.10009 74 75.0
'''
