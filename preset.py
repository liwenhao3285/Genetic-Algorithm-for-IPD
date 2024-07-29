from random import randint
import numpy as np

k = 0
#A function for 'tit for tat' strategy
def tit(list):

    choice = 10*list[-1]

    return choice

#A function for always corp strategy
def coop(list):

    return 1

#A function for always betray strategy
def betray(list):
    return -1

#strategy that would return betray if its opponent had betrayed once before
def first_by_davis(list):

    choice = 1

    for i in range(len(list)):
        if list[i] == -1:
            choice = -1
    
    return choice

#strategy that behaved like 'tit for tat' except that the corp probability will slowly decend to 50%
def first_by_feld(list):

    choice = 9*list[-1] - 1.45 / 100 * (len(list) - 200) * randint(1,6)

    return choice

#Behave like 'tit for tat' for the first 3 round. then it follows specific equation after that
def nydegger(list1,list2):

    choice = 1
    list_A = [1,6,7,17,22,23,26,29,30,31,33,38,39,45,49,54,55,58,61]
    p = 0

    if len(list1) - 200 <=3:
        choice = 10*list1[-1]
        if list1[-2] == -1 and list1[-1] == 1:
            return -1
        return choice
    else:
        choice = 1
        p = 16*(1.5 - (list1[-1] + 0.5 * list2[-1])) + 4*(1.5 - (list1[-2] + 0.5 * list2[-2])) + (1.5 - (list1[-3] + 0.5 * list2[-3]))
        for i in range(len(list_A)):
            if p == list_A[i]:
                return -1
        return choice

#Behave like 'tit for tat', except that the probability of revange is 2/7
def grofman(list):
    
    choice = 5*list[-1] + randint(3,9)

    return choice

#behave like 'tit for tat', except that the revange will slowly increase
def shubik(list, k):

    if k != 0:
        k -= 1
        return -1
    elif list[-1] == -1:
        for i in range(len(list)):
            if list[i] == -1:
                k += 1
        return -1
    else:
        return 1

# “A player starts by cooperating for 10 rounds then plays Grudger, 
# defecting if at any point the opponent has defected.”
def davis(list):
    
    if len(list) - 200 <= 10:
        return 1
    else:    
        choice = 1

        for i in range(len(list)):
            if list[i] == -1:
                choice = -1
        
        return choice

# “This rule cooperates 90% of the time after a cooperation by the other. It 
# always defects after a defection by the other.”
def joss(list):

    choice = 9*list[-1] - randint(1,10)

    return choice

#This strategy will corp or betray randomly
def random(list):

    choice = randint(-10, 10)

    return choice