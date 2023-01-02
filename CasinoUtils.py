import os
import sys
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def save(user_len,user,Balance,wincon):
    SaveData = open(sys.path[0] + r"\SaveData.txt" , "r")
    SaveData_temp = open(sys.path[0] + r"\SaveData_temp.txt" , "w")
    wincon = int(wincon)
    wincon = str(abs(wincon))
    SaveData_temp.write(wincon + '\n')

    temp = SaveData.readline()

    for i in SaveData:
        if i[:user_len] == user:
            SaveData_temp.write(user + ":" + str(Balance) + '\n')
        elif i == temp:
            continue
        else:
            SaveData_temp.write(i)
    SaveData_temp.close()
    SaveData.close()

    SaveData_temp = open(sys.path[0] + r"\SaveData_temp.txt" , "r")
    SaveData = open(sys.path[0] + r"\SaveData.txt" , "w")
    for i in SaveData_temp:
        SaveData.write(i)
    SaveData_temp.close()
    SaveData.close()
    os.remove(sys.path[0] + r"\SaveData_temp.txt")

def GenDeck():
    storedDeck = []
    suit = ["club","diamond","heart","spade"]
    for i in suit:
        for x in range(1,14):
            if x == 1:
                storedDeck.append(str(i + "," + "ace"))
            elif x == 11:
                storedDeck.append(str(i + "," + "joker"))
            elif x == 12:
                storedDeck.append(str(i + "," + "queen"))
            elif x == 13:
                storedDeck.append(str(i + "," + "king"))
            else:
                storedDeck.append(str(i + "," + str(x)))
    return(storedDeck)
