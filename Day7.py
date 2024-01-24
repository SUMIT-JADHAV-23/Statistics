"""
Task
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. 
The box weight of this type of cargo follows a distribution with a mean of u=205 pounds and a standard deviation of sd=15 pounds.
Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

Input Format
There are 4 lines of input (shown below):
9800
49
205
15

The first line contains the maximum weight the elevator can transport. The second line contains the number of boxes in the cargo. 
The third line contains the mean weight of a cargo box, and the fourth line contains its standard deviation.
If you do not wish to read this information from stdin, you can hard-code it into your program

"""
# maxLimit = 9800;
# int n = 49;

# mean = 205;
# stdDev = 15;

# meanX = n * mean;
# stdDevX = math.sqrt(n) * stdDev;
# # p = probability(meanX, stdDevX, maxLimit);

import math

def cdf(mean, variance, x):
    return 0.5*(1 + math.erf((x-mean)/math.sqrt(2*variance)))

max_weight = int(input())
num_boxes = int(input())
mean_weight = int(input())
std_dev = int(input())

mean = mean_weight*num_boxes
variance = num_boxes*std_dev**2

print(round(cdf(mean, variance, max_weight), 4))



# if name == "main": maximum = int(input()) #x contain_box = int(input()) #n m = int(input()) #mean u = int(input()) #u

# import math

# mean = contain_box * m stdev = math.sqrt(contain_box) * u z = (maximum-mean)/(math.sqrt(2)*stdev) prob = 0.5 + math.erf(z)/2

# print(round(prob,4))

"""
Task
The number of tickets purchased by each student for the University X vs. 
University Y football game follows a distribution that has a mean of u=2.4 and a standard deviation of 2.
A few hours before the game starts, 100 eager students line up to purchase last-minute tickets.
If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

Input Format
There are 4 lines of input (shown below):
250
100
2.4
2.0

The first line contains the number of last-minute tickets available at the box office. 
The second line contains the number of students waiting to buy tickets. 
The third line contains the mean number of purchased tickets, and the fourth line contains the standard deviation.
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format
Print the probability that 100 students can successfully purchase the remaining 250 tickets, rounded to a scale of 4 decimal places 

"""

# task-2

import math as m
def cdf(mn, std, x):
    return 1/2 * (1 + m.erf((x-mn)/(std*m.sqrt(2))))
print(f'{cdf(2.4*100, 2*m.sqrt(100), 250):.4f}')


"""

Task
You have a sample of 100 values from a population with mean u=500 and with standard deviation 80.
Compute the interval that covers the middle 95% of the distribution of the sample mean;
in other words, compute A and B such that P(A<x<B)=0.95. Use the value of Z=1.96. Note that Z is the z-score.

Input Format
There are five lines of input (shown below):
100
500
80
.95
1.96

The first line contains the sample size. The second and third lines contain the respective mean (U) and standard deviation (SD). 
The fourth line contains the distribution percentage we want to cover (as a decimal), and the fifth line contains the value of z.
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format
Print the following two lines of output, rounded to a scale of 2 decimal places.
On the first line, print the value of A.
On the second line, print the value of B.

"""



# task-3

import math as m
mn, std, z = 500*100, 80*m.sqrt(100), 1.96
A, B = (mn-z*std)/100, (mn+z*std)/100
print(f'{A:.2f}\n{B:.2f}')