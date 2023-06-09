import math
import os
import random
import re
import sys



#
# Complete the 'reducearray' function below.
#
# The function is expected to return an INTEGER.
#

def reducearray():
    array=[1,6,3,20]
    array.sort()
    cost=0
    while(len(array)>1):
        a=array[0]
        b=array[1]
        c=a+b
        cost=cost+a+b
        array.pop(0)
        array.pop(0)
        array.insert(0,c)
    return cost
    # Write your code here

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'value'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = reducearray()

    fptr.write(str(result) + '\n')

    fptr.close()