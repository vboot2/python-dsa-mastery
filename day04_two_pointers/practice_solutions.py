"""
Day 04: Two Pointers - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Merge Sorted Array (LeetCode 88, Easy)
# Link: https://leetcode.com/problems/merge-sorted-array/
# ---------------------------------------------------------
class SolutionMergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Constraint checks
        assert len(nums1) == m + n, f"nums1 length must be m + n, got {len(nums1)} != {m+n}"
        assert len(nums2) == n, f"nums2 length must be n, got {len(nums2)} != {n}"
        assert 0 <= m <= 200, f"m must be in range [0,200], got {m}"
        assert 0 <= n <= 200, f"n must be in range [0,200], got {n}"
        assert 1 <= m + n <= 200, f"m+n must be in range [1,200], got {m+n}"
        for val in nums1 + nums2:
            assert -10**9 <= val <= 10**9, f"Value {val} out of allowed range [-10^9,10^9]"

        # Merge process
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 has leftover elements
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# ---------------------------------------------------------
# Problem: Two Sum II - Input Array is Sorted (LeetCode 167, Medium)
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# ---------------------------------------------------------
class SolutionTwoSumSorted:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
        return []


# ---------------------------------------------------------
# Problem: Linked List Cycle (LeetCode 141, Easy)
# Link: https://leetcode.com/problems/linked-list-cycle/
# ---------------------------------------------------------
# Floyd’s cycle detection (fast & slow pointers)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionLinkedListCycle:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# ---------------------------------------------------------
# Example usage (LeetCode cases)
# ---------------------------------------------------------
if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    SolutionMergeSortedArray().merge(nums1, 3, [2,5,6], 3)
    print("Merge Sorted Array Example 1:\nnums1:", nums1)
    nums1 = [1]
    SolutionMergeSortedArray().merge(nums1, 1, [], 0)
    print("Merge Sorted Array Example 2:\nnums1:", nums1)
    nums1 = [0]
    SolutionMergeSortedArray().merge(nums1, 0, [1], 1)
    print("Merge Sorted Array Example 3:\nnums1:", nums1)
    print()
    print("Two Sum II - Input Array is Sorted Example 1:", SolutionTwoSumSorted().twoSum([2,7,11,15], 9))
    print("Two Sum II - Input Array is Sorted Example 2:", SolutionTwoSumSorted().twoSum([2,3,4], 6))
    print("Two Sum II - Input Array is Sorted Example 3:", SolutionTwoSumSorted().twoSum([-1,0], 0))
