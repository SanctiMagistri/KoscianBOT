import re
import random

def throw_dice(list, throws, dice_size):
    for i in range(throws):
        list.append(random.randint(1,dice_size))
    return list

def TFTL_throw(command):
    throw_string = ''
    split_throws = re.split("[tT]", command)    # separate number of dices from t's

    if split_throws[0] != '':   # check if number of dices is on 1st or 2nd position
        res = throw_dice([], int(split_throws[0]), 6)
    else:
        res = throw_dice([], int(split_throws[1]), 6)

    for i in res:
        throw_string += str(i) + " + "

    throw_string = throw_string[:-3]
    if res.count(6) == 0:
        emote = " :clueless:"
    else: emote = " :EZ:"

    return "Wynik: " + throw_string + " \nSukcesów: **" + str(res.count(6)) + "**" + emote

def standard_throw(command):
    sum = 0
    emote = " :um:"
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
                        emote = "\nKrytyczna porażka!!! :clueless:"
                    elif res[0] == 20:
                        emote = "\nKrytyczny sukces!!! :EZ:"
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

def check_command(command):
    if re.findall("[^kKdDtT0-9+]", command):    # find incorrect command
        return "Błąd w równaniu rzutu!"
    else:
        if re.findall("[tT]", command):     # check for TFTL command
            if re.findall("[^tT0-9]", command):     # check if TFTL is only command
                return "Mieszane komendy rzutu! Proszę wpisać ponownie!"
            else:
                return TFTL_throw(command)
        else:
            if re.findall("[^kKdD0-9+]", command):      # check if this is standard command
                return "Mieszane komendy rzutu! Proszę wpisać ponownie!"
            else:
                return standard_throw(command)