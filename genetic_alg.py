from random import *
import genetic_tools
import compete
import numpy as np;
from classgeneration import generation
import math

#This function generate the starting colony and coordinate other functions
#This function have no input
#This function have no output
def start_colony():

    global generation1
    global generation_dic
    generation1 = {}
    generation_dic = {}

    #Generate 200 individual for the starting colony
    for i in range(200):
        generation1['strategy{0}'. format(i)] = genetic_tools.random_gen()

    #Get the score of the first generation and generate next generation
    generation_dic[0] = generation(0, generation1, [])
    competation(1, generation1)

    #repeat the process for 50 generations
    for i in range(1, 50):
        competation(i + 1, generation_dic[i].get_generation_dic())

    #Record the result in text files
    file1 = open("1.txt", 'w')
    file2 = open("2.txt", 'w')
    file1.write(str(generation_dic[1].get_generation_dic()))
    file1.write(str(generation_dic[1].get_score_dic()))
    file2.write(str(generation_dic[49].get_generation_dic()))
    file2.write(str(generation_dic[49].get_score_dic()))
    file1.close()
    file2.close()

#This function generate a fitness score for each individual for 1 generation
#This function takes an generation number and the dictionary for all generation as input
#This function returns a list for fitness score as output
def competation(n, dictionary):

    global total_score
    total_score = []
    average_score = 0
    total_score.clear()

    #Generate fitness score for each individual in a generation
    for i in range(200):
        temp_store = compete.compete(i, dictionary)
        total_score.append(['strategy{0}'. format(i), temp_store])
        average_score += temp_store

    #Store the score list in generation_dic
    generation_dic[n-1].set_score_dic(total_score)

    #Print average score of all individuals in one generation
    print(average_score / 200)

    #Generate the next generation with function natural_selection
    natural_selection(n, total_score, dictionary)

#This function simulate natural selection for offspring generation
#This function takes a generation number, a fitness score list, and a dictionary for all generation as input
#This function have no output
def natural_selection(n, list, dictionary):

    selection_list = []
    selection_list.clear()
    selection_list2 = []
    selection_list2.clear()
    temp_store_dic = {}

    #Sort the fitness score list based on value for fitness scores
    list.sort(key = lambda x: x[1])

    for i in range(200):
        if randint(0,100) >= 90:
            genetic_tools.mutation(i, dictionary)

    #Generate a random selection list that have the following trait:
    #the individual with higher fitness value will be selected more frequently as parents
    while len(selection_list) < 400:
        selection_list = np.random.power(5, 4000)

    for i in range(400):
        selection_list2.append(math.ceil(selection_list[i] * 200) - 1)
    
    #Generate 200 offspring as the next generation
    for i in range(0, 399, 2):
        temp_store_dic['strategy{0}'. format(int(i/2))] = genetic_tools.independent_assortment(selection_list2[i], selection_list2[i+1], dictionary)

    #Store the next generation in dictionary for all generation
    generation_dic[n] = generation(n, temp_store_dic, [])


start_colony()