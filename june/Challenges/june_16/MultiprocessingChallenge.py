import time
from multiprocessing import Pool


def calculate_sum(n):
    return sum(i**2 for i in range(n))


if __name__ == "__main__":
    numbers = [5_000_000, 6_000_000, 7_000_000, 8_000_000]

    start = time.time()
    results = [calculate_sum(n) for n in numbers]
    sequential_time = time.time() - start
    print(f"Sequential: {sequential_time:.4f}s")
    print(results)

    start = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(calculate_sum, numbers)
    parallel_time = time.time() - start
    print(f"Parallel: {parallel_time:.4f}s")
    print(results)

    speedup = sequential_time / parallel_time
    print(f"Speedup: {speedup:.2f}x faster")
