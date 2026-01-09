"""Day 127: Array - LeetCode Problem Solutions"""

from typing import List


# ---------------------------------------------------------
# Problem: Range Addition II (LeetCode 598, Easy)
# Link: https://leetcode.com/problems/range-addition-ii/
# ---------------------------------------------------------
class SolutionProblemOne:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row, min_col = m, n
        for r, c in ops:
            min_row = min(min_row, r)
            min_col = min(min_col, c)
        return min_row * min_col


# ---------------------------------------------------------
# Problem: Can Place Flowers (LeetCode 605, Easy)
# Link: https://leetcode.com/problems/can-place-flowers/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = i == 0 or flowerbed[i - 1] == 0
                right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
                if left and right:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0


# ---------------------------------------------------------
# Problem: Maximum Product of Three Numbers (LeetCode 628, Easy)
# Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
# ---------------------------------------------------------
class SolutionProblemThree:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


# ---------------------------------------------------------
# Problem: Image Smoother (LeetCode 661, Easy)
# Link: https://leetcode.com/problems/image-smoother/
# ---------------------------------------------------------
class SolutionProblemFour:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                total = count = 0
                for i in range(max(0, r - 1), min(rows, r + 2)):
                    for j in range(max(0, c - 1), min(cols, c + 2)):
                        total += img[i][j]
                        count += 1
                result[r][c] = total // count

        return result


# ---------------------------------------------------------
# Problem: Longest Continuous Increasing Subsequence (LeetCode 674, Easy)
# Link: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# ---------------------------------------------------------
class SolutionProblemFive:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                curr = 1
            longest = max(longest, curr)

        return longest


# ---------------------------------------------------------
# Problem: Baseball Game (LeetCode 682, Easy)
# Link: https://leetcode.com/problems/baseball-game/
# ---------------------------------------------------------
class SolutionProblemSix:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)


# ---------------------------------------------------------
# Problem: 1-bit and 2-bit Characters (LeetCode 717, Easy)
# Link: https://leetcode.com/problems/1-bit-and-2-bit-characters/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1


# ---------------------------------------------------------
# Problem: Find Pivot Index (LeetCode 724, Easy)
# Link: https://leetcode.com/problems/find-pivot-index/
# ---------------------------------------------------------
class SolutionProblemEight:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, n in enumerate(nums):
            if left_sum == total - left_sum - n:
                return i
            left_sum += n

        return -1


# ---------------------------------------------------------
# Problem: Flood Fill (LeetCode 733, Easy)
# Link: https://leetcode.com/problems/flood-fill/
# ---------------------------------------------------------
class SolutionProblemNine:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image

        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            if image[r][c] != original:
                return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


# ---------------------------------------------------------
# Problem: Find Smallest Letter Greater Than Target (LeetCode 744, Easy)
# Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# ---------------------------------------------------------
class SolutionProblemTen:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]


# ---------------------------------------------------------
# Problem: Largest Number At Least Twice of Others (LeetCode 747, Easy)
# Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# ---------------------------------------------------------
class SolutionProblemEleven:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        idx = nums.index(max_val)

        for n in nums:
            if n != max_val and max_val < 2 * n:
                return -1
        return idx


# ---------------------------------------------------------
# Problem: Toeplitz Matrix (LeetCode 766, Easy)
# Link: https://leetcode.com/problems/toeplitz-matrix/
# ---------------------------------------------------------
class SolutionProblemTwelve:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False
        return True


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("598 Example:", SolutionProblemOne().maxCount(3, 3, [[2, 2], [3, 3]]))
    print("605 Example:", SolutionProblemTwo().canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print("628 Example:", SolutionProblemThree().maximumProduct([1, 2, 3, 4]))
    print("674 Example:", SolutionProblemFive().findLengthOfLCIS([1, 3, 5, 4, 7]))
    print("682 Example:", SolutionProblemSix().calPoints(["5", "2", "C", "D", "+"]))
    print("717 Example:", SolutionProblemSeven().isOneBitCharacter([1, 0, 0]))
    print("724 Example:", SolutionProblemEight().pivotIndex([1, 7, 3, 6, 5, 6]))
    print("744 Example:", SolutionProblemTen().nextGreatestLetter(["c", "f", "j"], "a"))
    print("747 Example:", SolutionProblemEleven().dominantIndex([3, 6, 1, 0]))
    print(
        "766 Example:",
        SolutionProblemTwelve().isToeplitzMatrix([[1, 2, 3], [4, 1, 2], [5, 4, 1]]),
    )
