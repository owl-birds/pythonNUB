import math
# Finding any fnnc in math
#print(help(math))
print(math.floor(9.621))
print(math.ceil(9.621))
print(round(9.43))
# ROUNDING TO EVEN VALUE
print(round(4.5))
print(round(6.5))
print(round(7.5))
print(round(5.5))
print(math.pi)
print(math.inf)
print(math.nan)  # NOT A NUMBER
print(math.log(math.e))
# CUSTOM BASE
print(math.log(100, 10))
print(math.log(math.e ** 2, math.e))
print(math.log(math.e, math.e))
print(math.sin(90))
print(math.cos(90))
print(math.sin(0))
print(math.cos(0))
# 180 angles == pi
print(math.radians(180))
import random
# seeddd
#random.seed(221810193)
print(random.randint(1, 100))
print(random.randint(1, 100))
mylist = list(range(30))
print(random.choice(mylist))
print(random.choice(mylist))

# WR SAMPLE
wrSample = random.choices(population=mylist, k=10)
print(wrSample)
print(mylist)
# WOR SAMPLE
worSample = random.sample(population=mylist, k=10)
print(worSample)
print(mylist)

# RANDOM DISTRIBUTION
# UNIFORM DISTRIBUTION
# continous, random picks a calue between a and b, each value
# has equal change of being  picked
print(random.uniform(a=0, b=100))
# NORMAL/GAUSSIAN DISTRIBUTION
print(random.gauss(mu=0, sigma=1))