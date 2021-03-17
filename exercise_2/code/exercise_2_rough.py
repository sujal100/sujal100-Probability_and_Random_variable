# problem
''' A box contains 4 white balls and 3 red balls.
In succession, two balls are randomly selected
and removed from the box. Given that the first
removed ball is white, the probability that the
second removed ball is red is _____
(A) 1/3
(B) 3/7
(C) 1/2
(D) 4/7'''

# solution
import random


def pickBalls(nLoops=1000):
    Balls = [0]*3+[1]*4
    nHits = 0
    for _ in range(nLoops):
        b = random.sample(Balls, 2)
        while b[1] == 0:  # While 2nd ball is red
            b = random.sample(Balls, 2)
        if b[0]:  # If first ball was white
            nHits += 1
    return float(nHits) / nLoops


print('the probability that the second removed ball is red is ',format(pickBalls(1000000)))
print('Hence, answer is (C)')