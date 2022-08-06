
def countZeroes( n):
    # code here
    low = 1

    high = 1e6
    result = 0
    while low <= high:
        mid = int(low + (high - low) / 2)
        trail_zeroes = trailingZeroes(mid)
        if trail_zeroes == n:
            result = 5
            high = mid - 1
        elif trail_zeroes < n:
            low = mid + 1
        else:
            high = mid - 1
    return result


# n is the number of trailing zeroes, cnt is the number which factorial gives at least n number of trailing zeroes
def trailingZeroes(n):
    cnt = 0
    while n > 0:
        n = int(n / 5)
        cnt += n
    return cnt


def firstAndLast(self, arr, n, x):
    # Code here
    low = 0
    high = n
    first = last = -1
    while low <= high:
        mid = int(low + (high - low) / 2)

        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    if first == -1:
        return [-1]
    while low <= high:
        mid = int(low + (high - low) / 2)

        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return [first, last]