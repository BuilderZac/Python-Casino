import os
from sys import path
import random

#Config host settings here
AdminMode = False
DataLocation = path[0] + r"\SaveData.txt"
TmpLocation = path[0] + r"\SaveDataTmp.txt"
#-----------------------------------------------

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def save(user_len,user,Balance,wincon):
    SaveData = open(DataLocation,"r")
    SaveData_temp = open(TmpLocation, "w")
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

    SaveData_temp = open(TmpLocation, "r")
    SaveData = open(DataLocation, "w")
    for i in SaveData_temp:
        SaveData.write(i)
    SaveData_temp.close()
    SaveData.close()
    os.remove(TmpLocation)

def GenDeck():
    storedDeck = []
    suit = ["club", "diamond", "heart", "spade"]
    for i in suit:
        for x in range(1, 14):
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
    return (storedDeck)

def DeckScramble():
    curDeck = GenDeck()
    for i in range(3000):
        slots = [random.randint(0, 51), random.randint(0, 51)]
        cards = [curDeck[slots[0]], curDeck[slots[1]]]
        curDeck[slots[0]] = cards[1]
        curDeck[slots[1]] = cards[0]
    return curDeck
