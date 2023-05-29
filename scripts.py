import re
import random



def throw_dice(list, throws, dice_size):
    for i in range(throws):
        list.append(random.randint(1,dice_size))
    return list

def TFTL_throw(dice_number):
    result = throw_dice([], int(dice_number), 6)
    throw_string = ''
    for i in result:
        throw_string += str(i) + " + "

    throw_string = throw_string[:-3]
    if result.count(6) == 0:
        emote = " <:clueless:1109878324253179914>"
    else: emote = " <:Prayge:1109877279334596721>"

    return "Wynik: " + throw_string + " \nSukcesów: **" + str(result.count(6)) + "**" + emote

def standard_throw(command):
    # print(command)
    if re.findall("[^kKdD0-9+]", command):  # find incorrect command
        return "Błąd w równaniu rzutu!"
    else:
        sum = 0
        emote = " <:um:1109877400927469628>"
        throw_string = ''     # string fo throw results
        result = []      # result values list
        split_throws = re.split("[+]", command)    # separated throws: 3k6 2k4

        for i in split_throws:
            if re.search("[kdKD]", i):      # check if separated part is throw or added value
                throw = re.split("[kdKD]", i)  # splitting throw to number of throws and dice
                if throw[0] != '':      # if number of dice is given
                    res = throw_dice([], int(throw[0]), int(throw[1]))
                    result.append(res)
                else:       # if number of dice is not given
                    res = throw_dice([], 1, int(throw[1]))
                    if throw[1] == "20":
                        if res[0] == 1:
                            emote = "\nKrytyczna porażka!!! <:clueless:1109878324253179914>"
                        elif res[0] == 20:
                            emote = "\nKrytyczny sukces!!! <:NOWAY:1109877122169835642>"
                    result.append(res)
            else:       # if separated part is added value
                temp = []
                temp.append(int(i))
                result.append(temp)

        for i in result:        # make string with throws results and sum them into sum var
            for j in i:
                throw_string += str(j) + ' + '
                sum += j



        throw_string = throw_string[:-3]        # delete ' + ' signs from last position
        return "Wynik: " + throw_string + "\nRazem: " + str(sum) + emote
