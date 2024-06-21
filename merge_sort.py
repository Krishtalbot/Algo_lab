import random
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def calc_time(arr):
    start_time = time.perf_counter()
    merge_sort(arr.copy())
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
    plt.title('Merge Sort Execution Time')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
