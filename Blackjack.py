import CasinoUtils
import random
from time import sleep

def BlackJack(user,UserData,user_len,wincon):
    Balance = UserData[user_len+1:];Balance.replace('\n','')
    #main game loop
    while True:
        try:
            while True:
                print('Your balance is: $' + str(Balance))
                wager = input('Enter your wager:')

                deck = CasinoUtils.DeckScramble()
                






        except KeyboardInterrupt:
            CasinoUtils.clear()
            print('Thank you for playing BlackJack!')
            CasinoUtils.save(user_len,user,Balance,wincon)

            sleep(1)
            CasinoUtils.clear()
            break
