"""
Day 70: Design Patterns (Cache) - LeetCode Problem Solutions
"""


# ---------------------------------------------------------
# Problem 1: LRU Cache (LeetCode 146, Medium)
# Link: https://leetcode.com/problems/lru-cache/
# ---------------------------------------------------------
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# ---------------------------------------------------------
# Problem 2: Design HashSet (LeetCode 705, Easy)
# Link: https://leetcode.com/problems/design-hashset/
# ---------------------------------------------------------
class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        h = self._hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key: int) -> bool:
        h = self._hash(key)
        return key in self.buckets[h]


# ---------------------------------------------------------
# Problem 3: Design HashMap (LeetCode 706, Easy)
# Link: https://leetcode.com/problems/design-hashmap/
# ---------------------------------------------------------
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)
        for pair in self.buckets[h]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[h].append([key, value])

    def get(self, key: int) -> int:
        h = self._hash(key)
        for pair in self.buckets[h]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        for i, pair in enumerate(self.buckets[h]):
            if pair[0] == key:
                self.buckets[h].pop(i)
                return


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Testing LRU Cache:")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # returns 1
    cache.put(3, 3)
    print(cache.get(2))  # returns -1

    print("\nTesting MyHashSet:")
    hs = MyHashSet()
    hs.add(1)
    hs.add(2)
    print(hs.contains(1), hs.contains(3))

    print("\nTesting MyHashMap:")
    hm = MyHashMap()
    hm.put(1, 2)
    hm.put(2, 3)
    print(hm.get(1))
    hm.remove(1)
    print(hm.get(1))
