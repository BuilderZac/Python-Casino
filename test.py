import time
import CasinoUtils

test = CasinoUtils.GenDeck()
time.sleep(2)
for i in range(52):
    print(test[i] , " ", i)