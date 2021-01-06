# Midterm problem 7
# Hongyiel Suh
import sys

# the basic format is that
# [input]
# 4 5 # first, setting the list and item
# 2 3
# 3 4
# 4 5
# 5 6
#

N, K = map(int, input().split()) # split in int format in " "

the_box = [[0,0]] # initial array values
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)] # prepare get values

# get array space (first input) and type the values from user input
for _ in range(N):
    the_box.append(list(map(int, input().split())))
#knapsack problem solve
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = the_box[i][0]
        value = the_box[i][1]
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #if smaller than weight, get value which is above
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
print(knapsack[N][K])

# Citation: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
