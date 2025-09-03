"""
Day 03: Hashing - LeetCode Problem Solutions
"""

from typing import List

# ---------------------------------------------------------
# Problem: Happy Number (LeetCode 202, Easy)
# Link: https://leetcode.com/problems/happy-number/
# ---------------------------------------------------------
class SolutionHappyNumber:
    def isHappy(self, n: int) -> bool:
        # Enforce constraints: 1 <= n <= 2^31 - 1
        if not (1 <= n <= 2**31 - 1):
            raise ValueError("Input n must be in the range 1 <= n <= 2^31 - 1")

        def get_next(num):
            return sum(int(ch) ** 2 for ch in str(num))
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


# ---------------------------------------------------------
# Problem: Group Anagrams (LeetCode 49, Medium)
# Link: https://leetcode.com/problems/group-anagrams/
# ---------------------------------------------------------
class SolutionGroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values())


# ---------------------------------------------------------
# Problem: Top K Frequent Elements (LeetCode 347, Medium)
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# ---------------------------------------------------------
class SolutionTopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        return [item for item, count in freq.most_common(k)]


# ---------------------------------------------------------
# Example usage (LeetCode cases)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Happy Number Example 1:", SolutionHappyNumber().isHappy(19))
    print("Happy Number Example 2:", SolutionHappyNumber().isHappy(2))
    print("Group Anagram Example 1:", SolutionGroupAnagrams().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print("Group Anagram Example 2:", SolutionGroupAnagrams().groupAnagrams([""]))
    print("Group Anagram Example 3:", SolutionGroupAnagrams().groupAnagrams(["a"]))
    print("Top K Frequent Elements Example 1:", SolutionTopKFrequent().topKFrequent([1,1,1,2,2,3], 2))
    print("Top K Frequent Elements Example 2:", SolutionTopKFrequent().topKFrequent([1], 1))
    print("Top K Frequent Elements Example 3:", SolutionTopKFrequent().topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))
