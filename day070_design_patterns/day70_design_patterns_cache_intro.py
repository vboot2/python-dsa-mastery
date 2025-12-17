"""
Day 70: Design Patterns (Cache)

Common cache design patterns:
- LRU Cache → Ordered HashMap + Double Linked List
- HashSet → Basic hashing with chaining/bucketing
- HashMap → Custom key-value mapping
"""


# -------------------------------------------------------
# Example 1: Simple LRU Cache Implementation
# -------------------------------------------------------
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key → node
        # dummy head and tail
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
            # remove from the least recently used side (left)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


print("Example 1 (LRUCache):")
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1
cache.put(3, 3)  # evicts key 2
print(cache.get(2))  # returns -1


# -------------------------------------------------------
# Example 2: Simple HashSet Design
# -------------------------------------------------------
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


print("Example 2 (MyHashSet):")
s = MyHashSet()
s.add(1)
s.add(2)
print(s.contains(1), s.contains(3))


# -------------------------------------------------------
# Example 3: Simple HashMap Design
# -------------------------------------------------------
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


print("Example 3 (MyHashMap):")
m = MyHashMap()
m.put(1, 2)
print(m.get(1))
m.put(2, 3)
m.remove(1)
print(m.get(1))
