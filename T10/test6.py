from memory_profiler import profile
import random

@profile
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = sorted(random.sample(range(1, 10_000_001), 10_000_000))
    target = arr[-1]
    result = linear_search(arr, target)
    print("Результат поиска:", result)
