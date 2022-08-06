

# if array is sorted we can make use of it
# at any index we can get to know how many numbers are missing
def kthSmallestMissingNumber(A, K):
        A = list(set(A))
        A.sort()
        low = 0
        high = len(A) - 1
        K = K - 1  # considering zero removing 1
        while low <= high:
            mid = (low + high) // 2  # middle point - pivot
            missingK = A[mid] - mid
            if missingK > K:
                # print(missingK, mid, high)
                high = mid - 1
                # go right side
            else:
                low = mid + 1  # go left side

        return low + K

print(kthSmallestMissingNumber([1,3,3], 5))