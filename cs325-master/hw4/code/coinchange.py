from collections import OrderedDict

def coinChanger(denomi, k, n):
     # Initialize matrix
     M = [[0 for j in range(n+1)] for i in range(k+1)]
     # Initialize values for penny 
     for j in range(n+1):
         M[0][j] = j    
         for i in range(1, k+1):
             for j in range(1, n+1):
                  if denomi[i] > j:
                      M[i][j] = M[i-1][j]
                  else:
                      M[i][j] = min(1 + M[i][j-denomi[i]], M[i-1][j])
                      return M

def findCoin(M, denomi, k, n):
    coins = []
    j = n
    for i in range(k, 0, -1):
        while j >= 0:
            if M[i][j] < M[i-1][j]:
                coins.append(denomi[i])
                j -= denomi[i]
            else:
                break
                # Handles pennies
            if j < denomi[1]:
                while j > 0:
                    coins.append(1)
                    j -= 1
                    return coins
                    # Program starts heref = open("data.txt", "r")for x in f:    line = [int(elem) for elem in x.split(' ')]    c = line[0]    k = line[1]    n = line[2]    denomi = [c**i for i in range(k+1)]   # List of denominations        M = coinChanger(denomi, k, n)         # Get a matrix by dynamic programming    coins = findCoin(M, denomi, k, n)     # Find coins for optimal solution by retrace matrix             freq = OrderedDict()                  # Store frequency of coins in a dictionary    for coin in coins:        if coin in freq:            freq[coin] += 1        else:            freq[coin] = 1        fout = open("change.txt", "a")    for k,v in freq.items():              # key-value pairs in ordered dictionary        fout.write(str(k) + ' ' + str(v) + '\n')    fout.write("==============================\n")        fout.close()                f.close()
