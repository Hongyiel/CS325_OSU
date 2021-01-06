# HONGYIEL
# define DFS function
def DFS(a, row, col):
    row_len=len(a) #length of row
    column_length = len(a[0]) # length of column
    if row < 0 or row >= row_len or col < 0 or col >= column_length or a[row][col] == 0:
        return
    a[row][col] = 0

    DFS(a, row+1, col)
    DFS(a, row-1, col)
    DFS(a, row, col+1)
    DFS(a, row, col-1)


#count DFS function
def count_island(a):
    count = 0 #init count value
    if len(a) == 0:
        return count

    # looping to get count
    for i in range(len(a)):
        for j in range(len(a[i])):
        # if island is found
            if a[i][j] == 1:
                count = count + 1
                DFS(a, i, j)

    return count

# main

a = ([[1,1,1,0,0],
    [0,0,0,0,1],
    [1,0,0,0,1],
    [0,0,0,0,0]])
count_is = count_island(a)
print(count_is)
# Citation
# https://www.geeksforgeeks.org/strongly-connected-components/
# https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
