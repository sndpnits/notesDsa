import heapq


# kth smallest number
# algo: keep on pushing the element to max heap and always check that it should not exceed the size of k.
# if it exceed pop the maximum number
# multiplication by -1 convert this min heap to max heap
def kthSmallestElement(arr, k):
    h = []
    for i in arr:
        heapq.heappush(h, i*-1)
        # print(h)
        if len(h) > k:
            heapq.heappop(h)

    return -1*heapq.heappop(h)


print(kthSmallestElement([7,6,5,4,3,2,1],3))