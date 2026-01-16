"""Day 136: Hash Table - LeetCode Problem Solutions"""

from typing import List
from collections import defaultdict, Counter, deque


# ---------------------------------------------------------
# Problem: Destination City (LeetCode 1436, Easy)
# Link: https://leetcode.com/problems/destination-city/
# ---------------------------------------------------------
class SolutionProblemOne:
    def destCity(self, paths: List[List[str]]):
        outgoing = set()
        for a, b in paths:
            outgoing.add(a)

        for a, b in paths:
            if b not in outgoing:
                return b


# ---------------------------------------------------------
# Problem: Make Two Arrays Equal by Reversing Subarrays (LeetCode 1460, Easy)
# Link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


# ---------------------------------------------------------
# Problem: Path Crossing (LeetCode 1496, Easy)
# Link: https://leetcode.com/problems/path-crossing/
# ---------------------------------------------------------
class SolutionProblemThree:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        visited = {(0, 0)}

        for p in path:
            if p == "N":
                y += 1
            elif p == "S":
                y -= 1
            elif p == "E":
                x += 1
            else:
                x -= 1

            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False


# ---------------------------------------------------------
# Problem: Integer to Roman (LeetCode 12, Medium)
# Link: https://leetcode.com/problems/integer-to-roman/
# ---------------------------------------------------------
class SolutionProblemFour:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        res = []
        for v, s in values:
            while num >= v:
                num -= v
                res.append(s)

        return "".join(res)


# ---------------------------------------------------------
# Problem: Fraction to Recurring Decimal (LeetCode 166, Medium)
# Link: https://leetcode.com/problems/fraction-to-recurring-decimal/
# ---------------------------------------------------------
class SolutionProblemFive:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(res)

        res.append(".")
        seen = {}

        while remainder != 0:
            if remainder in seen:
                idx = seen[remainder]
                res.insert(idx, "(")
                res.append(")")
                break

            seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)


# ---------------------------------------------------------
# Problem: Repeated DNA Sequences (LeetCode 187, Medium)
# Link: https://leetcode.com/problems/repeated-dna-sequences/
# ---------------------------------------------------------
class SolutionProblemSix:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            sub = s[i : i + 10]
            if sub in seen:
                repeated.add(sub)
            else:
                seen.add(sub)

        return list(repeated)


# ---------------------------------------------------------
# Problem: Word Ladder II (LeetCode 126, Hard)
# Link: https://leetcode.com/problems/word-ladder-ii/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        L = len(beginWord)
        generic = defaultdict(list)
        for w in word_set:
            for i in range(L):
                generic[w[:i] + "*" + w[i + 1 :]].append(w)
        parents = defaultdict(list)
        frontier = {beginWord}
        found = False

        while frontier and not found:
            next_front = set()
            word_set -= frontier

            for w in frontier:
                for i in range(L):
                    pattern = w[:i] + "*" + w[i + 1 :]
                    for nb in generic[pattern]:
                        if nb not in word_set:
                            continue
                        parents[nb].append(w)
                        if nb == endWord:
                            found = True
                        next_front.add(nb)

            frontier = next_front

        if not found:
            return []
        results: List[List[str]] = []

        def dfs(cur: str, path: List[str]) -> None:
            """Walk backwards from `cur` to `beginWord` using `parents`."""
            if cur == beginWord:
                results.append([beginWord] + path[::-1])
                return
            for pred in parents[cur]:
                dfs(pred, path + [cur])

        dfs(endWord, [])
        return results


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "1436 Example:",
        SolutionProblemOne().destCity(
            [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
        ),
    )
    print("1460 Example:", SolutionProblemTwo().canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
    print("1496 Example:", SolutionProblemThree().isPathCrossing("NESWW"))
    print("12 Example:", SolutionProblemFour().intToRoman(1994))
    print("166 Example:", SolutionProblemFive().fractionToDecimal(4, 333))
    print(
        "187 Example:",
        SolutionProblemSix().findRepeatedDnaSequences(
            "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        ),
    )
