from time import sleep
import Slots
import Blackjack
import CasinoUtils
import os
import sys


#user management
CasinoUtils.clear()
print('Welcome to the Deamon Casino!')
print('Dont worry the only thing you will loose here is time and proccessor power.')
user = input('Enter your Username:')
CasinoUtils.clear()
user_len = len(user)

if not os.path.exists(sys.path[0] + r"\SaveData.txt"):
    SaveData = open(sys.path[0] + r"\SaveData.txt" , "w")
    SaveData.write('450000\n')
    SaveData.close()

SaveData = open(sys.path[0] + r"\SaveData.txt" , "r")

wincon = SaveData.readline()[:7]


AP = False
if AP == True & user == 'aldwin':
    userEdit = False
    try:
        while True:
            CasinoUtils.clear()
            print('Admin mode options:')
            print('1. Modify win condition')
            print('2. Edit profile')
            panel = input()
            
            if panel == '1':
                wincon = input('Enter new win condition:')
                wincon.replace('\n','')
                user_len = len("aldwin")
                SaveData = open(sys.path[0] + r"\SaveData.txt" , "r")
                temp = SaveData.readline()
                SaveData_temp = open(sys.path[0] + r"\SaveData_temp.txt" , "w")
                SaveData_temp.write(wincon + '\n')
                for i in SaveData:
                    if i[:user_len] == user:
                        SaveData_temp.write(user + ":" + str(Balance) + '\n')
                    else:
                        SaveData_temp.write(i)
                SaveData_temp.close()
                SaveData_temp = open(sys.path[0] + r"\SaveData_temp.txt" , "r")
                SaveData.close()
                SaveData = open(sys.path[0] + r"\SaveData.txt" , "w")
                for i in SaveData_temp:
                    SaveData.write(i)
                SaveData_temp.close()
                os.remove(sys.path[0] + r"\SaveData_temp.txt")
                SaveData.close()

            if panel == '2':
                user = input('Enter username to edit:')
                Balance = input('Enter new balance:')
                Balance.replace('\n',''); user.replace('\n','')
                user_len = len(user)
                SaveData = open(sys.path[0] + r"\SaveData.txt" , "r")
                wincon = SaveData.readline()
                SaveData_temp = open(sys.path[0] + r"\SaveData_temp.txt" , "w")
                SaveData_temp.write(wincon)
                for i in SaveData:
                    if i[:user_len] == user:
                        SaveData_temp.write(user + ":" + str(Balance) + '\n')
                    else:
                        SaveData_temp.write(i)
                SaveData_temp.close()
                SaveData_temp = open(sys.path[0] + r"\SaveData_temp.txt" , "r")
                SaveData.close()
                SaveData = open(sys.path[0] + r"\SaveData.txt" , "w")
                for i in SaveData_temp:
                    SaveData.write(i)
                SaveData_temp.close()
                os.remove(sys.path[0] + r"\SaveData_temp.txt")
                SaveData.close()

    except KeyboardInterrupt:
        sys.exit()
   
for i in SaveData:
    if i[:user_len] == user:
        i.replace('\n','')
        print('Welcome back ' + user + ' your balance is: $' + i[user_len+1:])
        UserData = i
        break
else:
    print('Welcome to the Daemon Casino ' + user + '. You have been given a initial balance of $5000.')
    SaveData.close()
    SaveData = open(sys.path[0] + r"\SaveData.txt" , "a")
    SaveData.write(user + ":5000" +  '\n')
    SaveData.close()
    SaveData = open(sys.path[0] + r"\SaveData.txt" , "r")

    for i in SaveData:
        if i[:user_len] == user:
            UserData = i
            SaveData.close()
            break
while True:
    try:
        print('Please select which game you want to play:')
        print('1. Slots')
        print('2. Blackjack')
        while True:
            game = input()
            if game == '1':
                CasinoUtils.clear()
                Slots.Slots(user,UserData,user_len,wincon)
                game = ''
                break
            elif game == '2':
                CasinoUtils.clear()
                Blackjack.BlackJack(user,UserData,user_len,wincon)
                game = ''
                break
            else:
                print('Invalid input')
                continue
    except KeyboardInterrupt:
        CasinoUtils.clear()
        print('Thank you for playing')
        sys.exit()