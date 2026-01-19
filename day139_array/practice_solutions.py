"""Day 139: Array - LeetCode Problem Solutions"""

from typing import List
import random
import bisect
from collections import defaultdict


# ---------------------------------------------------------
# Problem: Range Sum Query 2D - Immutable (LeetCode 304)
# Link: https://leetcode.com/problems/range-sum-query-2d-immutable/
# ---------------------------------------------------------
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            self.ps = []
            return

        r, c = len(matrix), len(matrix[0])
        self.ps = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(r):
            for j in range(c):
                self.ps[i + 1][j + 1] = (
                    matrix[i][j] + self.ps[i][j + 1] + self.ps[i + 1][j] - self.ps[i][j]
                )

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (
            self.ps[r2 + 1][c2 + 1]
            - self.ps[r1][c2 + 1]
            - self.ps[r2 + 1][c1]
            + self.ps[r1][c1]
        )


# ---------------------------------------------------------
# Problem: Range Sum Query - Mutable (LeetCode 307)
# Link: https://leetcode.com/problems/range-sum-query-mutable/
# ---------------------------------------------------------
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self.arr = nums[:]
        for i, v in enumerate(nums):
            self._add(i + 1, v)

    def _add(self, i, v):
        while i <= self.n:
            self.tree[i] += v
            i += i & -i

    def update(self, index: int, val: int) -> None:
        diff = val - self.arr[index]
        self.arr[index] = val
        self._add(index + 1, diff)

    def sumRange(self, left: int, right: int) -> int:
        def prefix(i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        return prefix(right + 1) - prefix(left)


# ---------------------------------------------------------
# Problem: Maximum Product of Word Lengths (LeetCode 318)
# Link: https://leetcode.com/problems/maximum-product-of-word-lengths/
# ---------------------------------------------------------
class SolutionProblemThree:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        for w in words:
            mask = 0
            for c in set(w):
                mask |= 1 << (ord(c) - ord("a"))
            masks.append((mask, len(w)))

        ans = 0
        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                if masks[i][0] & masks[j][0] == 0:
                    ans = max(ans, masks[i][1] * masks[j][1])
        return ans


# ---------------------------------------------------------
# Problem: Wiggle Sort II (LeetCode 324)
# Link: https://leetcode.com/problems/wiggle-sort-ii/
# ---------------------------------------------------------
class SolutionProblemFour:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return

        nums.sort()

        half = (n + 1) // 2
        small = nums[:half][::-1]
        large = nums[half:][::-1]

        for i in range(1, n, 2):
            nums[i] = large.pop(0)
        for i in range(0, n, 2):
            nums[i] = small.pop(0)


# ---------------------------------------------------------
# Problem: Increasing Triplet Subsequence (LeetCode 334)
# Link: https://leetcode.com/problems/increasing-triplet-subsequence/
# ---------------------------------------------------------
class SolutionProblemFive:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


# ---------------------------------------------------------
# Problem: Combination Sum IV (LeetCode 377)
# Link: https://leetcode.com/problems/combination-sum-iv/
# ---------------------------------------------------------
class SolutionProblemSix:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for n in nums:
                if t - n >= 0:
                    dp[t] += dp[t - n]
        return dp[target]


# ---------------------------------------------------------
# Problem: Shuffle an Array (LeetCode 384)
# Link: https://leetcode.com/problems/shuffle-an-array/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.nums = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = random.randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# ---------------------------------------------------------
# Problem: UTF-8 Validation (LeetCode 393)
# Link: https://leetcode.com/problems/utf-8-validation/
# ---------------------------------------------------------
class SolutionProblemEight:
    def validUtf8(self, data: List[int]) -> bool:
        remaining = 0
        for d in data:
            if remaining == 0:
                if d >> 5 == 0b110:
                    remaining = 1
                elif d >> 4 == 0b1110:
                    remaining = 2
                elif d >> 3 == 0b11110:
                    remaining = 3
                elif d >> 7:
                    return False
            else:
                if d >> 6 != 0b10:
                    return False
                remaining -= 1
        return remaining == 0


# ---------------------------------------------------------
# Problem: Rotate Function (LeetCode 396)
# Link: https://leetcode.com/problems/rotate-function/
# ---------------------------------------------------------
class SolutionProblemNine:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        f = sum(i * n for i, n in enumerate(nums))
        ans = f
        n = len(nums)

        for i in range(1, n):
            f = f + total - n * nums[-i]
            ans = max(ans, f)
        return ans


# ---------------------------------------------------------
# Problem: The Skyline Problem (LeetCode 218)
# Link: https://leetcode.com/problems/the-skyline-problem/
# ---------------------------------------------------------
class SolutionProblemTen:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h))
            events.append((r, h))
        events.sort()

        import heapq

        res = []
        heap = [0]
        prev = 0
        active = defaultdict(int)
        active[0] = 1

        for x, h in events:
            if h < 0:
                heapq.heappush(heap, h)
                active[-h] += 1
            else:
                active[h] -= 1

            while heap and active[-heap[0]] == 0:
                heapq.heappop(heap)

            curr = -heap[0]
            if curr != prev:
                res.append([x, curr])
                prev = curr
        return res


# ---------------------------------------------------------
# Problem: Contains Duplicate III (LeetCode 220)
# Link: https://leetcode.com/problems/contains-duplicate-iii/
# ---------------------------------------------------------
class SolutionProblemEleven:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        if valueDiff < 0:
            return False

        bucket_size = valueDiff + 1

        def get_bucket(x: int) -> int:
            return x // bucket_size

        buckets = {}

        for i, num in enumerate(nums):
            b = get_bucket(num)

            if b in buckets:
                return True

            left = b - 1
            if left in buckets and abs(num - buckets[left]) <= valueDiff:
                return True

            right = b + 1
            if right in buckets and abs(num - buckets[right]) <= valueDiff:
                return True

            buckets[b] = num

            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket = get_bucket(old_num)
                del buckets[old_bucket]

        return False


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "318 Example:",
        SolutionProblemThree().maxProduct(
            ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
        ),
    )
    print("334 Example:", SolutionProblemFive().increasingTriplet([2, 1, 5, 0, 4, 6]))
    print("377 Example:", SolutionProblemSix().combinationSum4([1, 2, 3], 4))
