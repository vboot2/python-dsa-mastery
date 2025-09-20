"""
Day 20: Recursion, Sorting, Searching
"""

# ---------------------------------------------------------
# Example 1: Partition to K Equal Sum Subsets
# ---------------------------------------------------------
def can_partition_k_subsets(nums, k):
    total = sum(nums)
    if total % k != 0:
        return False

    target = total // k
    nums.sort(reverse=True)
    used = [False] * len(nums)

    def backtrack(start, k_left, current_sum):
        if k_left == 0:
            return True
        if current_sum == target:
            return backtrack(0, k_left-1, 0)

        for i in range(start, len(nums)):
            if not used[i] and current_sum + nums[i] <= target:
                used[i] = True
                if backtrack(i+1, k_left, current_sum+nums[i]):
                    return True
                used[i] = False
        return False

    return backtrack(0, k, 0)

print("Partition to K Subsets [4,3,2,3,5,2,1], k=4:", can_partition_k_subsets([4,3,2,3,5,2,1], 4))


# ---------------------------------------------------------
# Example 2: Letter Case Permutation
# ---------------------------------------------------------
def letter_case_permutation(s: str):
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

print("Letter Case Permutation for 'a1b2':", letter_case_permutation("a1b2"))


# ---------------------------------------------------------
# Example 3: Combination Sum III
# ---------------------------------------------------------
def combination_sum3(k, n):
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

print("Combination Sum III (k=3, n=7):", combination_sum3(3, 7))
