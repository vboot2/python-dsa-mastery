"""
Day 22: Two Pointers, Greedy, Prefix Sum - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Container With Most Water (LeetCode 11, Medium)
# Link: https://leetcode.com/problems/container-with-most-water/
# ---------------------------------------------------------
class SolutionContainerWater:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            best = max(best, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best


# ---------------------------------------------------------
# Problem: 3Sum (LeetCode 15, Medium)
# Link: https://leetcode.com/problems/3sum/
# ---------------------------------------------------------
class SolutionThreeSum:
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return result


# ---------------------------------------------------------
# Problem: 3Sum Closest (LeetCode 16, Medium)
# Link: https://leetcode.com/problems/3sum-closest/
# ---------------------------------------------------------
class SolutionThreeSumClosest:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(target - total) < abs(target - closest):
                    closest = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target
        return closest


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Container With Most Water:", SolutionContainerWater().maxArea([1,8,6,2,5,4,8,3,7]))
    print("3Sum:", SolutionThreeSum().threeSum([-1,0,1,2,-1,-4]))
    print("3Sum Closest:", SolutionThreeSumClosest().threeSumClosest([-1,2,1,-4], 1))
