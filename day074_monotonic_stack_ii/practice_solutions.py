"""
Day 74: Monotonic Stack II - LeetCode Problem Solutions
"""


# ---------------------------------------------------------
# Problem 1: Largest Rectangle in Histogram (LeetCode 84, Hard)
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
# ---------------------------------------------------------
class SolutionLargestRectangle:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        heights.pop()
        return max_area


# ---------------------------------------------------------
# Problem 2: Maximal Rectangle (LeetCode 85, Hard)
# Link: https://leetcode.com/problems/maximal-rectangle/
# ---------------------------------------------------------
class SolutionMaximalRectangle:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        for row in matrix:
            for i in range(n):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            max_area = max(max_area, self.largestRectangle(heights))
        return max_area

    def largestRectangle(self, heights):
        stack = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        heights.pop()
        return max_area


# ---------------------------------------------------------
# Problem 3: Remove K Digits (LeetCode 402, Medium)
# Link: https://leetcode.com/problems/remove-k-digits/
# ---------------------------------------------------------
class SolutionRemoveKDigits:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        final_stack = stack[:-k] if k else stack
        result = "".join(final_stack).lstrip("0") or "0"
        return result


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "Largest Rectangle:",
        SolutionLargestRectangle().largestRectangleArea([2, 1, 5, 6, 2, 3]),
    )  # 10
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(
        "Maximal Rectangle:", SolutionMaximalRectangle().maximalRectangle(matrix)
    )  # 6
    print(
        "Remove K Digits:", SolutionRemoveKDigits().removeKdigits("1432219", 3)
    )  # "1219"
