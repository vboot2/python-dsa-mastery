"""Day 141: Array - LeetCode Problem Solutions"""

from typing import List
from collections import defaultdict
import random
import bisect


# ---------------------------------------------------------
# Problem: Minimum Moves to Equal Array Elements (LeetCode 453)
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# ---------------------------------------------------------
class SolutionProblemOne:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


# ---------------------------------------------------------
# Problem: 4Sum II (LeetCode 454)
# Link: https://leetcode.com/problems/4sum-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        ab = defaultdict(int)
        for a in nums1:
            for b in nums2:
                ab[a + b] += 1

        count = 0
        for c in nums3:
            for d in nums4:
                count += ab[-(c + d)]
        return count


# ---------------------------------------------------------
# Problem: 132 Pattern (LeetCode 456)
# Link: https://leetcode.com/problems/132-pattern/
# ---------------------------------------------------------
class SolutionProblemThree:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float("-inf")

        for n in reversed(nums):
            if n < third:
                return True
            while stack and stack[-1] < n:
                third = stack.pop()
            stack.append(n)
        return False


# ---------------------------------------------------------
# Problem: Circular Array Loop (LeetCode 457)
# Link: https://leetcode.com/problems/circular-array-loop/
# ---------------------------------------------------------
class SolutionProblemFour:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i

            while (
                nums[slow] * nums[next_index(slow)] > 0
                and nums[fast] * nums[next_index(fast)] > 0
                and nums[fast] * nums[next_index(next_index(fast))] > 0
            ):

                slow = next_index(slow)
                fast = next_index(next_index(fast))

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            slow = i
            val = nums[i]
            while val * nums[slow] > 0:
                next_slow = next_index(slow)
                nums[slow] = 0
                slow = next_slow

        return False


# ---------------------------------------------------------
# Problem: Minimum Moves to Equal Array Elements II (LeetCode 462)
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# ---------------------------------------------------------
class SolutionProblemFive:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(n - median) for n in nums)


# ---------------------------------------------------------
# Problem: Heaters (LeetCode 475)
# Link: https://leetcode.com/problems/heaters/
# ---------------------------------------------------------
class SolutionProblemSix:
    def findRadius(self, houses: List[int], heaters: List[int]):
        heaters.sort()
        res = 0

        for h in houses:
            i = bisect.bisect_left(heaters, h)
            left = heaters[i - 1] if i > 0 else float("-inf")
            right = heaters[i] if i < len(heaters) else float("inf")
            res = max(res, min(abs(h - left), abs(right - h)))

        return res


# ---------------------------------------------------------
# Problem: Total Hamming Distance (LeetCode 477)
# Link: https://leetcode.com/problems/total-hamming-distance/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for bit in range(32):
            ones = sum((num >> bit) & 1 for num in nums)
            res += ones * (n - ones)
        return res


# ---------------------------------------------------------
# Problem: Non-decreasing Subsequences (LeetCode 491)
# Link: https://leetcode.com/problems/non-decreasing-subsequences/
# ---------------------------------------------------------
class SolutionProblemEight:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(i, path):
            if len(path) >= 2:
                res.add(tuple(path))
            used = set()
            for j in range(i, len(nums)):
                if (not path or nums[j] >= path[-1]) and nums[j] not in used:
                    used.add(nums[j])
                    backtrack(j + 1, path + [nums[j]])

        backtrack(0, [])
        return list(map(list, res))


# ---------------------------------------------------------
# Problem: Random Point in Non-overlapping Rectangles (LeetCode 497)
# Link: https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
# ---------------------------------------------------------
class SolutionProblemNine:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.points = []
        total = 0
        for x1, y1, x2, y2 in rects:
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.points.append(total)

    def pick(self) -> List[int]:
        r = random.randint(1, self.points[-1])
        idx = bisect.bisect_left(self.points, r)
        x1, y1, x2, y2 = self.rects[idx]
        width = x2 - x1 + 1
        offset = r - (self.points[idx - 1] if idx > 0 else 0) - 1
        return [x1 + offset % width, y1 + offset // width]


# ---------------------------------------------------------
# Problem: Max Sum of Rectangle No Larger Than K (LeetCode 363)
# Link: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
# ---------------------------------------------------------
class SolutionProblemTen:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int):
        res = float("-inf")
        rows, cols = len(matrix), len(matrix[0])

        for left in range(cols):
            sums = [0] * rows
            for right in range(left, cols):
                for r in range(rows):
                    sums[r] += matrix[r][right]

                prefix = [0]
                curr = 0
                for s in sums:
                    curr += s
                    idx = bisect.bisect_left(prefix, curr - k)
                    if idx < len(prefix):
                        res = max(res, curr - prefix[idx])
                    bisect.insort(prefix, curr)
        return res


# ---------------------------------------------------------
# Problem: Insert Delete GetRandom O(1) - Duplicates allowed (LeetCode 381)
# Link: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
# ---------------------------------------------------------
class RandomizedCollection:
    def __init__(self):
        self.arr = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False
        i = self.idx[val].pop()
        last = self.arr[-1]
        self.arr[i] = last
        self.idx[last].add(i)
        self.idx[last].discard(len(self.arr) - 1)
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# ---------------------------------------------------------
# Problem: Perfect Rectangle (LeetCode 391)
# Link: https://leetcode.com/problems/perfect-rectangle/
# ---------------------------------------------------------
class SolutionProblemTwelve:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()
        x1 = y1 = float("inf")
        x2 = y2 = float("-inf")

        for a, b, c, d in rectangles:
            area += (c - a) * (d - b)
            x1, y1 = min(x1, a), min(y1, b)
            x2, y2 = max(x2, c), max(y2, d)

            for p in [(a, b), (a, d), (c, b), (c, d)]:
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)

        return (
            area == (x2 - x1) * (y2 - y1)
            and len(corners) == 4
            and (x1, y1) in corners
            and (x1, y2) in corners
            and (x2, y1) in corners
            and (x2, y2) in corners
        )
