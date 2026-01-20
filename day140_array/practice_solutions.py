"""Day 140: Array - LeetCode Problem Solutions"""

from typing import List
from collections import defaultdict
import bisect
import heapq


# ---------------------------------------------------------
# Problem: Queue Reconstruction by Height (LeetCode 406)
# Link: https://leetcode.com/problems/queue-reconstruction-by-height/
# ---------------------------------------------------------
class SolutionProblemOne:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


# ---------------------------------------------------------
# Problem: Battleships in a Board (LeetCode 419)
# Link: https://leetcode.com/problems/battleships-in-a-board/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if (i == 0 or board[i - 1][j] == ".") and (
                        j == 0 or board[i][j - 1] == "."
                    ):
                        count += 1
        return count


# ---------------------------------------------------------
# Problem: Maximum XOR of Two Numbers in an Array (LeetCode 421)
# Link: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# ---------------------------------------------------------
class SolutionProblemThree:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            prefixes = {n & mask for n in nums}
            candidate = ans | (1 << i)
            if any((candidate ^ p) in prefixes for p in prefixes):
                ans = candidate
        return ans


# ---------------------------------------------------------
# Problem: Construct Quad Tree (LeetCode 427)
# Link: https://leetcode.com/problems/construct-quad-tree/
# ---------------------------------------------------------
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class SolutionProblemFour:
    def construct(self, grid: List[List[int]]):
        def build(x, y, n):
            val = grid[x][y]
            same = True
            for i in range(x, x + n):
                for j in range(y, y + n):
                    if grid[i][j] != val:
                        same = False
                        break
            if same:
                return Node(val == 1, True, None, None, None, None)

            half = n // 2
            return Node(
                True,
                False,
                build(x, y, half),
                build(x, y + half, half),
                build(x + half, y, half),
                build(x + half, y + half, half),
            )

        return build(0, 0, len(grid))


# ---------------------------------------------------------
# Problem: Find Right Interval (LeetCode 436)
# Link: https://leetcode.com/problems/find-right-interval/
# ---------------------------------------------------------
class SolutionProblemFive:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((s, i) for i, (s, e) in enumerate(intervals))
        res = []

        for s, e in intervals:
            idx = bisect.bisect_left(starts, (e,))
            res.append(starts[idx][1] if idx < len(starts) else -1)
        return res


# ---------------------------------------------------------
# Problem: Find All Duplicates in an Array (LeetCode 442)
# Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
# ---------------------------------------------------------
class SolutionProblemSix:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                res.append(abs(n))
            nums[idx] *= -1
        return res


# ---------------------------------------------------------
# Problem: Number of Boomerangs (LeetCode 447)
# Link: https://leetcode.com/problems/number-of-boomerangs/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            freq = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    dx = points[i][0] - points[j][0]
                    dy = points[i][1] - points[j][1]
                    freq[dx * dx + dy * dy] += 1
            for v in freq.values():
                res += v * (v - 1)
        return res


# ---------------------------------------------------------
# Problem: Count of Smaller Numbers After Self (LeetCode 315)
# Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# ---------------------------------------------------------
class SolutionProblemTen:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        def sort(enum):
            mid = len(enum) // 2
            if mid:
                left, right = sort(enum[:mid]), sort(enum[mid:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or (i < m and left[i][1] <= right[j][1]):
                        enum[i + j] = left[i]
                        res[left[i][0]] += j
                        i += 1
                    else:
                        enum[i + j] = right[j]
                        j += 1
            return enum

        sort(list(enumerate(nums)))
        return res


# ---------------------------------------------------------
# Problem: Create Maximum Number (LeetCode 321)
# Link: https://leetcode.com/problems/create-maximum-number/
# ---------------------------------------------------------
class SolutionProblemEleven:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums, k):
            stack = []
            drop = len(nums) - k
            for n in nums:
                while drop and stack and stack[-1] < n:
                    stack.pop()
                    drop -= 1
                stack.append(n)
            return stack[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in range(len(a) + len(b))]

        res = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            res = max(res, merge(pick(nums1, i), pick(nums2, k - i)))
        return res


# ---------------------------------------------------------
# Problem: Count of Range Sum (LeetCode 327)
# Link: https://leetcode.com/problems/count-of-range-sum/
# ---------------------------------------------------------
class SolutionProblemTwelve:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)

        def sort(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)
            j = k = mid
            for i in range(lo, mid):
                while k < hi and prefix[k] - prefix[i] < lower:
                    k += 1
                while j < hi and prefix[j] - prefix[i] <= upper:
                    j += 1
                count += j - k
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        return sort(0, len(prefix))


# ---------------------------------------------------------
# Problem: Patching Array (LeetCode 330)
# Link: https://leetcode.com/problems/patching-array/
# ---------------------------------------------------------
class SolutionProblemThirteen:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        i = patches = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches


# ---------------------------------------------------------
# Problem: Self Crossing (LeetCode 335)
# Link: https://leetcode.com/problems/self-crossing/
# ---------------------------------------------------------
class SolutionProblemFourteen:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for i in range(3, len(distance)):
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True
            if (
                i >= 4
                and distance[i - 1] == distance[i - 3]
                and distance[i] + distance[i - 4] >= distance[i - 2]
            ):
                return True
            if (
                i >= 5
                and distance[i - 2] >= distance[i - 4]
                and distance[i] >= distance[i - 2] - distance[i - 4]
                and distance[i - 1] >= distance[i - 3] - distance[i - 5]
                and distance[i - 1] <= distance[i - 3]
            ):
                return True
        return False


# ---------------------------------------------------------
# Problem: Palindrome Pairs (LeetCode 336)
# Link: https://leetcode.com/problems/palindrome-pairs/
# ---------------------------------------------------------
class SolutionProblemFifteen:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res: List[List[int]] = []
        rev_lookup = {w[::-1]: i for i, w in enumerate(words)}

        for i, w in enumerate(words):
            n = len(w)
            for j in range(n + 1):
                left, right = w[:j], w[j:]

                if left == left[::-1]:
                    idx = rev_lookup.get(right)
                    if idx is not None and idx != i:
                        res.append([idx, i])

                if j != n and right == right[::-1]:
                    idx = rev_lookup.get(left)
                    if idx is not None and idx != i:
                        res.append([i, idx])

        return res
