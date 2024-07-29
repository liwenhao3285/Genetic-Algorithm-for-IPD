from random import *

#This function generate random individuals for the starting colony
#This function have no input
#This function returns a list as output
def random_gen():

    list = []
    list.clear()

    list.append(randint(-100,100))

    for i in range(200):
        list.append(randint(-10,10))

    list.append(randint(-10,10))
    return list

#This function simulate mutation to randomly swap one trait for an individual
#This function takes the individual number and dictionary for current generation as input
#This function produce an resulting list for individual as output
def mutation(n,dictionary):

    list1 = []
    list1.clear()
    list1 = dictionary.get('strategy' + str(n))

    x = randint(0,len(list1) - 1)
    if x == 0:
        list1[0] = randint(-100,100)
    else:
        list1[x] = randint(-10,10)

    return list1

#This function simulate independent assortment for offspring generation
#This function takes two individual number and dictionary for current generation as input
#This function produce an offspring individual list as output
def independent_assortment(x,y,dictionary):

    list3 = []
    list4 = []
    list3.clear()
    list4.clear()

    list5 = []
    list5.clear()

    list3 = dictionary.get('strategy' + str(x))
    list4 = dictionary.get('strategy' + str(y))

    rand = randint(-11, 10)

    if rand >= 0:
        n = round(0.5 * len(list3))
        list5 = list3[0:n] + list4[n : len(list4)]
    else:
        n = round(0.5 * len(list4))
        list5 = list4[0:n] + list3[n : len(list3)]

    return list5

#This function represent the decision making process
#This function takes an individual number, dictionary for current generation and the list for his opponent move as input
#This function return a score for decision making as output: positive for corp and negetive for betray
def desicion(n, list, dictionary):

    list7 = []
    list7.clear()
    score = 0

    list7 = dictionary.get('strategy' + str(n))
    score = list7[0]

    for i in range(200):
        score += list7[i + 1] * list[-i]

    for i in range(len(list7) - 201):
        score += list7[i + 201] * randint(-10, 10)

    return score