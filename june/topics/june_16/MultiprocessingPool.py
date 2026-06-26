import time
from multiprocessing import Pool


def square(n):
    return n**2


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    # Without pool - sequential
    start = time.time()
    results = [square(n) for n in numbers]
    print(f"Sequential: {time.time() - start:.4f}s")
    print(results)

    # With pool - parallel
    start = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    print(f"Parallel: {time.time() - start:.4f}s")
    print(results)
