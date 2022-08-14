import heapq
def getKLargestElement(arr,k):
    h = []
    for i in arr:
        heapq.heappush(h, i)
        if len(h)>k:
            heapq.heappop(h)

    return h

print(getKLargestElement([10,4,5,6,3,9,7],3))