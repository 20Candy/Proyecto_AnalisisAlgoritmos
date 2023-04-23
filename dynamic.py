import time
from sys import maxsize
 
# dinamico
def findMaxSubarraySum(X,n):
    maxSumEnding = [0]*n
    maxSumEnding[0] = X[0]

    for i in range(1,n):
        if maxSumEnding[i-1] > 0:
            maxSumEnding[i] = X[i] + maxSumEnding[i-1]
        else:
            maxSumEnding[i] = X[i]

    maxSubarraySum = -maxsize
    for i in range(n):
        maxSubarraySum = max(maxSubarraySum, maxSumEnding[i])

    return maxSubarraySum

# arr = [2, 3, 4, 5, 7]
# print ("Maximum contiguous sum is", findMaxSubarraySum(arr, len(arr)))

# Kadane’s Algorithm
def maxSubArraySum(a, size):
 
    max_so_far = -maxsize - 1
    max_ending_here = 0
 
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
 
# arr = [8, 4, 7, 5, 1, 0, 6, 2, 9, 3, 2, 1, 4, 5]
# start_time = time.time()
# print ("Maximum contiguous sum is", maxSubArraySum(arr, len(arr)))
# end_time = time.time()

# total_time = (end_time - start_time)*1000

# print("Tiempo total de ejecución: {:.10f}".format(total_time))

     