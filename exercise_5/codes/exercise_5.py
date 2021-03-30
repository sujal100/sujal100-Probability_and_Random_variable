# problem
'''
Let X and Y be two statistically independent random variables uniformly
distributed in the ranges (−1, 1) and (−2, 1) respectively. 
Let Z = X + Y. then the probability that [Z ≤ −2] is
(a) zero 
(b)1/6
(c)1/3
(d)1/12
'''

# solution

import numpy as np

sample = 1000000

# generating uniform samples of x in the range (-1,1)
x = np.random.uniform(low=-1, high=1, size=sample)
# generating uniform samples of y in the range (-2,1)
y = np.random.uniform(low=-2, high=1, size=sample)

count = 0
for (i, j) in zip(x, y):  # taking each point (x,y)
    z = i+j
    if z <= -2:           # checking condition whether given condition
        count = count+1   # counting the number of points given codition is true

# calculating prob= no. of points in the Z<=-2/total no.of points of X and Y
p = count / sample
print("Probability that [Z<=-2] is ", p)
print("Hence, option (D) is correct")