import sys
luc=[0,0]
luc[0]=2
luc[1]=1
a=1
b=1
c=0
seq_num = int(sys.stdin.readline())
for i in range(seq_num):
    luc.append(luc[-1]+luc[-2])
    '''
    c=a+b
    a=b
    b=c
    print(c)
    '''
for i in range(len(luc)):
    if(i%7==0 and i!=0):
        print()
    if(i%7==6):
        print(luc[i],end='')    
    print(luc[i],end=' ')
print()