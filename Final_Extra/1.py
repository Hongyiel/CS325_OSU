# Minimum amount of coins
# Hongyiel Suh

# count action (when the ways go processing + 1)

# coin [1 , 2 , 5]
# amount = 11

# minus biggest coin first
# A Naive recursive python program to find minimum of coins
# to make a given change V
import sys

def getCoins(coins, m, V):
    if( V == 0 ):
        return 0

    #setting store in max size number which from system input
    store = sys.maxsize
    # init store value
    for i in range(0,m):
        if (coins[i] == 0):
            return 0
            # if coin setting 0 then return 0
        if (coins[i] <= V):
            sub_store = getCoins(coins, m, V - coins[i])
            # get coin's remain count
            if(sub_store != sys.maxsize and sub_store + 1 < store):
                store = sub_store + 1
                # get number when coin is valid
    return store
    # return store value when the coin using well
coins = [1,10,25,50]

m = len(coins)
V = 40
require_coin_num = getCoins(coins,m,V)
print (require_coin_num)
