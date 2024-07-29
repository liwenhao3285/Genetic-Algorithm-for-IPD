import preset
import genetic_tools

#This function generate the fitness score for one individual
#This function takes an individual number and the dictionary for current generation as input
#This function returns fitness score as output
def compete(x, dictionary):

    score_total = 0
    k = 0

    #Each individual will compete with 11 preset strategy
    for y in range(11):
        list_temp_A = []
        list_temp_B = []
        list_temp_A.clear()
        list_temp_B.clear()

        for i in range(200):
            list_temp_A.append(0)
            list_temp_B.append(0)

        score_A = 0
        score_B = 0
        preset_list = [preset.shubik(list_temp_B, k), preset.nydegger(list_temp_B, list_temp_A), preset.betray(list_temp_B), preset.coop(list_temp_B), \
            preset.first_by_davis(list_temp_B), preset.davis(list_temp_B), preset.first_by_feld(list_temp_B), preset.grofman(list_temp_B), preset.joss(list_temp_B), \
                preset.random(list_temp_B), preset.tit(list_temp_B)]

        for i in range(200):

            a = preset_list[y]
            #b = preset.tit(list_temp_A)
            b = genetic_tools.desicion(x, list_temp_A, dictionary)

            if a >= 0:
                a = 1
            else:
                a = -1
            if b >= 0:
                b = 1
            else:
                b = -1
            
            list_temp_A.append(a)
            list_temp_B.append(b)
            list_temp_A.pop(0)
            list_temp_B.pop(0)

            #3 points for both corporate, 0 for corporate being betrayed, 
            #5 points for betray vs. corporate, 1 point for both betray
            if list_temp_A[-1] == 1 and list_temp_B[-1] == 1:
                score_A += 3
                score_B += 3
            elif list_temp_A[-1] == -1 and list_temp_B[-1] == 1:
                score_A += 5
            elif list_temp_A[-1] == 1 and list_temp_B[-1] == -1:
                score_B += 5
            elif list_temp_A[-1] == -1 and list_temp_B[-1] == -1:
                score_A += 1
                score_B += 1
        score_total += score_A

    #print(score_total/11)
    return score_total / 11

#compete(1,1)