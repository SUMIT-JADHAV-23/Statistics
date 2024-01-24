"""
Task
Suppose a family has  children, one of which is a boy. What is the probability that both children are boys?

1 / 3
1 / 2
2 / 3
1 / 9

In this problem, the family has two children, and you know that at least one of them is a boy. 
The sample space can be represented as the possible gender combinations for the two children: BB, BG, GB, GG.
However, since you know that at least one child is a boy, you can exclude the GG case. So, the reduced sample space is: BB, BG, GB.
Now, you want to find the probability that both children are boys given this reduced sample space. The only case where both children are boys is BB.
Therefore, the probability is the number of favorable outcomes (BB) divided by the total number of outcomes in the reduced sample space.

The probability is=p(both boys | at least one boy)=(Number of BB outcomes/Total number of outcomes in reduced sample space)

In this case, it=p(both boys | at least one boy)=1/3

"""
from fractions import Fraction
# Define the sample space
sample_space = ['BB', 'BG', 'GB']

# Count the number of outcomes where both children are boys
favorable_outcomes = sum(1 for outcome in sample_space if 'BB' in outcome)

# Calculate the total number of outcomes
total_outcomes = len(sample_space)

# Calculate the probability using Fraction to maintain exact fractions
probability = Fraction(favorable_outcomes, total_outcomes)

# Print the result
print(probability)

"""
# Task
# You draw  cards from a standard -card deck without replacing them. What is the probability that both cards are of the same suit?

# 1 / 156
# 1 / 39
# 12 / 39
# 12 / 51

# A standard deck has 52 cards, and it consists of four suits: hearts, diamonds, clubs, and spades. Each suit has 13 cards.
# When drawing two cards without replacement, the total number of ways to choose the first card is 52. Once the first card is drawn, there are 51 cards remaining for the second draw.
# Now, let's consider the favorable outcomes - drawing two cards of the same suit. There are 4 suits, and for each suit
# you can choose 2 cards out of the 13 in that suit. So, the number of favorable outcomes is p=(4×(13/2))/(52/2).
# Now, the probability is given by the number of favorable outcomes divided by the total number of outcomes.
"""
from itertools import combinations
lst = list(13*'c' + 13*'d' + 13*'h' + 13*'s')
comb = list(combinations(lst,2))
x = [i for i in comb if i[0]==i[1]]
print(len(x) / len(comb))


"""
Task
A bag contains  red marbles and  blue marbles. Then,  marbles are drawn from the bag, at random, without replacement. If the first marble drawn is red, what is the probability that the second marble is blue?

1 / 12
7 / 12
1 / 6
2 / 3
Solution:
P(R) = 3/7
P(B) = 4/7
P(R|B) = 3/6 = 1/2
P(R|Bc) = 2/6 = 1/3
P(Bc) = 1-4/7 = 3/7
P(B|R) = P(R|B) * P(B) / P(R|B) * P(B) + P(R|Bc) * P(Bc)
P(B|R) = { (1/2) * (4/7) } / { (1/2) * (4/7) + (1/3) * (3/7) }
P(B|R) = { (4/14) } / { (4/14) + (1/7) }
P(B|R) = { (4/14) } / { (4/14) + (2/14) }
P(B|R) = (4/14) / (6/14)
P(B|R) = (4/6)
P(B|R) = (2/3)
"""
lst, lst2 = list('rrrbbbb'), list('rrbbbb')  # Two scenarios/lists

S1, S2 = len(lst), len(lst2)  # Length of each list

A = len([i for i in lst if i == 'r'])  # Count of 'r' in lst
B = len([i for i in lst2 if i == 'b'])  # Count of 'b' in lst2

prob_A = A / S1  # Probability of drawing 'r' in the first scenario
prob_B = B / S2  # Probability of drawing 'b' in the second scenario

prob_AandB = prob_A * prob_B  # Probability of both events happening
prob_BgivenA = prob_AandB / prob_A  # Probability of drawing 'b' given that the first marble drawn is 'r'

print(prob_BgivenA)  # Print the result



