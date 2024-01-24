"""
Task
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. 
Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed as the following list of (x,y) points:
95 85
85 95
80 70
70 65
60 70
If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? 
Determine the equation of the best-fit line using the least squares method, then compute and print the value of y when 80.
Input Format
There are five lines of input; each line contains two space-separated integers describing a student's respective x and y grades.
Output Format
Print a single line denoting the answer, rounded to a scale of 3 decimal places
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import math

X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

mean_x = statistics.mean(X)
mean_y = statistics.mean(Y)

diff_x = 0
diff_y = 0
for i in range(len(X)):
    diff_x += pow(X[i] - mean_x, 2)
    diff_y += pow(Y[i] - mean_y, 2)
    
stand_dev_x = math.sqrt(1 / len(X) * diff_x)
stand_dev_y = math.sqrt(1 / len(Y) * diff_x)

sum = 0
for i in range(len(X)):
    sum += ((X[i] - mean_x) / stand_dev_x ) * ((Y[i] - mean_y) / stand_dev_y)
    
r = 1 / len(X) * sum

b = r * stand_dev_y / stand_dev_x
a = mean_y - b * mean_x

answer = a + b * 80

print(round(answer, 3))


"""
95 85
85 95
80 70
70 65
60 70

sumX = 390.0
meanX = 78.0
sumY = 385.0
meanY = 77.0
sumX2 = 31150.0
sumXY = 30500.0
b = 0.6438356164383562
a = 26.78082191780822

result = a + b * 80 = 78.288

"""