"""
Task-1
Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.
Input Format
The first line contains an integer, n , denoting the size of data sets X and Y.
The second line contains N space-separated real numbers (scaled to at most one decimal place), defining data set X.
The third line contains N space-separated real numbers (scaled to at most one decimal place), defining data set Y.
Output Format
Print the value of the Pearson correlation coefficient, rounded to a scale of 3 decimal places.


"""

# import statistics as stat
from sys import stdin, stdout
import math

def mean(arr):
    return sum(arr) / len(arr)

def sd(arr, mean):
    squared_diff_sum = sum((x - mean)**2 for x in arr)
    variance = squared_diff_sum / len(arr)
    return math.sqrt(variance)

def covariance(X, Y):
    mean_X = mean(X)
    mean_Y = mean(Y)
    covariance_sum = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X)))
    cov = covariance_sum / len(X)
    return cov

def pearson_correlation(X, Y):
    cov_XY = covariance(X, Y)
    st_dev_X = sd(X, mean(X))
    st_dev_Y = sd(Y, mean(Y))
    coefficient = cov_XY / (st_dev_X * st_dev_Y)
    return coefficient

n = int(stdin.readline().strip())
X = list(map(float, stdin.readline().strip().split()))
Y = list(map(float, stdin.readline().strip().split()))

if len(X) != len(Y):
    print("Error: Data sets X and Y must have equal lengths")
else:
    t = pearson_correlation(X, Y)
    print(round(t, 3))



"""
Task-2  Spearman's Rank Correlation Coefficient
Given two n-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.
Input Format
The first line contains an integer,n , denoting the number of values in data sets X and Y.
The second line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set X.
The third line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set Y.
Output Format
Print the value of the Spearman's rank correlation coefficient, rounded to a scale of 3 decimal places.

We know that data sets  and  both contain unique values,so the rank of each value in each data set is unique. 
Because of this property  we can use the following formula to calculate the value of Spearman's rank correlation coefficient

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

X_sort = sorted(X)
Y_sort = sorted(Y)

rank_X = []
rank_Y = []

for i in range(n):
    for j in range(n):
        if X[i] == X_sort[j]:
            rank_X.append(j+1)
        if Y[i] == Y_sort[j]:
            rank_Y.append(j+1)

d = 0
for i in range(n):
    d += pow((rank_X[i] - rank_Y[i]), 2)
    
Spearman_rank_coef = 1 - 6 * d / (n * (n * n - 1))
print(round(Spearman_rank_coef, 3))
