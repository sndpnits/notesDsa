# problem statement: find the water trapped between buildings of given heights in array
# eg: i/p= 3 0 0 2 0 4 o/p = 10
# explanation:
#             |
#        |    |
#        |  | |
#        |  | |
#        033130
def VolOfTrappedWater(arr, n):
    maxL = []
    maxR = []

    # initiate with 0
    for i in range(n):
        maxL.append(0)
        maxR.append(0)

    # prepare the maxL (greatest element to left), maxR (greatest element to the right)
    maxL[0] = arr[0]
    maxR[n-1] = arr[n-1]
    for j in range(1, n):
        if arr[j] > maxL[j-1]:
            maxL[j] = arr[j]
        else:
            maxL[j] = maxL[j-1]

    for i in reversed(range(0, n-1)):
        if arr[i] > maxR[i+1]:
            maxR[i] = arr[i]
        else:
            maxR[i] = maxR[i+1]
    water = 0
    for i in range(n):
        water += min(maxR[i], maxL[i]) - arr[i]

    return water

