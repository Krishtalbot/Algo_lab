import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

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

def calc_time(sort_func, arr):
    start_time = time.perf_counter()
    
    if sort_func.__name__ == 'insertion_sort':
        sort_func(arr.copy())
    elif sort_func.__name__ == 'merge_sort':
        sort_func(arr.copy())
    elif sort_func.__name__ == 'quick_sort':
        sort_func(arr.copy(), 0, len(arr) - 1)
    else:
        sort_func(arr.copy())
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time

def main():
    sizes = [10, 50, 100, 200, 300, 400, 500]
    sort_functions = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Selection Sort": selection_sort
    }

    plt.figure(figsize=(10, 6))

    for name, sort_func in sort_functions.items():
        times_random = []
        times_asc = []
        times_desc = []

        for size in sizes:
            arr = [random.randint(1, 1000) for _ in range(size)]
            asc_arr = sorted(arr)
            desc_arr = sorted(arr, reverse=True)

            # Pass the sorting function and the array to calc_time
            times_random.append(calc_time(sort_func, arr))
            times_asc.append(calc_time(sort_func, asc_arr))
            times_desc.append(calc_time(sort_func, desc_arr))

        # plt.plot(sizes, times_random, label=f'{name} (Random)')
        plt.plot(sizes, times_asc, label=f'{name} (Ascending)')
        # plt.plot(sizes, times_desc, label=f'{name} (Descending)')

    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithm Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
