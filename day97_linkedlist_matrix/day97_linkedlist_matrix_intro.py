"""
Day 97: Linked List / Matrix  
Understanding how linked lists reorder, rotate, and how matrix rules help simulate cellular automata (Game of Life).
"""

# ---------------------------------------------------------
# Example 1: Insertion Sort on Linked List (concept only)
# ---------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def example_one():
    """
    Demonstrates concept of insertion-sort behavior on a linked list.
    """
    # create 3 -> 1 -> 2
    head = ListNode(3, ListNode(1, ListNode(2)))

    # Explanation-only demo: extract values, sort, return sorted list as Python list
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    vals.sort()
    return vals


print("Output Example 1:", example_one())

# ---------------------------------------------------------
# Example 2: Matrix update rule (e.g. Game of Life concept)
# ---------------------------------------------------------
def example_two():
    """
    Shows a simple matrix neighbor-count rule.
    """
    grid = [
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 0]
    ]
    rows, cols = len(grid), len(grid[0])
    live_neighbors_center = 0

    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]:
        nr, nc = 1 + dx, 1 + dy
        if 0 <= nr < rows and 0 <= nc < cols:
            live_neighbors_center += grid[nr][nc]

    return live_neighbors_center


print("Output Example 2:", example_two())
