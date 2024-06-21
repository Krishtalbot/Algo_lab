import time, random
import matplotlib.pyplot as plt

def heap_permutation(data, n):
    if n ==1:
        print(data)
        return
    
    for i in range(n):
        heap_permutation(data, n-1)
        if n%2 ==0:
            data[i], data[n-1] = data[n-1], data[i]

        else:
            data[0], data[n-1] = data[n-1], data[0]

def measure_time(arr, n):
    arr.sort()
    start_time = time.perf_counter()
    heap_permutation(arr, n)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    array_sizes = [1, 2, 3, 4, 5, 6, 7]
    execution_times = []

    for size in array_sizes:
        arr = [random.randint(0, 5) for _ in range(size)]
        execution_time = measure_time(arr, len(arr))
        execution_times.append(execution_time)
        print(f"Array size: {size}, Execution time: {execution_time:.10f} seconds")

    plt.plot(array_sizes, execution_times, marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Heap Permutation vs Array Size')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()