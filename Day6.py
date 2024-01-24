# posiion Distribution
# Task-1
# A random variable,X , follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5
# Input Format
# The first line contains X's mean. The second line contains the value we want the probability for:
# 2.5
# 5
# If you do not wish to read this information from stdin, you can hard-code it into your program.
# Output Format
# Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e.,1.245 format).


"""
from math import factorial, exp

miu = float(input())
x = int(input())
poisson_prob = ((miu ** x) * exp(-miu)) / factorial(x)
print("%.3f" %poisson_prob)

"""

"""
import math

mean = 2.5
k = 5

p = pow(mean, k) * pow(math.e, -mean) / math.factorial(k)

print(round(p, 3))

"""
from math import factorial as fc
e, l, k = 2.71828, 2.5, 5
print(f'{(l**k * e**-l) / fc(k):.3f}')

"""
Task-2
The manager of a industrial plant is planning to buy a machine of either type A  or type B. For each day’s operation:
1.The number of repairs,X , that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating  A is 160+40X**2.
2.The number of repairs,Y , that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is 128+40Y**2.
Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day.
Find and print the expected daily cost for each machine.

"""


import math
mean_A, mean_B = map(float, input().split())
cost_of_operating_A = 160 + (40 * (math.pow(mean_A, 2) + mean_A))
cost_of_operating_B = 128 + (40 * (math.pow(mean_B, 2) + mean_B))
print(round(cost_of_operating_A, 3))
print(round(cost_of_operating_B, 3))



X,Y=map(float,input().split())
print(round(160+(40*(X+X**2)),3))
print(round(128+(40*(Y+Y**2)),3))



# print(160 + 40*(0.88+0.88**2))
# print(128 + 40*(1.55+1.55**2))



"""
# Nominal Distribution
Task-3
In a certain plant, the time taken to assemble a car is a random variable X  having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours.
What is the probability that a car can be assembled at this plant in: 1.less than 19.5 hours   2.between 20 to 22

Input Format:There are  lines of input (shown below):
20 2
19.5
20 22
The first line contains 2 space-separated values denoting the respective mean and standard deviation for X. The second line contains the number associated with question 1. 
The third line contains 2 space-separated values describing the respective lower and upper range boundaries for question 2.

Output Format
There are two lines of output. Your answers must be rounded to a scale of 3 decimal places (i.e.,1.2345  format):
On the first line, print the answer to question 1 (i.e., the probability that a car can be assembled in less than 19.5 hours).
On the second line, print the answer to question 2 (i.e., the probability that a car can be assembled in between 20 to 22 hours).

"""

# #calculating the cumulative distribution function (CDF) for specific values related to a normal distribution.
# from scipy.stats import norm
# #Takes input for the mean (m) and standard deviation (s) of the normal distribution.
# m, s = map(int, input().split())
# #Takes input for a specific value (x) for which the CDF will be calculated.
# x = float(input())
# #Takes input for the range (a,b) for which the probability between a and b will be calculated.
# a, b = map(int, input().split())
# #Calculates the Z-score for the specific value x and prints the CDF for that Z-score.
# z1 = (x - m) / s
# print(NormalDist().cdf(z1))
# #Calculates the Z-scores for the range (a,b) and prints the probability between these two Z-scores.
# z2 = (a - m) / s
# z3 = (b - m) / s
# print(NormalDist().cdf(z3) - NormalDist().cdf(z2))



import math as m
def cdf(mn, std, x):
    return 0.5 * (1 + m.erf((x-mn)/(std*m.sqrt(2))))
    
print(f'{cdf(20,2,19.5):.3f}')
print(f'{cdf(20,2,22) - cdf(20,2,20):.3f}')



"""

Task-4
The final grades for a Physics exam taken by a large group of students have a mean of U=70 and a standard deviation of SD=10.
If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

1.Scored higher than 80
2.passed the test(grade>60)
3.failed the test(grade<60)

Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

Input Format
There are 3 lines of input (shown below):
70 10
80
60
The first line contains 2 space-separated values denoting the respective mean and standard deviation for the exam. 
The second line contains the number associated with question 1.
The third line contains the pass/fail threshold number associated with questions 2 and 3.



"""



import math as m 

def calculate_percent_cdf(mean, stdev, x):
    p = (1/2 * (1 + m.erf((x-mean)/(stdev*m.sqrt(2)))))*100
    return p

if __name__ == '__main__':        
    # read input
    mean, std = map(int, input().split())
    x1 = int(input())
    x2 = int(input())
    
    # calculate percentages
    p1 = 100 - calculate_percent_cdf(mean, std, x1)
    p2 = 100 - calculate_percent_cdf(mean, std, x2)
    p3 = calculate_percent_cdf(mean, std, x2)
    
    # print results
    print(round(p1, 2))
    print(round(p2, 2))
    print(round(p3, 2))