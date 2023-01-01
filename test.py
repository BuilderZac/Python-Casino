import Cards
import time

test = Cards.deck()
time.sleep(2)
for i in range(40):
    print(test.printCard() , " ", i)