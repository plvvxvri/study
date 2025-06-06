from memory_profiler import profile
import random

@profile
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = sorted(random.sample(range(1, 10_000_001), 10_000_000))
    target = arr[-1]
    result = binary_search(arr, target)
    print("Результат поиска:", result)
