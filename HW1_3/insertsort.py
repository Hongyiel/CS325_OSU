# Oregon State University
# CS 325
# Hongyiel Suh
# insert function #
def insertionSort(conv_arr):
    # length of array will compare to 1 to n
    print("Start insertion")
    print(conv_arr[0])
    i = 2
    for i in range(1, len(conv_arr)):

        key = conv_arr[i] # will get array for compare each values

        # Move value to key and compare next key: if  next key is
        # greater than current key current position will go head
        j = i-1
        while j >= 1 and key < conv_arr[j] :
                conv_arr[j + 1] = conv_arr[j]
                j -= 1
        conv_arr[j + 1] = key

insertsort = open("insert.txt", "w")
f = open("data.txt", "r")
line1 = f.readline()
x1 = line1.split()

arr = x1
conv_arr = x1

n = len(arr)

for i in range(n):
    conv_int = int(arr[i])
    conv_arr[i] = conv_int

insertionSort(conv_arr)

for i in range(conv_arr[0]):
    insertsort.write(str(conv_arr[i+1]))
    insertsort.write(str(" ")),

insertsort.write(str("\n"))
#######################################

line2 = f.readline()
x2 = line2.split()
print("second Read for merge")
print(x2)

arr = x2
conv_arr = x2

n = len(arr)
for i in range(n):
    conv_int = int(arr[i]),
# driver code to test the above code
insertionSort(arr)
for i in range(int(conv_arr[0])):
    if i==0:
        insertsort.write(str(""))
    else:
        insertsort.write(str(conv_arr[i]))
        insertsort.write(str(" ")),


#######################################

# line2 = f.readline()
# x2 = line2.split()
# print(x2)
f.close()
insertsort.close()
# Citation by https://www.geeksforgeeks.org/insert-sort/
