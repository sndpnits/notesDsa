from stack.base.NSL import nearestLeftSmallerElementIndex
from stack.base.NSR import nearestRightSmallerElementIndex
#


# Algorithm: find the index of Next smaller element to right and Nearest smaller element index from left
# take the difference and calculate the area


# get the area of histograms and return the max one
def maxAreaHistogram(arr, n):
    left_idx = nearestLeftSmallerElementIndex(arr, n)
    right_idx = nearestRightSmallerElementIndex(arr, n)
    print(left_idx)
    print(right_idx)
    print
    max_area = 0

    for i in range(n):
        no_of_histogram = right_idx[i] - left_idx[i] - 1
        area_of_histogram = arr[i] * no_of_histogram
        if max_area < area_of_histogram:
            max_area = area_of_histogram

    return max_area


print(maxAreaHistogram([9, 10, 4, 10, 4, 5, 16], 7))
