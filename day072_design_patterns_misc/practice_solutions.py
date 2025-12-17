"""
Day 72: Design Patterns (Misc) - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Kth Largest Element in a Stream (LeetCode 703, Easy)
# Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# ---------------------------------------------------------
import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)

        # Keep heap size = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # If heap smaller than k, just push
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            # replace smallest of the k largest
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


# ---------------------------------------------------------
# Problem 2: Design Twitter (LeetCode 355, Medium)
# Link: https://leetcode.com/problems/design-twitter/
# ---------------------------------------------------------
import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # user -> list of (time, tweetId)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        # user sees their own tweets
        users = set([userId])
        # user sees followed users' tweets
        users |= self.following[userId]

        for u in users:
            for ts, twid in self.tweets[u]:
                heapq.heappush(heap, (-ts, twid))

        res = []
        for _ in range(min(10, len(heap))):
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# ---------------------------------------------------------
# Problem 3: All O(1) Data Structure (LeetCode 432, Hard)
# Link: https://leetcode.com/problems/all-oone-data-structure/
# ---------------------------------------------------------
class Node:
    """
    Doubly linked list node:
    Stores:
    - count
    - keys at this count
    """

    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        # Dummy head and tail for DLL
        self.head = Node(float("-inf"))
        self.tail = Node(float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head

        # key -> node that contains it
        self.key_to_node = {}

    def _insert_after(self, node, newNode):
        newNode.prev = node
        newNode.next = node.next
        node.next.prev = newNode
        node.next = newNode

    def _remove_node_if_empty(self, node):
        if node != self.head and node != self.tail and not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            # insert with count 1
            if self.head.next.count == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._insert_after(self.head, node)
            node.keys.add(key)
            self.key_to_node[key] = node
        else:
            node = self.key_to_node[key]
            nextCount = node.count + 1
            if node.next.count == nextCount:
                nextNode = node.next
            else:
                nextNode = Node(nextCount)
                self._insert_after(node, nextNode)
            nextNode.keys.add(key)
            self.key_to_node[key] = nextNode

            # remove key from old node
            node.keys.remove(key)
            self._remove_node_if_empty(node)

    def dec(self, key: str) -> None:
        if key not in self.key_to_node:
            return

        node = self.key_to_node[key]
        if node.count == 1:
            # remove key entirely
            del self.key_to_node[key]
            node.keys.remove(key)
            self._remove_node_if_empty(node)
        else:
            prevCount = node.count - 1
            if node.prev.count == prevCount:
                prevNode = node.prev
            else:
                prevNode = Node(prevCount)
                self._insert_after(node.prev, prevNode)
            prevNode.keys.add(key)
            self.key_to_node[key] = prevNode

            node.keys.remove(key)
            self._remove_node_if_empty(node)

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Test Problem 1
    kth = KthLargest(3, [4, 5, 8, 2])
    print("Problem One Example:", kth.add(10))

    # Test Problem 2
    tw = Twitter()
    tw.postTweet(1, 100)
    print("Problem Two Example:", tw.getNewsFeed(1))

    # Test Problem 3
    ao = AllOne()
    ao.inc("a")
    ao.inc("a")
    ao.inc("b")
    print("Problem Three Example:", ao.getMaxKey())
