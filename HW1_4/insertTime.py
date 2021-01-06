# insertionSort Time calculate
import random
import time
# Testing Time complexity on the insertion sort
def testTime(n):
    Range = 10000 # range will until 10000
    List = [random.randint(0, Range) for i in range(n)] # get random list of the integer.
    # setting start time and end time for calculate time complexity
# Citation by https://www.tutorialspoint.com/generating-random-number-list-in-python
    Time_start = time.time()
    insertionSort(List, n)
    Time_end = time.time()
    Time_cal = Time_end - Time_start
    # getting result
    return Time_cal
#Citation by https://www.geeksforgeeks.org/insertion-sort/
def insertionSort(arr, length):
    for j in range(1, length):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

# this will be the number of the n
caseList = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]

for case in caseList:
    Time_total = 0
    Time_total += testTime(case)
    # print result in format
    print("Calculating... n: {}, time: {}".format(case, Time_total))
