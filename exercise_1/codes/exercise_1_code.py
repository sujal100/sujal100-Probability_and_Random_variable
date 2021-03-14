#problem
'''A die is thrown. If E is the event ”the number
appearing is a multiple of 3” and F be the event
”the number appearing is even” then find whether
E and F are independent ?'''

#solution
import random

#Function for roll the dice.
def roll_the_dice(Event):
    n_simulation=1000000
    count=0
    #each iteration of the for loop is trial.
    for i in range(n_simulation):

        #Roll dice
        die=random.randint(1,6)

        #decide if we should add it to count

        #event A for multiple of 3
        if Event=='A':
            if die%3==0:
                count+=1

        #event B for even numbers       
        elif Event=='B':
            if die%2==0:
                count+=1
        
        #find A and B
        else :
            if die%3==0 and die%2==0:
                count+=1

    return count/n_simulation

print("Probability of multiple of 3, Pr(A) = ",round(roll_the_dice('A'),2))
print("Probability of even number, Pr(B) = ",round(roll_the_dice('B'),2))
print("Probability of even multiple of 3, Pr(A and B) = ",round(roll_the_dice('A and B'),2))
print("Since,\n\tPr(E).Pr(F) = ",round(roll_the_dice('A')*roll_the_dice('B'),2)," = Pr(A and B)")
print("So, event A and B are independent events.")