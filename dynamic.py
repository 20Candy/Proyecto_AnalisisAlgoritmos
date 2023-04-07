from sys import maxsize
 
 
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
 
arr = [2, 3, 4, 5, 7]
print ("Maximum contiguous sum is", maxSubArraySum(arr, len(arr)))
 