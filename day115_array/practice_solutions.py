""" Day 115: Array - LeetCode Problem Solutions """

from typing import List


# ---------------------------------------------------------
# Problem: Relative Ranks (LeetCode 506, Easy)
# Link: https://leetcode.com/problems/relative-ranks/
# ---------------------------------------------------------
class SolutionProblemOne:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        rank_map = {}

        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)

        return [rank_map[s] for s in score]


# ---------------------------------------------------------
# Problem: Array Partition I (LeetCode 561, Easy)
# Link: https://leetcode.com/problems/array-partition-i/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0

        for i in range(0, len(nums), 2):
            total += nums[i]

        return total


# ---------------------------------------------------------
# Problem: Reshape the Matrix (LeetCode 566, Easy)
# Link: https://leetcode.com/problems/reshape-the-matrix/
# ---------------------------------------------------------
class SolutionProblemThree:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = [num for row in mat for num in row]

        if len(flat) != r * c:
            return mat

        result = []
        idx = 0
        for _ in range(r):
            result.append(flat[idx:idx + c])
            idx += c

        return result


# ---------------------------------------------------------
# Problem: Distribute Candies (LeetCode 575, Easy)
# Link: https://leetcode.com/problems/distribute-candies/
# ---------------------------------------------------------
class SolutionProblemFour:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique = len(set(candyType))
        return min(unique, len(candyType) // 2)


# ---------------------------------------------------------
# Problem: Longest Harmonious Subsequence (LeetCode 594, Easy)
# Link: https://leetcode.com/problems/longest-harmonious-subsequence/
# ---------------------------------------------------------
class SolutionProblemFive:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        longest = 0
        for k in freq:
            if k + 1 in freq:
                longest = max(longest, freq[k] + freq[k + 1])

        return longest


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().findRelativeRanks([10,3,8,9,4]))
    print("Problem Two Example:", SolutionProblemTwo().arrayPairSum([1,4,3,2]))
    print("Problem Three Example:", SolutionProblemThree().matrixReshape([[1,2],[3,4]], 1, 4))
    print("Problem Four Example:", SolutionProblemFour().distributeCandies([1,1,2,2,3,3]))
    print("Problem Five Example:", SolutionProblemFive().findLHS([1,3,2,2,5,2,3,7]))
