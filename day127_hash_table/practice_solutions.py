"""Day 127: Hash Table - LeetCode Problem Solutions"""

from typing import List
from collections import Counter, defaultdict


# ---------------------------------------------------------
# Problem: Unique Number of Occurrences (LeetCode 1207, Easy)
# Link: https://leetcode.com/problems/unique-number-of-occurrences/
# ---------------------------------------------------------
class SolutionProblemOne:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        return len(freq.values()) == len(set(freq.values()))


# ---------------------------------------------------------
# Problem: Find Winner on a Tic Tac Toe Game (LeetCode 1275, Easy)
# Link: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = defaultdict(int)
        cols = defaultdict(int)
        diag = anti = 0

        for i, (r, c) in enumerate(moves):
            player = 1 if i % 2 == 0 else -1
            rows[r] += player
            cols[c] += player
            if r == c:
                diag += player
            if r + c == 2:
                anti += player
            if (
                abs(rows[r]) == 3
                or abs(cols[c]) == 3
                or abs(diag) == 3
                or abs(anti) == 3
            ):
                return "A" if player == 1 else "B"

        return "Draw" if len(moves) == 9 else "Pending"


# ---------------------------------------------------------
# Problem: Rank Transform of an Array (LeetCode 1331, Easy)
# Link: https://leetcode.com/problems/rank-transform-of-an-array/
# ---------------------------------------------------------
class SolutionProblemThree:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
        return [rank[x] for x in arr]


# ---------------------------------------------------------
# Problem: Check If N and Its Double Exist (LeetCode 1346, Easy)
# Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/
# ---------------------------------------------------------
class SolutionProblemFour:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for n in arr:
            if 2 * n in seen or (n % 2 == 0 and n // 2 in seen):
                return True
            seen.add(n)
        return False


# ---------------------------------------------------------
# Problem: How Many Numbers Are Smaller Than the Current Number (LeetCode 1365, Easy)
# Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# ---------------------------------------------------------
class SolutionProblemFive:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        first_index = {}

        for i, n in enumerate(sorted_nums):
            if n not in first_index:
                first_index[n] = i

        return [first_index[n] for n in nums]


# ---------------------------------------------------------
# Problem: Increasing Decreasing String (LeetCode 1370, Easy)
# Link: https://leetcode.com/problems/increasing-decreasing-string/
# ---------------------------------------------------------
class SolutionProblemSix:
    def sortString(self, s: str) -> str:
        freq = Counter(s)
        result = []

        while len(result) < len(s):
            for ch in sorted(freq):
                if freq[ch] > 0:
                    result.append(ch)
                    freq[ch] -= 1
            for ch in sorted(freq, reverse=True):
                if freq[ch] > 0:
                    result.append(ch)
                    freq[ch] -= 1

        return "".join(result)


# ---------------------------------------------------------
# Problem: Find Lucky Integer in an Array (LeetCode 1394, Easy)
# Link: https://leetcode.com/problems/find-lucky-integer-in-an-array/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        lucky = -1

        for num, count in freq.items():
            if num == count:
                lucky = max(lucky, num)

        return lucky


# ---------------------------------------------------------
# Problem: Count Largest Group (LeetCode 1399, Easy)
# Link: https://leetcode.com/problems/count-largest-group/
# ---------------------------------------------------------
class SolutionProblemEight:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            groups[digit_sum] += 1

        max_size = max(groups.values())
        return sum(1 for size in groups.values() if size == max_size)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("1207 Example:", SolutionProblemOne().uniqueOccurrences([1, 2, 2, 1, 1, 3]))
    print(
        "1275 Example:",
        SolutionProblemTwo().tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]),
    )
    print("1331 Example:", SolutionProblemThree().arrayRankTransform([40, 10, 20, 30]))
    print("1346 Example:", SolutionProblemFour().checkIfExist([10, 2, 5, 3]))
    print(
        "1365 Example:",
        SolutionProblemFive().smallerNumbersThanCurrent([8, 1, 2, 2, 3]),
    )
    print("1370 Example:", SolutionProblemSix().sortString("aaaabbbbcccc"))
    print("1394 Example:", SolutionProblemSeven().findLucky([2, 2, 3, 4]))
    print("1399 Example:", SolutionProblemEight().countLargestGroup(13))
