"""
Day 06: Prefix Sum - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Problem: Range Sum Query - Immutable (LeetCode 303, Easy)
# Link: https://leetcode.com/problems/range-sum-query-immutable/
# ---------------------------------------------------------
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# ---------------------------------------------------------
# Problem: Subarray Sum Equals K (LeetCode 560, Medium)
# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# ---------------------------------------------------------
# Approach: HashMap + Prefix Sum
class SolutionSubarraySumEqualsK:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        seen = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in seen:
                count += seen[prefix_sum - k]
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
        return count


# ---------------------------------------------------------
# Problem: Continuous Subarray Sum (LeetCode 523, Medium)
# Link: https://leetcode.com/problems/continuous-subarray-sum/
# ---------------------------------------------------------
class SolutionContinuousSubarraySum:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i
        return False


# ---------------------------------------------------------
# Example usage (LeetCode cases)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Range Sum Query - Immutable Example 1:")
    # Input from the problem description
    commands = ["NumArray", "sumRange", "sumRange", "sumRange"]
    args = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

    # Process the commands and arguments
    num_array_instance = None
    outputs = []

    for i in range(len(commands)):
        command = commands[i]
        if command == "NumArray":
            # Create an instance of NumArray
            num_array_instance = NumArray(args[i][0])
            outputs.append(None)  # The constructor returns nothing
        elif command == "sumRange":
            # Call the sumRange method
            left, right = args[i]
            result = num_array_instance.sumRange(left, right)
            outputs.append(result)

    # Print the outputs
    print(outputs)


    print("Subarray Sum Equals K Example 1:", 
          SolutionSubarraySumEqualsK().subarraySum([1,1,1], 2))
    print("Subarray Sum Equals K Example 2:", 
          SolutionSubarraySumEqualsK().subarraySum([1,2,3], 3))


    print("Continuous Subarray Sum Example 1:", 
          SolutionContinuousSubarraySum().checkSubarraySum([23,2,4,6,7], 6))
    print("Continuous Subarray Sum Example 2:", 
          SolutionContinuousSubarraySum().checkSubarraySum([23,2,6,4,7], 6))
    print("Continuous Subarray Sum Example 3:", 
          SolutionContinuousSubarraySum().checkSubarraySum([23,2,6,4,7], 13))
