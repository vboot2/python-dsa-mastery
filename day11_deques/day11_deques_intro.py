"""
Day 11: Deques (Double-Ended Queues)

Deques are double-ended queues that allow fast 
append and pop operations from both ends.
"""

from collections import deque

# Example 1: Basic deque operations
dq = deque()

dq.append(1)         # add to right
dq.append(2)
dq.appendleft(0)     # add to left
print("Deque after appends:", dq)

dq.pop()             # remove from right
print("After pop:", dq)

dq.popleft()         # remove from left
print("After popleft:", dq)

# Example 2: Rotating a deque
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)  # shift right by 2
print("Rotated right by 2:", dq)

dq.rotate(-3)  # shift left by 3
print("Rotated left by 3:", dq)

# Example 3: Using deque as a sliding window
nums = [1, 3, 5, 2, 8, 6]
k = 3
dq = deque()
window_sums = []

for i in range(len(nums)):
    dq.append(nums[i])
    if len(dq) > k:
        dq.popleft()
    if len(dq) == k:
        window_sums.append(sum(dq))

print("Sliding window sums:", window_sums)
