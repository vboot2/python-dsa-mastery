"""Day 131: Array - LeetCode Problem Solutions"""

from typing import List
import heapq


# ---------------------------------------------------------
# Problem: Maximize Sum Of Array After K Negations (LeetCode 1005, Easy)
# Link: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
# ---------------------------------------------------------
class SolutionProblemOne:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0

        while i < len(nums) and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1

        if k % 2 == 1:
            nums[nums.index(min(nums))] *= -1

        return sum(nums)


# ---------------------------------------------------------
# Problem: Partition Array Into Three Parts With Equal Sum (LeetCode 1013, Easy)
# Link: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        prefix = count = 0

        for num in arr:
            prefix += num
            if prefix == target:
                count += 1
                prefix = 0

        return count >= 3


# ---------------------------------------------------------
# Problem: Binary Prefix Divisible By 5 (LeetCode 1018, Easy)
# Link: https://leetcode.com/problems/binary-prefix-divisible-by-5/
# ---------------------------------------------------------
class SolutionProblemThree:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        current = 0

        for bit in nums:
            current = (current * 2 + bit) % 5
            result.append(current == 0)

        return result


# ---------------------------------------------------------
# Problem: Matrix Cells in Distance Order (LeetCode 1030, Easy)
# Link: https://leetcode.com/problems/matrix-cells-in-distance-order/
# ---------------------------------------------------------
class SolutionProblemFour:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int):
        cells = [(r, c) for r in range(rows) for c in range(cols)]
        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return cells


# ---------------------------------------------------------
# Problem: Valid Boomerang (LeetCode 1037, Easy)
# Link: https://leetcode.com/problems/valid-boomerang/
# ---------------------------------------------------------
class SolutionProblemFive:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)


# ---------------------------------------------------------
# Problem: Last Stone Weight (LeetCode 1046, Easy)
# Link: https://leetcode.com/problems/last-stone-weight/
# ---------------------------------------------------------
class SolutionProblemSix:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0


# ---------------------------------------------------------
# Problem: Height Checker (LeetCode 1051, Easy)
# Link: https://leetcode.com/problems/height-checker/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(h != e for h, e in zip(heights, expected))


# ---------------------------------------------------------
# Problem: Distance Between Bus Stops (LeetCode 1184, Easy)
# Link: https://leetcode.com/problems/distance-between-bus-stops/
# ---------------------------------------------------------
class SolutionProblemEight:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        if start > destination:
            start, destination = destination, start

        clockwise = sum(distance[start:destination])
        counter = sum(distance) - clockwise

        return min(clockwise, counter)


# ---------------------------------------------------------
# Problem: Minimum Absolute Difference (LeetCode 1200, Easy)
# Link: https://leetcode.com/problems/minimum-absolute-difference/
# ---------------------------------------------------------
class SolutionProblemNine:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")

        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "1005 Example:",
        SolutionProblemOne().largestSumAfterKNegations([-2, 5, 0, 2, -2], 3),
    )
    print(
        "1013 Example:",
        SolutionProblemTwo().canThreePartsEqualSum([0, 2, 1, -1, 1, -1, 1]),
    )
    print("1018 Example:", SolutionProblemThree().prefixesDivBy5([0, 1, 1]))
    print("1046 Example:", SolutionProblemSix().lastStoneWeight([2, 7, 4, 1, 8, 1]))
