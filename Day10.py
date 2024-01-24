#Multiple line regression

from sklearn import linear_model

first_input=input()
m = int(first_input.split()[0])
n = int(first_input.split()[1])

x_s = []
y_s = []
for i in range(n):
    x_n_y = input().split()      
    x_s.append([float(x_n_y[j]) for j in range(m)])
    y_s.append(float(x_n_y[-1]))

lm = linear_model.LinearRegression()
lm.fit(x_s, y_s)
a = lm.intercept_
b = lm.coef_
b_s = [b[k] for k in range(m)]

q = int(input())
for l in range(q):
    tests = input().split()
    summed = a 
    for i in range(m):
        summed += b_s[i]*float(tests[i])
    print(summed)