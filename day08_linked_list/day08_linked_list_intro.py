"""
Day 08: Linked Lists

A linked list is a linear data structure where each element (node) contains:
- data
- pointer to next node

Variants:
- Singly Linked List
- Doubly Linked List
- Circular Linked List
"""

# Simple Node class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example: Build linked list 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Traverse
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")
