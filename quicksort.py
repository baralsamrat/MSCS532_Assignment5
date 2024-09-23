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
    pivot = arr[len(arr) // 2]  # Middle = pivot
    left = [x for x in arr if x < pivot]  # Elements < pivot
    middle = [x for x in arr if x == pivot]  # Elements = pivot
    right = [x for x in arr if x > pivot]  # Elements > pivot
    return quicksort(left) + middle + quicksort(right)

def randomized_quicksort(arr):
    """
    Sorts an array using the randomized Quicksort algorithm.
    """

def performance_analysis(sort_function, arr):
    """
    Analyzes the performance of a sorting function.
    """

if __name__ == "__main__":
    # Testing the deterministic quicksort
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quicksort(sample_array)
    print("Sorted array (deterministic):", sorted_array)

    # Testing the randomized quicksort
    # Testing  Performance

