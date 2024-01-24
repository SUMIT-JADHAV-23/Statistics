# In a single toss of  fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.?
# <p>2 / 3</p>
# <p>5 / 6</p>
# <p>1 / 4</p>
# <p>1 / 6</p>
"""
To find the probability of getting a sum at most 9 when rolling a pair of six-sided dice, 
we can consider all the possible combinations of outcomes.
The total number of outcomes is 6×6=36(since each die has 6 faces).
Now, let's list the combinations where the sum is at most 9:
Sum = 2: (1, 1)
Sum = 3: (1, 2), (2, 1)
Sum = 4: (1, 3), (2, 2), (3, 1)
Sum = 5: (1, 4), (2, 3), (3, 2), (4, 1)
Sum = 6: (1, 5), (2, 4), (3, 3), (4, 2), (5, 1)
Sum = 7: (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)
Sum = 8: (2, 6), (3, 5), (4, 4), (5, 3), (6, 2)
Sum = 9: (3, 6), (4, 5), (5, 4), (6, 3)
There are 30 favorable outcomes (combinations with sums at most 9). Therefore, the probability is given by:
P(Sum at most 9)=Number of favorable outcomes/Total number of outcomes=30/36=5/6
"""

# Dice # 1
dice_1 = [1, 2, 3, 4, 5, 6]
# Dice # 2
dice_2 = dice_1.copy()
less_than_10 = 0
all_outcomes = 0
# Iterate through
for v1 in dice_1:
    for v2 in dice_2:
# add 1 for every pair to all_outcomes
        all_outcomes += 1
        if v1 + v2 < 10:
# add 1 for pairs that summed up to 9 or below to less_than_10.
            less_than_10 += 1
prob_less_than_10 = less_than_10 / all_outcomes
print(prob_less_than_10)


# Task
# In a single toss of  fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

# 1 / 9
# 1 / 6
# 2 / 3
# 5 / 6
"""
There are 6 number of ways for the sum of two dices to be 6: (1 + 5) (5 + 1) (2 + 4) (4 + 2) (3 + 3) (3 + 3). 
So we eliminate the last two since both dices are the same number. 
So the probability of getting the sum of 6 where the two dices are not the same = 4/36 (36 is the total outcomes of both dices)
"""
dice_1 = [1, 2, 3, 4, 5, 6]
dice_2 = dice_1.copy()

diff_and_sum_to_6 = 0
all_outcomes = 0
# for i in range(0,len(lst1)):
#     for j in range(0,len(lst2)):
for v1 in dice_1:
    for v2 in dice_2:
        all_outcomes += 1
        if (v1 != v2) and (v1 + v2 == 6):
            diff_and_sum_to_6 += 1

print(diff_and_sum_to_6)
print(all_outcomes)
prob_diff_and_sum_to_6 = diff_and_sum_to_6 / all_outcomes
print(prob_diff_and_sum_to_6)

# Task
# There are  urns labeled X, Y, and Z.


# Urn X contains 4 red balls and 3 black balls.
# Urn y contains 5 red balls and 4 black balls.
# Urn z contains 4 red balls and 4 black balls.

# One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

# 10 / 63
# 2 / 7
# 17 / 42
# 31 / 126

"""
modified the definition of X, Y, and Z to represent the possible outcomes of the dice rolls.
The itertools.product is used to generate all possible combinations of outcomes for X, Y, Z.
The count of favorable outcomes where the sum is 2 is calculated.
The probability is then computed using the Fraction class.
"""
from fractions import Fraction
from collections import Counter
import itertools

# Define the possible outcomes for each die
X = [1, 1, 1, 1, 0, 0, 0]  # Example: 1 represents a successful outcome, 0 represents an unsuccessful outcome
Y = [1, 1, 1, 1, 1, 0, 0, 0, 0]  # Example: 1 represents a successful outcome, 0 represents an unsuccessful outcome
Z = [1, 1, 1, 1, 0, 0, 0, 0]  # Example: 1 represents a successful outcome, 0 represents an unsuccessful outcome

# Generate all possible combinations of outcomes for X, Y, Z
TOTAL_SAMPLES = list(itertools.product(X, Y, Z))
TOTAL_SAMPLES_SIZE = len(TOTAL_SAMPLES)

# Count the number of favorable outcomes where the sum is 2
FAVOURABLE_OUTCOMES_SIZE = sum([sum(i) == 2 for i in TOTAL_SAMPLES])

# Calculate the probability
probability = Fraction(FAVOURABLE_OUTCOMES_SIZE, TOTAL_SAMPLES_SIZE)

print("Total Samples:", TOTAL_SAMPLES_SIZE)
print("Favorable Outcomes:", FAVOURABLE_OUTCOMES_SIZE)
print("Probability:", probability)
