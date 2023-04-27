import time
import dynamic
import divideAndConquer
from random import randint
import matplotlib.pyplot as plt

size = []
times = [[], []]
arrays_used = []

arr = []
for i in range(5, 501, 1):

    # se le agregan números aleatorios al arreglo ya existente de tamaño i
    for j in range(i - len(arr) + 1):
        arr.append(randint(-100, 100))

    n = len(arr)
    size.append(n)

    print("----- Arreglo: ", arr)
    # se calcula el tiempo de ejecución de la función maxSubArraySum
    start_time = time.time()
    max_sum = divideAndConquer.maxSubArraySum(arr, 0, n-1)
    end_time = time.time()
    total_time = (end_time - start_time)
    times[0].append(total_time)

    print("Maximum contiguous sum is ", max_sum)
    print("Tiempo total de ejecución de DAC: {:.7f}".format(total_time))

    # se calcula el tiempo de ejecución de la función maxSubArraySum
    start_time = time.time()
    max_sum = dynamic.maxSubArraySum(arr)
    end_time = time.time()
    total_time = (end_time - start_time)
    times[1].append(total_time)

    print("\nMaximum contiguous sum is ", max_sum)
    print("Tiempo total de ejecución de Dynamic: {:.10f}".format(total_time))

    print("\n")
    arrays_used.append(arr.copy())

plt.plot(size, times[0], 'o', label="Divide and Conquer")
plt.plot(size, times[1], 'o', label="Dynamic Programming")
plt.xlabel("Tamaño del arreglo")
plt.ylabel("Tiempo de ejecución")
plt.title("Tiempo Ejecución: DAC vs. Dynamic Programming")
plt.legend()
plt.show()

plt.plot(size, times[0], 'o', label="Divide and Conquer")
plt.xlabel("Tamaño del arreglo")
plt.ylabel("Tiempo de ejecución")
plt.title("Tiempo Ejecución: DAC")
plt.legend()
plt.show()

plt.plot(size, times[1], 'o', label="Dynamic Programming")
plt.xlabel("Tamaño del arreglo")
plt.ylabel("Tiempo de ejecución")
plt.title("Tiempo Ejecución: Dynamic Programming")
plt.legend()
plt.show()

# create .txt that stores the arrays used and time taken by each algorithm
file = open("arrays_used.txt", "w")
for i in range(len(arrays_used)):
    file.write("---------------Array: " + str(arrays_used[i]) + "\n")
    file.write("DAC time: " + str(times[0][i]) + "\n")
    file.write("Dynamic time: " + str(times[1][i]) + "\n\n")