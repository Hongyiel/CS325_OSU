from collections import OrderedDict


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
                    