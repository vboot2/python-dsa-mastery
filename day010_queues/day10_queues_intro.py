"""
Day 10: Queues Intro

A Queue is a linear data structure that follows the
FIFO (First In, First Out) principle.
"""

# Example 1: Using collections.deque as a Queue
from collections import deque

queue = deque()

# Enqueue (add elements to the right)
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue after enqueuing A, B, C:", queue)

# Dequeue (remove elements from the left)
print("Dequeued:", queue.popleft())
print("Queue now:", queue)

# Peek (front element without removing)
print("Front of queue:", queue[0])

# Example 2: Using queue.Queue
from queue import Queue

q = Queue(maxsize=3)

# Enqueue
q.put(10)
q.put(20)
q.put(30)
print("Is queue full?", q.full())

# Dequeue
print("Dequeued:", q.get())
print("Queue size after one dequeue:", q.qsize())

# Check empty/full
print("Is queue empty?", q.empty())
print("Is queue full?", q.full())
