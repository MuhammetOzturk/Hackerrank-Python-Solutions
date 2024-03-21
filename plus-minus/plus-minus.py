#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    l = len(arr)
    positives,negatives,zeros = 0,0,0
    for i in arr:
        if i == 0:
            zeros += 1
        elif i > 0:
            positives += 1
        else:
            negatives += 1
            
    print(positives / l)
    print(negatives / l)
    print(zeros / l)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

