# problem statement
# method to get the next greater element from right side of each element
#  eg: i/p = 1,3,2,4 o/p = 3,4,4,-1
# res is the array that will keep the right greater element at respective index

# ====================================================================================================================
# for each element you take from i/p, check in stack with following conditions
# if stack is empty that means there is no greater element to the right add -1 to result and push the current
# element to stack
# if stack is not empty check if the top element is greater than current element
# if yes then push top into result and push element into stack, if no then keep popping until you get a greater element
# if you don't get a greater element push -1 to result otherwise push the top element to result and at the end push the
# current element to stack
# ====================================================================================================================
from collections import deque


def nextLargerElementToRight(arr, n):
    res = []

    # initialize the result array to be -1
    for i in range(n):
        res.append(-1)

    # create a stack with deque
    dq = deque()

    # start from the end of the array
    # for each element you take from i/p, check in stack with following conditions
    for j in reversed(range(n)):
        # to check dq is empty
        if not dq:
            dq.append(arr[j])
        # dq[-1] gives you the top of the element
        elif dq and dq[-1] > arr[j]:
            res[j] = dq[-1]
            dq.append(arr[j])
        else:
            while dq and dq[-1] <= arr[j]:
                dq.pop()
            if dq:
                res[j] = dq[-1]

            dq.append(arr[j])
    return res


print(nextLargerElementToRight([16, 5, 4, 4, 4, 10, 9], 7))
