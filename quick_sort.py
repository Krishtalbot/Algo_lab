import random
import time
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def calc_time(arr):
    start_time = time.perf_counter()
    quick_sort(arr.copy(), 0, len(arr) - 1)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time

def main():
    sizes = [10, 50, 100, 200, 300, 400, 500, 1000]
    times_random = []
    times_asc = []
    times_desc = []

    for size in sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        asc_arr = sorted(arr)
        desc_arr = sorted(arr, reverse=True)

        times_random.append(calc_time(arr))
        times_asc.append(calc_time(asc_arr))
        times_desc.append(calc_time(desc_arr))

    print("Execution times for random arrays:", times_random)
    print("Execution times for ascending arrays:", times_asc)
    print("Execution times for descending arrays:", times_desc)

    plt.plot(sizes, times_random, label='Random')
    plt.plot(sizes, times_asc, label='Ascending')
    plt.plot(sizes, times_desc, label='Descending')
    
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Quick Sort Execution Time')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
