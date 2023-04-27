import time
import sys

# Fuente: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

# ----- findMaxSubarraySum -----
# Este primer algoritmo es la base para la creación del algoritmo definido por Kadane. 

# def findMaxSubarraySum(x):
    # n = len(x)
    # sumaMaximaFinal = [0] * n
    # sumaMaximaFinal[0] = x[0]

    # for i in range(1, n):
    #     if sumaMaximaFinal[i-1] > 0:
    #         sumaMaximaFinal[i] = x[i] + sumaMaximaFinal[i-1]
    #     else:
    #         sumaMaximaFinal[i] = x[i]

    # sumaMaximaSubmatriz = -sys.maxsize

    # for i in range(n):
    #     sumaMaximaSubmatriz = max(sumaMaximaSubmatriz, sumaMaximaFinal[i])

    # return sumaMaximaSubmatriz

# ----- maxSubarraySum -----
# Esta es nuestra implementación del algoritmo de Kadane. 
# Esto implementa el acercamiento de Dynamic Programming.

def maxSubArraySum(a):
    n = len(a)
    sumaMaximaHastaAhora = -sys.maxsize - 1
    sumaMaximaFinal = 0

    for i in range(n):
        sumaMaximaFinal += a[i]
        if sumaMaximaHastaAhora < sumaMaximaFinal:
            sumaMaximaHastaAhora = sumaMaximaFinal

        if sumaMaximaFinal < 0:
            sumaMaximaFinal = 0

    return sumaMaximaHastaAhora

# arr = [2, 3, 4, 5, 7]

# startTime = time.time()
# max_sum = maxSubArraySum(arr)
# endTime = time.time()
# print("\nRespuesta DP:", max_sum, "Tiempo:", startTime - endTime)