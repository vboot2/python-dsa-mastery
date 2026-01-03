"""Day 123: Two Pointers - LeetCode Problem Solutions"""

from typing import List
from collections import Counter


# ---------------------------------------------------------
# Problem: Number of Arithmetic Triplets (LeetCode 2367, Easy)
# Link: https://leetcode.com/problems/number-of-arithmetic-triplets/
# ---------------------------------------------------------
class SolutionProblemOne:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        count = 0
        for x in nums:
            if x + diff in s and x + 2 * diff in s:
                count += 1
        return count


# ---------------------------------------------------------
# Problem: Largest Positive Integer That Exists With Its Negative (LeetCode 2441, Easy)
# Link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for x in nums:
            if x * -1 in nums:
                return x * -1
        return -1


# ---------------------------------------------------------
# Problem: Apply Operations to an Array (LeetCode 2460, Easy)
# Link: https://leetcode.com/problems/apply-operations-to-an-array/
# ---------------------------------------------------------
class SolutionProblemThree:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        Two pointers:
        - First pass to apply doubling rules
        - Second pass to shift zeros to end
        """
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        write = 0
        for read in range(n):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        for i in range(write, n):
            nums[i] = 0

        return nums


# ---------------------------------------------------------
# Problem: Number of Distinct Averages (LeetCode 2465, Easy)
# Link: https://leetcode.com/problems/number-of-distinct-averages/
# ---------------------------------------------------------
class SolutionProblemFour:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        seen = set()

        while left < right:
            seen.add(nums[left] + nums[right])
            left += 1
            right -= 1

        return len(seen)


# ---------------------------------------------------------
# Problem: Maximum Enemy Forts That Can Be Captured (LeetCode 2511, Easy)
# Link: https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/
# ---------------------------------------------------------
class SolutionProblemFive:
    def captureForts(self, forts: List[int]) -> int:
        """
        Two pointers:
        - Track last friendly fort
        - Count enemy forts in between
        """
        last = -1
        result = 0

        for i, v in enumerate(forts):
            if v != 0:
                if last != -1 and forts[last] != v:
                    result = max(result, i - last - 1)
                last = i

        return result


# ---------------------------------------------------------
# Problem: Minimum Common Value (LeetCode 2540, Easy)
# Link: https://leetcode.com/problems/minimum-common-value/
# ---------------------------------------------------------
class SolutionProblemSix:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1


# ---------------------------------------------------------
# Problem: Find the Array Concatenation Value (LeetCode 2562, Easy)
# Link: https://leetcode.com/problems/find-the-array-concatenation-value/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = 0

        while left <= right:
            if left == right:
                result += nums[left]
            else:
                result += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1

        return result


# ---------------------------------------------------------
# Problem: Merge Two 2D Arrays by Summing Values (LeetCode 2570, Easy)
# Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
# ---------------------------------------------------------
class SolutionProblemEight:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        i = j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        result.extend(nums1[i:])
        result.extend(nums2[j:])
        return result


# ---------------------------------------------------------
# Problem: Lexicographically Smallest Palindrome (LeetCode 2697, Easy)
# Link: https://leetcode.com/problems/lexicographically-smallest-palindrome/
# ---------------------------------------------------------
class SolutionProblemNine:
    def makeSmallestPalindrome(self, s: str) -> str:
        sl = list(s)
        left, right = 0, len(sl) - 1

        while left < right:
            if sl[left] != sl[right]:
                smaller = min(sl[left], sl[right])
                sl[left] = sl[right] = smaller
            left += 1
            right -= 1

        return "".join(sl)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "2367 Example:", SolutionProblemOne().arithmeticTriplets([0, 1, 4, 6, 7, 10], 3)
    )
    print("2441 Example:", SolutionProblemTwo().findMaxK([-1, 2, -3, 3]))
    print("2460 Example:", SolutionProblemThree().applyOperations([1, 2, 2, 1, 1, 0]))
    print("2465 Example:", SolutionProblemFour().distinctAverages([4, 1, 4, 0, 3, 5]))
    print(
        "2511 Example:",
        SolutionProblemFive().captureForts([1, 0, 0, -1, 0, 0, 0, 0, 1]),
    )
    print("2540 Example:", SolutionProblemSix().getCommon([1, 2, 3], [2, 4]))
    print("2562 Example:", SolutionProblemSeven().findTheArrayConcVal([7, 52, 2, 4]))
    print(
        "2570 Example:",
        SolutionProblemEight().mergeArrays(
            [[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]
        ),
    )
    print("2697 Example:", SolutionProblemNine().makeSmallestPalindrome("egcfe"))
