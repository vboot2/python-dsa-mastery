"""
Day 20: Recursion, Sorting, Searching - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Partition to K Equal Sum Subsets (LeetCode 698, Medium)
# Link: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# ---------------------------------------------------------
class SolutionPartitionK:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)  # helps prune early
        
        n = len(nums)
        used = 0   # bitmask: 0 = unused, 1 = used
        memo = {}

        def backtrack(k_left, current_sum, start, used):
            if k_left == 1:  # last group will always be valid
                return True
            if (used, k_left, current_sum) in memo:
                return memo[(used, k_left, current_sum)]
            
            if current_sum == target:  
                # one bucket complete → move to next
                res = backtrack(k_left-1, 0, 0, used)
                memo[(used, k_left, current_sum)] = res
                return res

            for i in range(start, n):
                if not (used >> i) & 1 and current_sum + nums[i] <= target:
                    if backtrack(k_left, current_sum + nums[i], i+1, used | (1 << i)):
                        memo[(used, k_left, current_sum)] = True
                        return True

            memo[(used, k_left, current_sum)] = False
            return False

        return backtrack(k, 0, 0, used)


# ---------------------------------------------------------
# Problem 2: Letter Case Permutation (LeetCode 784, Medium)
# Link: https://leetcode.com/problems/letter-case-permutation/
# ---------------------------------------------------------
class SolutionLetterCase:
    def letterCasePermutation(self, s: str):
        res = []

        def backtrack(i, path):
            if i == len(s):
                res.append(path)
                return
            if s[i].isalpha():
                backtrack(i+1, path + s[i].lower())
                backtrack(i+1, path + s[i].upper())
            else:
                backtrack(i+1, path + s[i])

        backtrack(0, "")
        return res


# ---------------------------------------------------------
# Problem 3: Combination Sum III (LeetCode 216, Medium)
# Link: https://leetcode.com/problems/combination-sum-iii/
# ---------------------------------------------------------
class SolutionCombinationSum3:
    def combinationSum3(self, k: int, n: int):
        res = []

        def backtrack(start, comb, remaining):
            if len(comb) == k and remaining == 0:
                res.append(list(comb))
                return
            for i in range(start, 10):
                if remaining - i >= 0:
                    comb.append(i)
                    backtrack(i+1, comb, remaining-i)
                    comb.pop()

        backtrack(1, [], n)
        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Partition K Equal Sum Subsets:", SolutionPartitionK().canPartitionKSubsets([4,3,2,3,5,2,1], 4))
    print("Letter Case Permutation:", SolutionLetterCase().letterCasePermutation("a1b2"))
    print("Combination Sum III:", SolutionCombinationSum3().combinationSum3(3, 7))
