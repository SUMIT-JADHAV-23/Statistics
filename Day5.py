# problem-1

"""The properties of the binomial distribution are:
There are two possible outcomes: true or false, success or failure, yes or no.
There is ‘n’ number of independent trials or a fixed number of n times repeated trials.
The probability of success or failure remains the same for each trial.
Only the number of success is calculated out of n independent trials.
Every trial is an independent trial, which means the outcome of one trial does not affect the outcome of another trial.
 """

# Task
# The ratio of boys to girls for babies born in Russia is 1.09:1.
# If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?
# Write a program to compute the answer using the above parameters.
# Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)

Std_in=input().split()
s=Std_in
print(s)
n=6 #trials

#convert list obj in float
p=float(Std_in[0])/float(Std_in[1])+float(Std_in[1])
q=float(Std_in[1])/float(Std_in[0])+float(Std_in[1])
print(p,q)

def binominal():
    result=0
    #range (1,7)=(n=6)
    for i in range(1,7):
        pdf = (factorial(n)/(factorial(i)*((factorial(n-i)))))*(p**i)*(q**(n-i))
        if i >= 3:
            result = result + pdf
    return round(result,3)

print(binominal())

"""
# from math import factorial as f
# b, g = list(map(float, input().split()))
# p = b / (b+g)
# def comb(n, r):
#     return f(n) / (f(r) * f(n-r))
# n = 6
# res=(sum(p**k * (1-p)**(n-k) * comb(n, k) for k in range(3, 7)))
# print(round(res,3))
# # 0.6957033161509107

"""

"""#Your input
pp=str(input())
p1=float(pp[:pp.find(' ')])
p2=float(pp[pp.find(' ')+1:])
pf=0.0
#This is the probability of boy
p = p1/(p1+p2)
from math import factorial as f
def comb(n,r):
    return f(n) / f(r) / f(n-r)

#You have to sum the probabilities of 3,4,5 or 6 boys
for i1 in range(3,7):
    #You were not using the right formula (it's a multiplication, not a sum)
    prob_i1 = pow(p,i1)*pow(1-p,6-i1)*comb(6,i1)
    pf += prob_i1
print("%.3f"%(pf))
"""

"""
pp=str(input())
p1=float(pp[:pp.find(' ')])
p2=float(pp[pp.find(' ')+1:])
pf=0.0
pa=0.0
from math import factorial as f
def comb(n,r):
    return f(n) / f(r) / f(n-r)
for i1 in range(0,7):
    if i1>=3:
        pf=pf+(pow(p1,i1)*pow(p2,6-i1))*comb(6,i1)
    pa=pa+(pow(p1,i1)*pow(p2,6-i1))*comb(6,i1)
print("%.3f"%(pf/pa))"""


# problem-2
# Task
# A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. 
# What is the probability that a batch of 10 pistons will contain:
# 1.No more than 2 rejects?
# 2.At least 2 rejects?
# Input Format:
# A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons)
# #accepted
def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) // (fact(x) * fact(n-x))

def binomial(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int, input().split(" ")))
print(round(sum([binomial(i, n, p/100) for i in range(3)]), 3))
print(round(sum([binomial(i, n, p/100) for i in range(2, n+1)]), 3))

"""#problem-3"""
#negative binominal distribution
# A negative binomial experiment is a statistical experiment that has the following properties:
# The experiment consists of n repeated trials.
# The trials are independent.
# The outcome of each trial is either success (s) or failure (f).
# P(s) is the same for every trial.
# The experiment continues until x successes are observed.
# If X is the number of experiments until the x'th success occurs, then X is a discrete random variable called a negative binomial.

# Negative Binomial Distribution
# Consider the following probability mass function:b*(x,n,p)=comb(n-1  x-1)*(p**x)*((1-p)**(n-x))
# The function above is negative binomial and has the following properties:
# The number of successes to be observed is x.
# The total number of trials is n.
# The probability of success of 1 trial is p.
# The probability of failure of 1 trial q, where q=1-p.
# b*(x,n,p) is the negative binomial probability, meaning the probability of having x-1 successes after n-1 trials and having x successes after n trials.
"""
Geometric Distribution
The geometric distribution is a special case of the negative binomial distribution that deals with the number of Bernoulli trials required to get a success 
(i.e., counting the number of failures before the first success). Recall that X is the number of successes in N independent Bernoulli trials
The geometric distribution is a negative binomial distribution where the number of successes is 1. We express this with the following formula:
g(n,p)=((1-p)**(n-1) )* p
# """
# Task
# The probability that a machine produces a defective product is 1/3. What is the probability that the 1 defect occurs the 5 item produced?


def Geometric(n,p):
    return (1-p)**(n-1) * p

nume,deno = list(map(int,input().split()))
n = int(input())
print(f"{Geometric(n,nume/deno):.5f}")


"""# problem-4"""
# Task
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1 defect is found during the first 5 inspections?

# sol-1
def Geometric(n, p):
    result = 0
    for k in range(1, 6):
        result +=  p*(1-p)**(k-1)
        print(result)

    return result

nume, deno = list(map(int, input().split()))
n = int(input())
print(f"{Geometric(n, nume/deno):.3f}")

#sol-2

p=1/3

def geomprob(k,p):
    return p*(1-p)**(k-1)

print("{0:.3f}".format(sum([geomprob(k,p) for k in range(1,6)])))