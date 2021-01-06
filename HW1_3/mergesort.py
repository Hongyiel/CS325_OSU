# OSU CS 325
f = open("data.txt", "r") # open file

#Citation by https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr, length):
    if length == 1:
        return
        # when the merge sort is 1 then get return nothing
    l_mid = length // 2 # get value of the mid value
    l_left = arr[:l_mid]    # left position array
    l_right = arr[l_mid:]   # right position array

    #merge them in recursivly
    mergeSort(l_left, len(l_left))
    mergeSort(l_right, len(l_right))
    #then merge them in final round
    merge(l_left, l_right, arr)

def merge(left, right, arr):
    idx_left = idx_right = idx_input = 0
# init left , right , arr
    while idx_left < len(left) and idx_right < len(right):
        if (left[idx_left] < right[idx_right]):
            arr[idx_input] = left[idx_left]
            idx_left += 1
            # compare left and right index when left arr is below than right arr
        else:
            arr[idx_input] = right[idx_right]
            idx_right += 1
            # when is not compare this function
        idx_input += 1
            #then moving next array to compare right and left array
    while idx_left < len(left):
        arr[idx_input] = left[idx_left]
        idx_left += 1
        idx_input += 1
            # when left index is less than length of the left
            # +1 each index except right
    while idx_right < len(right):
        arr[idx_input] = right[idx_right]
        idx_right += 1
        idx_input += 1
            # when right index is less than length of the right
            # +1 each index except left

for i in f:
    numList = [int(n) for n in i.split(' ')]
    # split in each array
    length = int(numList[0]) # get length of the list
    sorted_result = numList[1:] # number of list of the sorted 

    mergeSort(sorted_result, length)
    # merge all sort
    fout = open("merge.txt", "a")
    fout.write(' '.join(str(i) for i in sorted_result))
    # get file open and get value in format on merge.txt
    fout.write('\n')
    fout.close()
