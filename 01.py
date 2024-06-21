import time

def get_first(data):
    return data[3]

if __name__ == "__main__":
    data = [1, 2, 6, 8, 9, 5]
    start_time = time.perf_counter()
    a = get_first(data)
    end_time = time.perf_counter()

    execution_time = end_time - start_time
    print(a)
    print(f"Execution time: {execution_time:.10f} seconds")