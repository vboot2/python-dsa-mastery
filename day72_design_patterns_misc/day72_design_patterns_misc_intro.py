"""
Day 72: Design Patterns (Misc)

Important design patterns:
- Min-Heap for maintaining streaming data (K-th largest)
- Social network feed design (Tweet retrieval with heaps)
- Doubly-linked list + ordered map design (All O(1) operations)
"""

# Example 1: Kth Largest Element Stream (Min Heap)
import heapq


def example_one():
    """
    Maintain a min-heap of size k.
    Always keep the k largest elements in the heap.
    The root of the heap is the kth largest.
    """
    k = 3
    nums = [4, 5, 8, 2]
    heap = nums[:k]
    heapq.heapify(heap)

    # Next elements arrive in stream
    for val in [10, 9, 4]:
        if val > heap[0]:
            heapq.heapreplace(heap, val)

    return heap[0]  # Kth largest element


print("Output Example 1:", example_one())


# Example 2: Designing a News Feed (Tweet retrieval pattern)
def example_two():
    """
    Use:
    - user->tweets history
    - follow graph
    - combine tweets of followed users using max-heap
    """
    import heapq

    # Dummy tweet data: (timestamp, tweetId)
    tweets = {1: [(5, "tweet5"), (3, "tweet3")], 2: [(4, "tweet4"), (2, "tweet2")]}
    following = {1: {2}}  # user1 follows user2

    feed = []
    heap = []

    # push latest tweets from self and following
    for user in [1] | following[1]:
        for ts, twid in tweets.get(user, []):
            heapq.heappush(heap, (-ts, twid))

    # get top 3 tweets
    for _ in range(min(3, len(heap))):
        feed.append(heapq.heappop(heap)[1])

    return feed


print("Output Example 2:", example_two())
