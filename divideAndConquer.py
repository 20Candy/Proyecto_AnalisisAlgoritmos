import time

# Fuente: https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/

# ----- maxCrossingSum -----
# Este algoritmo se encarga de encontrar la suma máxima de un subarreglo que cruza el punto medio de un arreglo dado.

def maxCrossingSum(arr, l, m, h): 
    sumaIzquierda = int(-1e9)
    sumaDerecha = int(-1e9)
    sumaTemporal = 0
 
    for i in range(m, l-1, -1):
        sumaTemporal += arr[i]

        if (sumaTemporal > sumaIzquierda):
            sumaIzquierda = sumaTemporal

    sumaTemporal = 0
    for i in range(m, h + 1):
        sumaTemporal = sumaTemporal + arr[i]

        if (sumaTemporal > sumaDerecha):
            sumaDerecha = sumaTemporal

    return max(sumaIzquierda + sumaDerecha - arr[m], sumaIzquierda, sumaDerecha)


# ----- maxSubArraySum -----
# Este algoritmo se encarga de encontrar la suma máxima de un subarreglo en un arreglo dado. 
# Implementa el acercamiento de Divide and Conquer.

def maxSubArraySum(arr, l, h):
    if (l > h):
        return int(-1e9)
    if (l == h):
        return arr[l]
 
    m = (l + h) // 2

    izquierda = maxSubArraySum(arr, l, m-1)
    derecha = maxSubArraySum(arr, m+1, h)
    cruzada = maxCrossingSum(arr, l, m, h)

    return max(izquierda, derecha, cruzada)


# arr = [2, 3, 4, 5, 7]

# start_time = time.time()
# max_sum = maxSubArraySum(arr, 0, len(arr)-1)
# end_time = time.time()
# print("Respuesta DaC:", max_sum, "Tiempo:", end_time - start_time)



     
 