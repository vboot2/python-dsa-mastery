""" Day 111: Linked List
Linked Lists store elements as nodes connected via pointers, enabling efficient insertions/deletions without shifting elements.
"""

# Example 1: Traverse a linked list and collect values
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def _to_pylist(head):
    """Helper: convert a linked list to a regular Python list."""
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals


def example_one():
    """
    Traverse linked list using a pointer.
    Time: O(n)
    """
    head = ListNode(1, ListNode(2, ListNode(3)))
    return _to_pylist(head)


print("Output Example 1:", example_one())


# Example 2: Remove nodes with a target value and show before/after lists
def example_two():
    """
    Use a dummy node to simplify deletions.
    Prints the list before and after removing `target`.
    Returns the final list as a Python list.
    """
    # Build the initial list: 1 → 2 → 6 → 3
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3))))
    target = 6

    # Show the list before any modifications
    print("Before removal:", _to_pylist(head))

    # Dummy node technique makes edge‑case deletions easy
    dummy = ListNode(0, head)
    curr = dummy

    while curr.next:
        if curr.next.val == target:
            # Skip the node containing the target value
            curr.next = curr.next.next
        else:
            curr = curr.next

    # `dummy.next` is the new head after deletions
    new_head = dummy.next

    # Show the list after the removal
    print("After removal :", _to_pylist(new_head))

    # Return the final list for further use
    return _to_pylist(new_head)


print("Output Example 2:", example_two())
