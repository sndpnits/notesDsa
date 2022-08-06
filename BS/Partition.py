

# in this method i will check if the partition is good enough for k painters
def isValid(arr, n, k, max_partition):
    cnt = 1
    sumup = 0
    for i in arr:
        sumup += i
        if sumup > max_partition:
            cnt += 1
            sumup = i

    if cnt > k:
        return False
    return True

# Sandeep wants to paint his dog's home that has n boards
# with different lengths. The length of ith board is given by arr[i]
# where arr[] is an array of n integers. He hired k painters for this work
# and each painter takes 1 unit time to paint 1 unit of the board.

# The problem is to find the minimum time to get this job done
# if all painters start together with the constraint that any painter will only paint
# continuous boards, say boards numbered {2,3,4} or only board {1} or nothing but not boards {2,4,5}.

# taking the sum of elements and BS will be applied to find the optimum job to be given to each painter
def minTime(arr, n, k):
    # code here
    high = sum(arr)
    low = max(arr)

    result = -1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if isValid(arr, n, k, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


