"""
Day 71: Design Patterns (Advanced)

Data structure design:
1. Time-based key-value store with binary search
2. RandomizedSet with O(1) insert/delete/getRandom
3. LFU Cache using min-frequency tracking and LinkedHashSets
"""

# -------------------------------------------------------
# Example 1: TimeMap (Time-Based Key-Value Store)
# -------------------------------------------------------
from bisect import bisect_right


class ExampleTimeMap:
    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        i = bisect_right(arr, (timestamp, chr(127))) - 1
        return arr[i][1] if i >= 0 else ""


# -------------------------------------------------------
# Example 2: RandomizedSet
# -------------------------------------------------------
import random


class ExampleRandomizedSet:
    def __init__(self):
        self.arr = []
        self.pos = {}  # value -> index

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.arr[-1]
        self.arr[idx] = last
        self.pos[last] = idx
        self.arr.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# -------------------------------------------------------
# Example 3: LFU Cache Core Idea
# -------------------------------------------------------
# NOTE: Actual implementation done in practice file.
# Showing core structure here.


class ExampleLFUCache:
    """
    Structure overview:
    - key_to_val_freq: {key: (value, freq)}
    - freq_to_keys: {freq: OrderedDict or LinkedHashSet of keys}
    - track minFreq for O(1) eviction
    """
