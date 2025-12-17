"""
Day 71: Design Patterns (Advanced) - LeetCode Solutions
"""

# ---------------------------------------------------------
# Problem 1: TimeMap (LeetCode 981)
# Link: https://leetcode.com/problems/time-based-key-value-store/
# ---------------------------------------------------------
from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.store = {}  # key: list[(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        # Use binary search
        i = bisect_right(arr, (timestamp, chr(127))) - 1
        return arr[i][1] if i >= 0 else ""


# ---------------------------------------------------------
# Problem 2: RandomizedSet (LeetCode 380)
# Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
# ---------------------------------------------------------
import random


class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.pos = {}

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


# ---------------------------------------------------------
# Problem 3: LFU Cache (LeetCode 460)
# Link: https://leetcode.com/problems/lfu-cache/
# ---------------------------------------------------------
from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.key_to_val_freq = {}  # key: (value, freq)
        self.freq_to_keys = defaultdict(OrderedDict)

    def _update_freq(self, key):
        val, freq = self.key_to_val_freq[key]

        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.minFreq:
                self.minFreq += 1

        self.freq_to_keys[freq + 1][key] = True
        self.key_to_val_freq[key] = (val, freq + 1)

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update_freq(key)
            return

        if len(self.key_to_val_freq) == self.capacity:
            # evict LFU key
            freq = self.minFreq
            key_to_evict, _ = self.freq_to_keys[freq].popitem(last=False)
            if not self.freq_to_keys[freq]:
                del self.freq_to_keys[freq]
            del self.key_to_val_freq[key_to_evict]

        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = True
        self.minFreq = 1


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    # TimeMap test
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))
    print(tm.get("foo", 3))

    # RandomizedSet test
    rs = RandomizedSet()
    rs.insert(1)
    rs.insert(2)
    rs.remove(1)
    print(rs.getRandom())

    # LFU Cache test
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(lfu.get(1))  # increases frequency of 1
    lfu.put(3, 3)  # evicts key 2
    print(lfu.get(2))  # -1
    print(lfu.get(3))  # 3
