"""
Day 07: Binary Search - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Problem: Binary Search (LeetCode 704, Easy)
# Link: https://leetcode.com/problems/binary-search/
# ---------------------------------------------------------
class SolutionBinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# ---------------------------------------------------------
# Problem: Search Insert Position (LeetCode 35, Easy)
# Link: https://leetcode.com/problems/search-insert-position/
# ---------------------------------------------------------
class SolutionSearchInsert:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


# ---------------------------------------------------------
# Problem: Find First and Last Position of Element in Sorted Array (LeetCode 34, Medium)
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# ---------------------------------------------------------
class SolutionFindFirstLast:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first):
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        return [find_bound(True), find_bound(False)]


# ---------------------------------------------------------
# Example usage (LeetCode cases)
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Binary Search Example 1:", 
          SolutionBinarySearch().search([-1,0,3,5,9,12], 9))
    print("Binary Search Example 2:", 
          SolutionBinarySearch().search([-1,0,3,5,9,12], 2))

    print("Search Insert Position Example 1:", 
          SolutionSearchInsert().searchInsert([1,3,5,6], 5))
    print("Search Insert Position Example 2:", 
          SolutionSearchInsert().searchInsert([1,3,5,6], 2))
    print("Search Insert Position Example 3:", 
          SolutionSearchInsert().searchInsert([1,3,5,6], 7))

    print("Find First and Last Position of Element in Sorted Array Example 1:", 
          SolutionFindFirstLast().searchRange([5,7,7,8,8,10], 8))
    print("Find First and Last Position of Element in Sorted Array Example 1:", 
          SolutionFindFirstLast().searchRange([5,7,7,8,8,10], 6))
    print("Find First and Last Position of Element in Sorted Array Example 1:", 
          SolutionFindFirstLast().searchRange([], 0))
