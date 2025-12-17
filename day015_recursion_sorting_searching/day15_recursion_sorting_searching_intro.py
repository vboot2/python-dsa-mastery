"""
Day 15: Recursion, Sorting, Searching

Recursion is a technique where a function calls itself to break down problems.
Sorting and searching are fundamental algorithms to organize and find data efficiently.
"""

# -------------------------------
# Example 1: Factorial (classic recursion)
# -------------------------------
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# -------------------------------
# Example 2: Binary Search (recursive)
# -------------------------------
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

arr = [1, 3, 5, 7, 9, 11]
print("Binary search for 7:", binary_search(arr, 7, 0, len(arr) - 1))


# -------------------------------
# Example 3: Merge Sort
# -------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

print("Merge sort [5,2,4,6,1,3]:", merge_sort([5,2,4,6,1,3]))


# -------------------------------
# Example 4: Quick Sort
# -------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print("Quick sort [3,6,8,10,1,2,1]:", quick_sort([3,6,8,10,1,2,1]))
