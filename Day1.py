"""
Given an array, X,N of  integers, calculate and print the respective mean, median, and mode on separate lines.
If your array contains more than one modal value, choose the numerically smallest one.
Note: Other than the modal value (which will always be an integer),
your answers should be in decimal form, rounded to a scale of 1 decimal place (i.e.,12.3 ,7format).

Input Format
The first line contains an integer, N, the number of elements in the array.
The second line contains N space-separated integers that describe the array's elements.

Output Format
Print  lines of output in the following order:
Print the mean on the first line to a scale of 1 decimal place 
Print the median on a new line, to a scale of 1 decimal place 
Print the mode on a new line. If more than one such value exists, print the numerically smallest one.
"""


def calc_mean(size,num):
    sum_num=sum(num)
    mean=(sum_num/size)
    return mean

def calc_median(size,num):
    l1=sorted(num)
    s=size
    if s %2 != 0:
        med=int(s/2)
        median=l1[med]
        return median
    else:
        med1=int(s/2)
        med2=int(s/2)-1
        median1=l1[med1]
        median2=l1[med2]
        median=(median1+median2)/2
        return median 
def calc_mode(size, num):
    dict1 = {}
    for i in num:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return max(dict1, key=dict1.get)

if __name__=='__main__':
    size = int(input())
    numbers = list(map(int, input().split()))
    # size=int(input())
    # num=[]
    # input_numbers = int(input().split())
    # for num in input_numbers:
    #     num.append(int(num))
    res=calc_mean(size,numbers)
    print(res)
    result = calc_median(size, numbers)
    print(result)
    resu=calc_mode(size,numbers)
    print(resu)




"""
def calc_mean(nums):
    my_count = len(nums)
    my_sum = 0
    for num in nums:
        my_sum += num
    my_mean = my_sum / my_count
    return my_mean

def calc_median(nums):
    my_count = len(nums)
    sorted_nums = sorted(nums)
    if my_count % 2 != 0:
        mid_val = ((len(sorted_nums))/2) - 0.5
        my_median = sorted_nums[int(mid_val)]
    elif my_count % 2 == 0:
        mid_val_2_int = len(sorted_nums)/2
        mid_val_1_int = len(sorted_nums)/2 - 1 
        mid_val_2 = sorted_nums[int(mid_val_2_int)]
        mid_val_1 = sorted_nums[int(mid_val_1_int)]
        my_median = (mid_val_1 + mid_val_2)/2
    return my_median

def calc_mode(nums):
    freq_dict = {}
    for elem in nums:
        if elem in freq_dict:
            freq_dict[elem] += 1
        elif elem not in freq_dict:
            freq_dict[elem] = 1
    return max(freq_dict, key=freq_dict.get)

# Correct variable name (use lowercase 'x' instead of 'X')
x = (1, 2, 3, 4, 5,5)

print(calc_mean(x))
print(calc_median(x))
print(calc_mode(x))


"""


# import numpy as np
# from scipy import stats

# size = int(input())
# numbers = list(map(int, input().split()))
# print(np.mean(numbers))
# print(np.median(numbers))
# print(int(stats.mode(numbers)[0]))





"""
Task
Given an array,X , of N  integers and an array, W, representing the respective weights of X elements,
calculate and print the weighted mean of X elements. Your answer should be rounded to a scale of 1 decimal place
Function Description
Complete the weightedMean function in the editor below.
weightedMean has the following parameters:
- int X[N]: an array of values
- int W[N]: an array of weights
Prints
- float: the weighted mean to one decimal place
Input Format
The first line contains an integer,N , the number of elements in arrays X and W
The second line contains N space-separated integers that descdribe the elements of array X.
The third line contains N space-separated integers that descdribe the elements of array W.
"""


import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    res=[]
    for i in range(0,len(X)):
        res.append(X[i]*W[i])
    print(round(sum(res)/sum(W),1))
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)