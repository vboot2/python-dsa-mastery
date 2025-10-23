"""
Day 53: Binary Search Patterns - LeetCode Problem Solutions
"""


# ---------------------------------------------------------
# Problem: Search in Rotated Sorted Array (LeetCode 33, Medium)
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# ---------------------------------------------------------
class SolutionProblemOne:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Left half sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# ---------------------------------------------------------
# Problem: Find Minimum in Rotated Sorted Array (LeetCode 153, Medium)
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


# ---------------------------------------------------------
# Problem: Find Peak Element (LeetCode 162, Medium)
# Link: https://leetcode.com/problems/find-peak-element/
# ---------------------------------------------------------
class SolutionProblemThree:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 1 Example:", SolutionProblemOne().search([4, 5, 6, 7, 0, 1, 2], 0))
    print("Problem 2 Example:", SolutionProblemTwo().findMin([3, 4, 5, 1, 2]))
    print(
        "Problem 3 Example:",
        SolutionProblemThree().findPeakElement([1, 2, 1, 3, 5, 6, 4]),
    )
