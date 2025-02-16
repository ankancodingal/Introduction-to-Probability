#--------------------------Coin CDF---------------------------
import scipy.stats as stats

# calculate the probability
prob = 1 - stats.binom.cdf(6, 10, 0.5)

print("the probability of getting more than 6 heads in 10 coin flips is :", prob)

#---------------------------------Rain Expectation-----------------
import scipy.stats as stats

# expected value = 10, probability of observing 6
prob1 = stats.poisson.pmf(6, 10)
print("probability of raining for exactly 6 days :", prob1)

# expected value = 10, probability of observing 12-14
prob2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10)
print("probability of raining for 12-14 days :", prob2)

#-------------------------------------Expected Calls--------------------------
import scipy.stats as stats

## Checkpoint 1
# calculate prob_more_than_20
prob1 = 1-stats.poisson.cdf(20, 15)

# print prob_more_than_20
print(prob1)

## Checkpoint 2
# calculate prob_17_to_21
prob2 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)

# print prob_17_to_21
print(prob2)

#------------------------------Rain Expectations-----------------------------
import scipy.stats as stats

# expected value = 10
# probability of observing 12 or more
prob1 = 1 - stats.poisson.cdf(11, 10)
print("Probability of observing 12 or more rainy days is :", prob1)

# expected value = 10
# probability of observing between 12 and 18
prob2 = stats.poisson.cdf(18, 10) - stats.poisson.cdf(11, 10)
print("Probability of observing between 12 to 18 rainy days is :", prob2)

