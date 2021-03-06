# problem statement
# find the next smaller element to left of the array
# eg: i/p = 4 8 5 2 25  o/p= 2 5 2 -1 -1

# looks similar to NSR just reverse the loop

# ====================================================================================================================
# for each element you take from i/p, check in stack with following conditions
# if stack is empty that means there is no smaller element to the left add -1 to result and push the current
# element to stack
# if stack is not empty check if the top element is smaller than current element
# if yes then push top into result and push element into stack, if no then keep popping until you get a smaller element
# if you don't get a smaller element push -1 to result otherwise push the top element to result and at the end push the
# current element to stack
# ====================================================================================================================
from collections import deque


def nearestSmallerElementToLeft(arr, n):
    res = []

    # initialize the result array to be -1
    for i in range(n):
        res.append(-1)

    # create a stack with deque
    dq = deque()

    # start from the first element of the array
    # for each element you take from i/p, check in stack with following conditions
    for j in range(n):
        # to check dq is empty
        if not dq:
            dq.append(arr[j])
        # dq[-1] gives you the top of the element
        elif dq and dq[-1] < arr[j]:
            res[j] = dq[-1]
            dq.append(arr[j])
        else:
            while dq and dq[-1] > arr[j]:
                dq.pop()
            if dq:
                res[j] = dq[-1]

            dq.append(arr[j])
    return res


# gives the index of nearest smaller element
def nearestLeftSmallerElementIndex(arr, n):
    idx = []
    # initialize the result array to be -1, we are going left so last index in left could be -1
    for i in range(n):
        idx.append(-1)

    # create a stack with deque
    dq = deque()

    # start from the first element of the array
    # for each element you take from i/p, check in stack with following conditions
    #  pushing the index and while popping, check the array value at the index

    for j in range(n):
        # to check dq is empty
        if not dq:
            dq.append(j)
        # dq[-1] gives you the top of the element
        elif dq and arr[dq[-1]] < arr[j]:
            idx[j] = dq[-1]
            dq.append(j)
        else:
            while dq and arr[dq[-1]] >= arr[j]:
                dq.pop()
            if dq:
                idx[j] = dq[-1]

            dq.append(j)
    return idx


# print(nearestLeftSmallerElementIndex([5, 2, 3, 1, 10, 3, 12], 7))