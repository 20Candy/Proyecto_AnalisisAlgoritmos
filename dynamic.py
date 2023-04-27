import time
import sys

def findMaxSubarraySum(x):
    n = len(x)
    maxSumEnding = [0] * n
    maxSumEnding[0] = x[0]

    for i in range(1, n):
        if maxSumEnding[i-1] > 0:
            maxSumEnding[i] = x[i] + maxSumEnding[i-1]
        else:
            maxSumEnding[i] = x[i]

    maxSubarraySum = -sys.maxsize
    for i in range(n):
        maxSubarraySum = max(maxSubarraySum, maxSumEnding[i])

    return maxSubarraySum

# arr = [2, 3, 4, 5, 7]
# print("Maximum contiguous sum is", findMaxSubarraySum(arr))

def maxSubArraySum(a):
    n = len(a)
    maxSoFar = -sys.maxsize - 1
    maxEndingHere = 0

    for i in range(n):
        maxEndingHere += a[i]
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere

        if maxEndingHere < 0:
            maxEndingHere = 0

    return maxSoFar

# arr = [8, 4, 7, 5, 1, 0, 6, 2, 9, 3, 2, 1, 4, 5]
# startTime = time.time()
# print("Maximum contiguous sum is", maxSubarraySum(arr))
# endTime = time.time()

# totalTime = (endTime - startTime) * 1000
# print("Total execution time: {:.10f}".format(totalTime))