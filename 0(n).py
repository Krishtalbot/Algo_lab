import time
import random
import matplotlib.pyplot as plt

def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return 1 
    return -1

def measure_time(arr, target):
    arr.sort()
    start_time = time.perf_counter()
    search(arr, target)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    array_sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
    execution_times = []

    for size in array_sizes:
        arr = [random.randint(1, 100) for _ in range(size)]
        target = 100
        execution_time = measure_time(arr, target)
        execution_times.append(execution_time)
        print(f"Array size: {size}, Execution time: {execution_time:.10f} seconds")

    plt.plot(array_sizes, execution_times, marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Linear Search Execution Time vs Array Size')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
