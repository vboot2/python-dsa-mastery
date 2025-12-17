"""
Day 09: Stacks - Introduction
Demonstrating basic stack operations in Python
"""

# Using list as a stack
stack = []
print("Using list as stack:")
stack.append(1)   # push
stack.append(2)
print("Stack after pushes:", stack)
print("Pop element:", stack.pop())  # 2
print("Stack now:", stack)

# Using collections.deque as a stack
from collections import deque
stack_deque = deque()
print("\nUsing deque as stack:")
stack_deque.append(10)
stack_deque.append(20)
print("Stack after pushes:", list(stack_deque))
print("Pop element:", stack_deque.pop())  # 20
print("Stack now:", list(stack_deque))
