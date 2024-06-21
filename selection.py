import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def calc_time(arr):
    start_time = time.perf_counter()
    selection_sort(arr.copy())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time

def main():
    sizes = [10, 50, 100, 200, 300, 400, 500]
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
    
    print(times_random)
    print(times_asc)
    print(times_desc)


    plt.plot(sizes, times_random, label='Random')
    plt.plot(sizes, times_asc, label='Ascending')
    plt.plot(sizes, times_desc, label='Descending')
    
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Selection Sort Execution Time')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
