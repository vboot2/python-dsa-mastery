"""Day 124: Two Pointers - LeetCode Problem Solutions"""

from typing import List


# ---------------------------------------------------------
# Problem: Count Pairs Whose Sum is Less than Target (LeetCode 2824, Easy)
# Link: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
# ---------------------------------------------------------
class SolutionProblemOne:
    def countPairs(self, nums: List[int], target: int) -> int:
        """
        Sort + two pointers:
        - If sum < target, all pairs between left and right count
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count


# ---------------------------------------------------------
# Problem: Find Indices With Index and Value Difference I (LeetCode 2903, Easy)
# Link: https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        """
        - Use two pointers i and j to check pairs
        - Move pointers based on indexDifference constraint
        """
        n = len(nums)

        for i in range(n):
            # j needs to be at least indexDifference away from i
            for j in range(i + indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]

        return [-1, -1]


# ---------------------------------------------------------
# Problem: Count the Number of Incremovable Subarrays I (LeetCode 2970, Easy)
# Link: https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/
# ---------------------------------------------------------
class SolutionProblemThree:
    def countIncremovable(self, nums: List[int]) -> int:
        """
        1. Precompute prefix and suffix arrays to check if parts are strictly increasing
        2. Use two pointers i (start) and j (end) to iterate through subarrays
        3. For each subarray [i, j], check if:
           - Prefix [0..i-1] is strictly increasing
           - Suffix [j+1..n-1] is strictly increasing
           - Last element of prefix < First element of suffix (if both exist)
        """
        n = len(nums)

        prefix_good = [True] * n

        for i in range(1, n):
            prefix_good[i] = prefix_good[i - 1] and (nums[i] > nums[i - 1])

        suffix_good = [True] * n

        for i in range(n - 2, -1, -1):
            suffix_good[i] = suffix_good[i + 1] and (nums[i] < nums[i + 1])

        result = 0

        for i in range(n):
            for j in range(i, n):
                valid = True
                if i > 0 and not prefix_good[i - 1]:
                    valid = False
                if j < n - 1 and not suffix_good[j + 1]:
                    valid = False
                if valid and i > 0 and j < n - 1:
                    if nums[j + 1] <= nums[i - 1]:
                        valid = False
                if valid:
                    result += 1

        return result


# ---------------------------------------------------------
# Problem: Minimum Average of Smallest and Largest Elements (LeetCode 3194, Easy)
# Link: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
# ---------------------------------------------------------
class SolutionProblemFour:
    def minimumAverage(self, nums: List[int]) -> float:
        """
        Maintain two pointers:
        - left at start
        - right at end
        Compute average pairs as we move inward.
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        min_avg = float("inf")

        while left < right:
            avg = (nums[left] + nums[right]) / 2
            min_avg = min(min_avg, avg)
            left += 1
            right -= 1

        return min_avg


# ---------------------------------------------------------
# Problem: Earliest Finish Time for Land and Water Rides I (LeetCode 3633, Easy)
# Link: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
# ---------------------------------------------------------
class SolutionProblemFive:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        result = float("inf")

        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):
                # Land first, then water
                finish1 = max(ws, ls + ld) + wd
                # Water first, then land
                finish2 = max(ls, ws + wd) + ld
                result = min(result, finish1, finish2)

        return int(result)


# ---------------------------------------------------------
# Problem: Flip Square Submatrix Vertically (LeetCode 3643, Easy)
# Link: https://leetcode.com/problems/flip-square-submatrix-vertically/
# ---------------------------------------------------------
class SolutionProblemSix:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        """
        Flip the submatrix in-place by swapping rows within the submatrix.
        """
        # Flip vertically by swapping rows
        for i in range(k // 2):  # Only need to swap first half with last half
            # Swap row i with row (k-1-i) within the submatrix
            top_row = x + i
            bottom_row = x + (k - 1 - i)

            # Swap all columns in these rows within the submatrix
            for j in range(k):
                grid[top_row][y + j], grid[bottom_row][y + j] = (
                    grid[bottom_row][y + j],
                    grid[top_row][y + j],
                )

        return grid


# ---------------------------------------------------------
# Problem: Minimum Number of Flips to Reverse Binary String (LeetCode 3750, Easy)
# Link: https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def minimumFlips(self, n: int) -> int:
        # Get binary string
        s = bin(n)[2:]
        n_len = len(s)

        # Two pointers approach
        left, right = 0, n_len - 1
        flips = 0

        while left < right:
            if s[left] != s[right]:
                flips += 2  # Need to flip both bits
            left += 1
            right -= 1

        return flips


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("2824 Example:", SolutionProblemOne().countPairs([3, 1, 5, 2], 6))
    print("2903 Example:", SolutionProblemTwo().findIndices([1, 5, 3, 4, 2], 2, 2))
    print("2970 Example:", SolutionProblemThree().countIncremovable([1, 2, 3, 4]))
    print("3194 Example:", SolutionProblemFour().minimumAverage([4, 2, 9, 5]))
    print(
        "3633 Example:",
        SolutionProblemFive().earliestFinishTime([2, 8], [4, 1], [6], [3]),
    )
    print(
        "3643 Example:",
        SolutionProblemSix().reverseSubmatrix(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1, 0, 3
        ),
    )
    print("3750 Example:", SolutionProblemSeven().minimumFlips(7))
