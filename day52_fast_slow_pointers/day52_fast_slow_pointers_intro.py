"""
Day 52: Fast & Slow Pointers
The Fast and Slow Pointers technique is used to detect cycles, find middle nodes, and handle linked list traversal efficiently.
"""


# Example 1: Detect cycle in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def example_one(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Example 2: Find middle element of a linked list
def example_two(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val if slow else None


if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Output Example 1:", example_one(head))  # Expected: False
    print("Output Example 2:", example_two(head))  # Expected: 3
