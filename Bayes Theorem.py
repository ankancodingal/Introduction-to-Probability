# ---------------------------Step Throat - Part 1---------------------------
def find_prob(a,b):

	if a==1:
		prob_a = 0.2
		if b==1:
			prob_bga = 0.85
		elif b==2:
			prob_bga = 0.15
		else:
			print("Invalid Choice")
		prob_a_and_b = prob_a * prob_bga
		print("Proability of b given a:", prob_bga)
		print("Probability of both the events occuring:", prob_a_and_b)

	elif a==2:
		prob_a = 0.8
		if b==1:
			prob_bga = 0.02
		elif b==2:
			prob_bga = 0.98
		else:
			print("Invalid Choice")
		prob_a_and_b = prob_a * prob_bga
		print("Proability of b given a:", prob_bga)
		print("Probability of both the events occuring:", prob_a_and_b)

	else:
		print("Invalid Choice")

print("Let's calculate probability. Please enter choices for the events...")

print("Person has step throat? \n 1. Yes \n 2. No")
a = int(input("Enter your choice (1/2): "))

print("Person has tested positive? \n 1. Yes \n 2. No")
b = int(input("Enter your choice (1/2): "))

print("Probabilities for event a and b:")
find_prob(a,b)

#----------------------------------Step Throat - Part 2----------------------
prob_st = 0.2

prob_st_pos = 0.2*0.85
prob_nst_pos = 0.8*0.02
prob_positive = prob_st_pos + prob_nst_pos 

prob_pos_given_st = 0.85

prob_result = (prob_st*prob_pos_given_st)/prob_positive

print("Probability of person testing positive having step throat is :", round((prob_result),3))

#--------------------------------------Dice Roll--------------------------------------
import numpy as np

# create 6 sided "die"
die_sides = int(input("enter number of sides for dice (6/12) : "))
die = range(1, die_sides)

# set number of rolls
num_rolls = int(input("Enter number of times you want to roll the dice : "))

# roll the "die" the set amount of times
results = np.random.choice(die, size = num_rolls, replace = True)
print(results)

#-----------------------Coin PMF---------------------------------------
import scipy.stats as stats

# value of interest
# change this
x = 3

# sample size
# change this
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print("Probability of getting 3 heads")
print(prob_1)

prob_2 = 1-stats.binom.pmf(0, n=10, p=.5)-stats.binom.pmf(1, n=10, p=.5)-stats.binom.pmf(2, n=10, p=.5)
print("Probability of getting more than 2 heads")
print(prob_2)

#-----------------------------------------Let's Try PMF------------------------------
import scipy.stats as stats

# calculate probability
prob_1 = stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5)
print("Probability of observing between 2 and 4 heads")
print(prob_1)
