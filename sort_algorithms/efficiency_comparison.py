import timeit
import random
from insertion_sort import insertion_sort
from merge_sort import merge_sort


# generate different size lists
small_data = [random.randint(0, 1_000) for _ in range(1_000)]
medium_data = [random.randint(0, 10_000) for _ in range(10_000)]
large_data = [random.randint(0, 100_000) for _ in range(100_000)]


# universal time_algorithm helper
def time_algorithm(func, data, number=10):
    """Measure how long function takes using a fresh copy of data each run."""
    return timeit.timeit(lambda: func(data.copy()), number=number)


if __name__ == "__main__":
    results = {
        "Insertion Sort": [
            time_algorithm(insertion_sort, small_data),
            time_algorithm(insertion_sort, medium_data, 5),
            time_algorithm(insertion_sort, large_data, 1),
        ],
        "Merge Sort": [
            time_algorithm(merge_sort, small_data),
            time_algorithm(merge_sort, medium_data),
            time_algorithm(merge_sort, large_data),
        ],
        "Timsort": [
            time_algorithm(sorted, small_data),
            time_algorithm(sorted, medium_data),
            time_algorithm(sorted, large_data),
        ],
    }

    print(f"{'Algorithm':<20} {'Small':>10} {'Medium':>10} {'Large':>10}")
    for alg, times in results.items():
        row = f"{alg:<20}"
        for t in times:
            row += f" {t:>10.5f}"
        print(row)
