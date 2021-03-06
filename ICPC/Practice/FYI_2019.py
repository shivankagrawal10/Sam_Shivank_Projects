#import numpy as np
import os
import sys
from sys import *


def fwrite(filenum, answer:str):
    #with open(os.path.join(sys.path[0],f'./p_set/a00{filenum}.ans'), 'w') as f:
    #    f.write(f'{answer}')
    print(answer)
for i in range(1,2):
    #with open(os.path.join(sys.path[0],f'./p_set/a00{i}.in'), "r") as f:
    #    first = f.readline()


    first = str(sys.stdin.readline())
    if first[0:3] == '555':
        fwrite(i,'YES')
    else:
        fwrite(i,'NO')

