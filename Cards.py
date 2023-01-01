import random
class player:
    storedHand = []
    def __init__(self,hand):
        self.storedHand.append(hand)

class deck:
    storedDeck = []
    pickedCard = -1
    def __init__(self):
        for i in range(4):
            suit = i
            for x in range(1,14):
                val = x
                tmp = i,x
                self.storedDeck.append(tmp)
        random.shuffle(self.storedDeck)
    def printCard(self):
        self.pickedCard += 1
        return(self.storedDeck[self.pickedCard])