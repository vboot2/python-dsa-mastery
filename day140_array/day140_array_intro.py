"""Day 140: Array
Advanced array manipulation using sorting,
greedy placement, prefix logic, divide & conquer,
and spatial hashing techniques.
"""


# Example 1: Queue reconstruction using sorting
def example_one():
    """
    Sort by height descending, then insert by index.
    """
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    people.sort(key=lambda x: (-x[0], x[1]))

    queue = []
    for p in people:
        queue.insert(p[1], p)

    return queue


print("Output Example 1:", example_one())


# Example 2: Count duplicates using set
def example_two():
    """
    Track seen values to detect duplicates.
    """
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    seen = set()
    dup = []

    for n in nums:
        if n in seen:
            dup.append(n)
        seen.add(n)

    return dup


print("Output Example 2:", example_two())
