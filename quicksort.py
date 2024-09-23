import random
import time

def quicksort(arr):
    """
    Sorts an array using the deterministic Quicksort algorithm.

    Parameters:
        arr (list): The list of elements to sort.

    Returns:
        list: A new sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 1/2 = Middle = pivot
    left = [x for x in arr if x < pivot]  # Elements < pivot
    middle = [x for x in arr if x == pivot]  # Elements = pivot
    right = [x for x in arr if x > pivot]  # Elements > pivot
    return quicksort(left) + middle + quicksort(right)

def randomized_quicksort(arr):
    """
    Sorts an array using the randomized Quicksort algorithm.

    Parameters:
        arr (list): The list of elements to sort.

    Returns:
        list: A new sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)  # Random = pivot
    pivot = arr[pivot_index] # Set = pivot
    left = [x for x in arr if x < pivot]  # Elements < pivot
    middle = [x for x in arr if x == pivot]  # Elements = pivot
    right = [x for x in arr if x > pivot]  # Elements > pivot
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

def performance_analysis(sort_function, arr):
    """
    Analyzes the performance of a sorting function.

    Parameters:
        sort_function (function): The sorting function to analyze.
        arr (list): The list of elements to sort.

    Returns:
        float: The time taken to sort the array.
    """
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    # Testing the deterministic quicksort
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quicksort(sample_array)
    print("Sorted array (deterministic):", sorted_array)

    # Testing the randomized quicksort
    sorted_array_randomized = randomized_quicksort(sample_array)
    print("Sorted array (randomized):", sorted_array_randomized)

    # Testing  Performance
    random_array = [random.randint(1, 1000) for _ in range(1000)]
    deterministic_time = performance_analysis(quicksort, random_array.copy())
    randomized_time = performance_analysis(randomized_quicksort, random_array.copy())
    print(f"Deterministic Quicksort time: {deterministic_time:.6f} seconds")
    print(f"Randomized Quicksort time: {randomized_time:.6f} seconds")
