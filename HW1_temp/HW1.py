# Oregon State University
# CS 325
# Hongyiel Suh
# insert function #
def insertionSort(conv_arr):
    # length of array will compare to 1 to n
    for i in range(1, len(conv_arr)):

        key = conv_arr[i] # will get array for compare each values

        # Move value to key and compare next key: if  next key is
        # greater than current key current position will go head
        j = i-1
        while j >= 0 and key < conv_arr[j] :
                conv_arr[j + 1] = conv_arr[j]
                j -= 1
        conv_arr[j + 1] = key
# mergeSort
def mergeSort(conv_arr):
    if len(conv_arr) >1:
        mid = len(conv_arr)//2 # try to fin mid of the line
        L = conv_arr[:mid] # get divide insert array
        R = conv_arr[mid:] # get array half

        mergeSort(L) # Getting sort the firt half
        mergeSort(R) # Getting sort the second half

        i = j = k = 0
        # copy data from L and R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                conv_arr[k] = L[i]
                i+= 1
            else:
                conv_arr[k] = R[j]
                j+= 1
            k+= 1
        # try to check this is correct or not
        while i < len(L):
            conv_arr[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            conv_arr[k] = R[j]
            j+= 1
            k+= 1
########################################################
insertsort = open("insert.txt", "w")
mergesort = open("merge.txt", "w")

f = open("data.txt", "r")
line1 = f.readline()
x1 = line1.split()
print("The First Read")
print(x1)

arr = x1
conv_arr = x1

n = len(arr)

for i in range(n):
    conv_int = int(arr[i])
    conv_arr[i] = conv_int


print(conv_arr[1])
# Driver code to test above
insertionSort(conv_arr)

for i in range(n):
    insertsort.write(str(conv_arr[i]))
    insertsort.write(str(" ")),

insertsort.write(str("\n"))


mergeSort(conv_arr)

for i in range(n):
    mergesort.write(str(conv_arr[i]))
    mergesort.write(" "),

mergesort.write(str("\n"))



print("This is first line from original")
print(conv_arr)
print("\n")
#######################################

line2 = f.readline()
x2 = line2.split()
print("second Read for merge")
print(x2)

arr = x2
conv_arr = x2

n = len(arr)
for i in range(n):
    conv_int = int(arr[i])
# driver code to test the above code
insertionSort(arr)

for i in range(n):
    insertsort.write(str(arr[i]))
    insertsort.write(str(" "))


mergeSort(arr)

for i in range(n):
    mergesort.write(str(arr[i]))
    mergesort.write(" "),


#######################################

# line2 = f.readline()
# x2 = line2.split()
# print(x2)
f.close()
insertsort.close()
mergesort.close()
# Citation by https://www.geeksforgeeks.org/merge-sort/
