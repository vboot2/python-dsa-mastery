"""
Day 14: Stack, Queue, LinkedList, Set

These four are fundamental data structures often built on top of arrays or pointers.

- Stack → LIFO (Last In First Out)
- Queue → FIFO (First In First Out)
- LinkedList → Nodes connected via pointers
- Set → Collection of unique items
"""

# -------------------------------
# Example 1: Stack (using list)
# -------------------------------
stack = []
stack.append(10)   # push
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)
stack.pop()        # pop
print("Stack after pop:", stack)

# -------------------------------
# Example 2: Queue (using deque)
# -------------------------------
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueues:", queue)
queue.popleft()  # dequeue
print("Queue after one dequeue:", queue)

# -------------------------------
# Example 3: Linked List (basic implementation)
# -------------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr, values = self.head, []
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values

ll = LinkedList()
ll.append(5)
ll.append(10)
ll.append(15)
print("LinkedList contents:", ll.display())

# -------------------------------
# Example 4: Set
# -------------------------------
unique_vals = {1, 2, 3, 3, 2}
print("Unique values in set:", unique_vals)
print("Check membership (2 in set?):", 2 in unique_vals)

# -------------------------------
# Example 5: Stack using deque (efficient)
# -------------------------------
stack2 = deque()
stack2.append("A")
stack2.append("B")
stack2.append("C")
print("Stack2:", stack2)
stack2.pop()
print("Stack2 after pop:", stack2)

# -------------------------------
# Example 6: Queue as FIFO buffer
# -------------------------------
buffer = deque(maxlen=3)  # fixed size queue
for i in range(5):
    buffer.append(i)
    print("Buffer state:", buffer)
