
class BinarySearch:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def binSearch(self, item):
        start = 0
        end = self.n-1
        while start <= end:
            mid = int(start + (end-start)/2)

            if self.arr[mid] == item:
                return mid
            elif self.arr[mid] > item:
                end = mid-1
            else:
                start = mid+1
        return -1

    def binSearchWithIdx(self, i, j, item):
        start = i
        end = j-1
        while start <= end:
            mid = int((start+end)/2)
            if self.arr[mid] == item:
                return mid
            elif self.arr[mid] > item:
                end = mid-1
            else:
                start = mid+1
        return -1

    # given a sorted array, find first occurrence of given number
    def findFirstOccurrence(self, item):
        start = 0
        end = self.n - 1
        result = -1
        while start <= end:
            mid = int((start + end) / 2)
            if self.arr[mid] == item:
                result = mid
                end = mid-1
            elif self.arr[mid] > item:
                end = mid - 1
            else:
                start = mid + 1
        return result

    def findLastOccurrence(self, item):
        start = 0
        end = self.n - 1
        result = -1
        while start <= end:
            mid = int((start + end) / 2)
            if self.arr[mid] == item:
                result = mid
                start = mid+1
            elif self.arr[mid] > item:
                end = mid - 1
            else:
                start = mid + 1
        return result

    def getNumberOfOccurrences(self):
        return self.findLastOccurrence() - self.findFirstOccurrence() + 1

    # i/p = 11, 12, 15, 18, 2, 5, 6, 8   o/p = 4
    # how many times the array is rotated
    # index of the first minimum element will be the answer
    # find that element , pattern is min element has greater number both the sides
    #
    def getNumberOfRotation(self):
        start = 0
        end = self.n - 1
        result = -1
        while start <= end:
            mid = int((start + end) / 2)
            if self.arr[mid] < self.arr[mid+1] and self.arr[mid] < self.arr[mid-1]:
                return mid
            elif self.arr[mid] > self.arr[0]:
                start = mid + 1
            else:
                end = mid - 1
        return result

    # i/p = 11, 12, 15, 18, 2, 5, 6, 8  find 18 o/p = 3
    # get the pivot element using above function and run binary search on two arrays
    def findInRotatedArray(self, item):
        pivot_index = self.getNumberOfRotation()
        if item >= self.arr[0]:
            return self.binSearchWithIdx(0, pivot_index, item)
        else:
            return self.binSearchWithIdx(pivot_index, self.n, item)


bs = BinarySearch([10, 11, 12, 15, 18, 1, 2, 5, 6, 8])
print(bs.findInRotatedArray(18))
# self.(binSearch([1, 2, 3, 4, 5, 6, 7, 8], 8, 2))
