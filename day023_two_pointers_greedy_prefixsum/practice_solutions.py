"""
Day 23: Two Pointers, Greedy, Prefix Sum - LeetCode Problem Solutions
"""

from typing import List

# ---------------------------------------------------------
# Problem: Trapping Rain Water (LeetCode 42, Hard)
# Link: https://leetcode.com/problems/trapping-rain-water/
# ---------------------------------------------------------
class SolutionTrappingRainWater:
    def trap(self, height: List[int]) -> int:
        # Two pointer approach
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water


# ---------------------------------------------------------
# Problem: Jump Game II (LeetCode 45, Medium)
# Link: https://leetcode.com/problems/jump-game-ii/
# ---------------------------------------------------------
class SolutionJumpGameII:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps


# ---------------------------------------------------------
# Problem: Jump Game (LeetCode 55, Medium)
# Link: https://leetcode.com/problems/jump-game/
# ---------------------------------------------------------
class SolutionJumpGame:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
        return True


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 42 Example:", SolutionTrappingRainWater().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print("Problem 45 Example:", SolutionJumpGameII().jump([2,3,1,1,4]))
    print("Problem 55 Example:", SolutionJumpGame().canJump([2,3,1,1,4]))
