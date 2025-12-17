""" 
Day 96: Linked List / Array  
Linked lists allow node-based dynamic structures, while arrays offer contiguous memory and fast random access.
"""

# Example 1: Reverse a linked list (classic operation)
def example_one():
    """
    Reverse a singly linked list using iterative pointers.
    - prev tracks reversed portion
    - curr iterates through list
    """
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    # Create 1 -> 2 -> 3
    head = Node(1, Node(2, Node(3)))

    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Collect reversed list for display
    result = []
    while prev:
        result.append(prev.val)
        prev = prev.next

    return result

print("Output Example 1:", example_one())


# Example 2: Two-pointer technique on arrays
def example_two():
    """
    Demonstrate two-pointer approach:
    - Move left/right to find pair sum target
    """
    nums = [1, 2, 3, 4, 6]
    target = 7
    l, r = 0, len(nums) - 1

    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return (nums[l], nums[r])
        elif s < target:
            l += 1
        else:
            r -= 1

    return None

print("Output Example 2:", example_two())
