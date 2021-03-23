# problem
''' 
In an experiment, a fair die is rolled until two sixes are obtained in succession. The probability that
the experiment will end in the fifth trial is equal to  _____
(A) 125/6^{5} = 0.0161
(B) 150/6^{5} = 0.0193
(C) 175/6^{5} = 0.0225
(D) 200/6^{5} = 0.0257
'''

# solution
import random


def roll_the_dice(n_simulation=1000000):
    count = 0 # count favourable outcome.

    # each iteration of the for loop is trial.
    for i in range(n_simulation):

        # Roll dices 5 times
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        die_3 = random.randint(1, 6)
        die_4 = random.randint(1, 6)
        die_5 = random.randint(1, 6)

        # Fourth and Fifth is 6 and Third is not 6.
        if die_4 == 6 and die_5 == 6 and die_3 != 6:

            # First and Second not become 6 simultaneously.
            if die_1 != 6 or die_2 != 6:
                count += 1
    return count/n_simulation

print('Probability of experiment end at Fifth trail = ',round(roll_the_dice(), 4))
print('Hence, answer is (C)')