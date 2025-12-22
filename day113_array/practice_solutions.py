""" Day 113: Array - LeetCode Problem Solutions """

from typing import List


# ---------------------------------------------------------
# Problem: Contains Duplicate II (LeetCode 219, Easy)
# Link: https://leetcode.com/problems/contains-duplicate-ii/
# ---------------------------------------------------------
class SolutionProblemOne:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i

        return False


# ---------------------------------------------------------
# Problem: Move Zeroes (LeetCode 283, Easy)
# Link: https://leetcode.com/problems/move-zeroes/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        In-place move using two pointers.
        """
        insert_pos = 0

        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        for i in range(insert_pos, len(nums)):
            nums[i] = 0


# ---------------------------------------------------------
# Problem: Intersection of Two Arrays (LeetCode 349, Easy)
# Link: https://leetcode.com/problems/intersection-of-two-arrays/
# ---------------------------------------------------------
class SolutionProblemThree:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# ---------------------------------------------------------
# Problem: Intersection of Two Arrays II (LeetCode 350, Easy)
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# ---------------------------------------------------------
class SolutionProblemFour:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter

        count1 = Counter(nums1)
        result = []

        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1

        return result


# ---------------------------------------------------------
# Problem: Third Maximum Number (LeetCode 414, Easy)
# Link: https://leetcode.com/problems/third-maximum-number/
# ---------------------------------------------------------
class SolutionProblemFive:
    def thirdMax(self, nums: List[int]) -> int:
        unique = set(nums)

        if len(unique) < 3:
            return max(unique)

        unique.remove(max(unique))
        unique.remove(max(unique))

        return max(unique)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().containsNearbyDuplicate([1,2,3,1], 3))

    nums = [0,1,0,3,12]
    SolutionProblemTwo().moveZeroes(nums)
    print("Problem Two Example:", nums)

    print("Problem Three Example:", SolutionProblemThree().intersection([1,2,2,1], [2,2]))

    print("Problem Four Example:", SolutionProblemFour().intersect([1,2,2,1], [2,2]))

    print("Problem Five Example:", SolutionProblemFive().thirdMax([3,2,1]))
