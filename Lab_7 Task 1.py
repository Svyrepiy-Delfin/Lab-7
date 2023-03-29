#Боглачев Артём 367901
import random
import numpy as np
from time import perf_counter


# Task1
list1 = [random.randint(0, 100) for _ in range(1000000)]
list2 = [random.randint(0, 100) for _ in range(1000000)]

arr1 = np.random.randint(0, 100, 1000000)
arr2 = np.random.randint(0, 100, 1000000)

start = perf_counter()
list3 = [list1[i] * list2[i] for i in range(len(list1))]
end = perf_counter()
print(f"Время при перемножении списков: {end - start:.5f} секунд")

start = perf_counter()
arr3 = np.multiply(arr1, arr2)
end = perf_counter()
print(f"Время при перемножении с помощью numPy: {end - start:.5f} секунд")


