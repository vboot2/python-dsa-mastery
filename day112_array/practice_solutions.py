""" Day 112: Array - LeetCode Problem Solutions """

from typing import List, Optional


# ---------------------------------------------------------
# Problem: Remove Duplicates from Sorted Array (LeetCode 26, Easy)
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# ---------------------------------------------------------
class SolutionProblemOne:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


# ---------------------------------------------------------
# Problem: Remove Element (LeetCode 27, Easy)
# Link: https://leetcode.com/problems/remove-element/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


# ---------------------------------------------------------
# Problem: Plus One (LeetCode 66, Easy)
# Link: https://leetcode.com/problems/plus-one/
# ---------------------------------------------------------
class SolutionProblemThree:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10

        if carry:
            digits.insert(0, carry)

        return digits


# ---------------------------------------------------------
# Problem: Single Number (LeetCode 136, Easy)
# Link: https://leetcode.com/problems/single-number/
# ---------------------------------------------------------
class SolutionProblemFour:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR cancels duplicates.
        a ^ a = 0, a ^ 0 = a
        """
        result = 0
        for num in nums:
            result ^= num
        return result


# ---------------------------------------------------------
# Problem: Majority Element (LeetCode 169, Easy)
# Link: https://leetcode.com/problems/majority-element/
# ---------------------------------------------------------
class SolutionProblemFive:
    def majorityElement(self, nums: List[int]) -> Optional[int]:
        """
        Boyer-Moore Voting Algorithm
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    nums1 = [1, 1, 2]
    print("Problem One Example:", SolutionProblemOne().removeDuplicates(nums1))

    nums2 = [3, 2, 2, 3]
    print("Problem Two Example:", SolutionProblemTwo().removeElement(nums2, 3))

    print("Problem Three Example:", SolutionProblemThree().plusOne([9, 9]))

    print("Problem Four Example:", SolutionProblemFour().singleNumber([4, 1, 2, 1, 2]))

    print("Problem Five Example:", SolutionProblemFive().majorityElement([3, 2, 3]))
