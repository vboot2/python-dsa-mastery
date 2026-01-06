"""Day 126: Hash Table - LeetCode Problem Solutions"""

from typing import List
from collections import Counter, defaultdict
import math


# ---------------------------------------------------------
# Problem: X of a Kind in a Deck of Cards (LeetCode 914, Easy)
# Link: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# ---------------------------------------------------------
class SolutionProblemOne:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)
        gcd_val = 0
        for count in freq.values():
            gcd_val = math.gcd(gcd_val, count)
        return gcd_val >= 2


# ---------------------------------------------------------
# Problem: Unique Email Addresses (LeetCode 929, Easy)
# Link: https://leetcode.com/problems/unique-email-addresses/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            seen.add(local + "@" + domain)

        return len(seen)


# ---------------------------------------------------------
# Problem: Verifying an Alien Dictionary (LeetCode 953, Easy)
# Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
# ---------------------------------------------------------
class SolutionProblemThree:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c1, c2 in zip(w1, w2):
                if rank[c1] < rank[c2]:
                    break
                elif rank[c1] > rank[c2]:
                    return False
            else:
                if len(w1) > len(w2):
                    return False

        return True


# ---------------------------------------------------------
# Problem: N-Repeated Element in Size 2N Array (LeetCode 961, Easy)
# Link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# ---------------------------------------------------------
class SolutionProblemFour:
    def repeatedNTimes(self, nums: List[int]):
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)


# ---------------------------------------------------------
# Problem: Find Common Characters (LeetCode 1002, Easy)
# Link: https://leetcode.com/problems/find-common-characters/
# ---------------------------------------------------------
class SolutionProblemFive:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        result = []
        for ch, count in common.items():
            result.extend([ch] * count)

        return result


# ---------------------------------------------------------
# Problem: Relative Sort Array (LeetCode 1122, Easy)
# Link: https://leetcode.com/problems/relative-sort-array/
# ---------------------------------------------------------
class SolutionProblemSix:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        result = []

        for num in arr2:
            result.extend([num] * freq[num])
            freq.pop(num)

        for num in sorted(freq):
            result.extend([num] * freq[num])

        return result


# ---------------------------------------------------------
# Problem: Number of Equivalent Domino Pairs (LeetCode 1128, Easy)
# Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        result = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            result += count[key]
            count[key] += 1

        return result


# ---------------------------------------------------------
# Problem: Find Words That Can Be Formed by Characters (LeetCode 1160, Easy)
# Link: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# ---------------------------------------------------------
class SolutionProblemEight:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0

        for word in words:
            freq = Counter(word)
            if all(freq[c] <= char_count[c] for c in freq):
                total += len(word)

        return total


# ---------------------------------------------------------
# Problem: Maximum Number of Balloons (LeetCode 1189, Easy)
# Link: https://leetcode.com/problems/maximum-number-of-balloons/
# ---------------------------------------------------------
class SolutionProblemNine:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        balloon = Counter("balloon")

        return min(freq[ch] // balloon[ch] for ch in balloon)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("914 Example:", SolutionProblemOne().hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
    print(
        "929 Example:",
        SolutionProblemTwo().numUniqueEmails(
            [
                "test.email+alex@leetcode.com",
                "test.e.mail+bob@leetcode.com",
                "testemail@leetcode.com",
            ]
        ),
    )
    print(
        "953 Example:",
        SolutionProblemThree().isAlienSorted(
            ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
        ),
    )
    print(
        "961 Example:", SolutionProblemFour().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4])
    )
    print(
        "1002 Example:", SolutionProblemFive().commonChars(["bella", "label", "roller"])
    )
    print(
        "1122 Example:",
        SolutionProblemSix().relativeSortArray(
            [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]
        ),
    )
    print(
        "1128 Example:",
        SolutionProblemSeven().numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]),
    )
    print(
        "1160 Example:",
        SolutionProblemEight().countCharacters(["cat", "bt", "hat", "tree"], "atach"),
    )
    print(
        "1189 Example:", SolutionProblemNine().maxNumberOfBalloons("loonbalxballpoon")
    )
