#Made by CMDR BuilderZac
import random
import CasinoUtils
from time import sleep

def Slots(user,UserData,user_len,wincon):

    Balance = UserData[user_len+1:];Balance.replace('\n','')
    #main game loop
    while True:

        #take a input from user
        try:
            while True:
                print('Your balance is: $' + str(Balance))
                wager = input('Enter your wager:')

                try:
                    if wager.isdigit() is not True:
                        print('Invalid wager. Please enter a number.')
                        continue
                    elif int(wager) < 0:
                        print('Invalid wager. Please enter a positive number.')
                        continue
                    elif int(wager) > int(Balance):
                        print('You do not have enough money to wager that amount.')
                        continue
                    elif int(wager) % 1 != 0:
                        print('Invalid wager. Please enter a whole number.')
                        continue
                    else:
                        print('You have waged $' + wager)
                        break

                except:
                    print('That is not a valid wager. Please enter a valid wager.')

            #generates random numbers and display the results
            CasinoUtils.clear()
            print('Rolling.')
            sleep(0.1)
            print('Rolling..')
            sleep(0.1)
            print('Rolling...')
            sleep(0.1)
            CasinoUtils.clear()

            wincon = int(wincon)

            number = random.randint(1,1000000)
            if number <= 7500:
                roll1 = 7; roll2 = 7; roll3 = 7
                wincon -= 200000
                Balance = int(Balance) + (int(wager) * 5)
                msg = 'You rolled a triple 7. You win $' + str(int(wager) * 5) + '!'
            elif wincon >= number:
                roll1 = random.randint(1,12)
                if roll1 == 7:
                    roll1 = 6
                roll2 = roll1; roll3 = roll1
                wincon -= 45000
                Balance = int(Balance) + (int(wager) * 2)
                msg = 'You rolled three in a row. You win $' + str(int(wager) * 2) + '!'
            else:
                roll1 = random.randint(1,12)
                roll2 = random.randint(1,12)
                if roll2 == roll1:
                    roll2 = roll1 + 1
                roll3 = random.randint(1,12)
                if roll3 == roll2:
                    roll3 = roll2 - 1
                wincon += 25000 + abs((int(wager) * 0.1))
                Balance = int(Balance) + (int(wager) * -1)
                msg = 'You lost your wager.'

            wincon = abs(wincon)
            if wincon > 1000000: wincon = 900000
            if wincon < 50000: wincon = 50000

            wheel1 = [12,1,2,3,4,5,6,7,8,9,10,11,12,1]
            wheel2 = [12,1,2,3,4,5,6,7,8,9,10,11,12,1]
            wheel3 = [12,1,2,3,4,5,6,7,8,9,10,11,12,1]

            print('=========')
            print(' =' + str(wheel1[roll1 + 1]) + '=' + str(wheel2[roll2 + 1]) + '=' + str(wheel3[roll3 + 1]) + '=')
            print(' >' + str(wheel1[roll1]) + '=' + str(wheel2[roll2]) + '=' + str(wheel3[roll3]) + '<')
            print(' =' + str(wheel1[roll1 - 1]) + '=' + str(wheel2[roll2 - 1]) + '=' + str(wheel3[roll3 - 1]) + '=')
            print('=========')
            print(msg + ' Your balance is now $' + str(Balance))

        #closing and saving player data
        except KeyboardInterrupt:
            CasinoUtils.clear()
            print('Thank you for playing Slots!')
            CasinoUtils.save(user_len,user,Balance,wincon)
            sleep(1)
            CasinoUtils.clear()
            break