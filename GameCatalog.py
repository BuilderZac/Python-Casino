import CasinoUtils
from time import sleep

#import game modules here
import Blackjack
import Slots
#-------------------------------------------

#add games to list
def GameList():
    print('Please select which game you want to play:')
    print('1. Slots')
    print('2. Blackjack')
#--------------------------------------

#install launch arguments for game here
def LaunchGame(selection,user,UserData,user_len,wincon):
    if selection == '1':
        CasinoUtils.clear()
        Slots.Slots(user,UserData,user_len,wincon)
        game = ''
    elif game == '2':
        CasinoUtils.clear()
        Blackjack.BlackJack(user,UserData,user_len,wincon)
        game = ''
    #-----------------------------------------

    else: #Dont touch this else statment
        print('Invalid input')
        sleep(2)
        CasinoUtils.clear()
        game=''