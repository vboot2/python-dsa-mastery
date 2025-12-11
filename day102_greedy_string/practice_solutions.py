"""
Day 102: Greedy/String - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Problem: Assign Cookies (LeetCode 455, Easy)
# Link: https://leetcode.com/problems/assign-cookies/
# ---------------------------------------------------------
class SolutionProblemOne:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Greedy:
        - Sort children by greed factor
        - Sort cookie sizes
        - Assign smallest cookie that satisfies each child's greed
        """
        g.sort()
        s.sort()

        i = j = 0
        count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count


# ---------------------------------------------------------
# Problem: Score After Flipping Matrix (LeetCode 861, Medium)
# Link: https://leetcode.com/problems/score-after-flipping-matrix/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def matrixScore(self, grid: List[List[int]]) -> int:
        """
        Greedy:
        - First ensure MSB of each row is 1 (flip row if needed)
        - For each column, flip if number of zeros > number of ones
        - Final value = sum of binary numbers from rows
        """
        rows = len(grid)
        cols = len(grid[0])

        # Step 1: flip rows with 0 in MSB (first column)
        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    grid[r][c] ^= 1

        # Step 2: flip columns if more zeros than ones
        for c in range(cols):
            ones = sum(grid[r][c] for r in range(rows))
            zeros = rows - ones

            if zeros > ones:
                for r in range(rows):
                    grid[r][c] ^= 1

        # Step 3: compute total score
        total = 0
        for r in range(rows):
            value = 0
            for c in range(cols):
                value = (value << 1) + grid[r][c]
            total += value

        return total


# ---------------------------------------------------------
# Problem: Valid Number (LeetCode 65, Hard)
# Link: https://leetcode.com/problems/valid-number/
# ---------------------------------------------------------
class SolutionProblemThree:
    def isNumber(self, s: str) -> bool:
        """
        Greedy + FSM-like approach:
        Valid patterns:
        - optional sign
        - digits
        - optional dot with digits
        - optional exponent with sign and digits

        Track flags:
        - seen_digit
        - seen_dot
        - seen_exponent
        """
        s = s.strip()

        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch in ['+', '-']:
                # sign allowed only at start or right after 'e'
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif ch == '.':
                # only one dot allowed, and cannot appear after exponent
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif ch in ['e', 'E']:
                # exponent only allowed once, and must follow a digit
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False  # reset: exponent must be followed by digit
            else:
                return False

        return seen_digit


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:",
          SolutionProblemOne().findContentChildren([1, 2, 3], [1, 1]))
    print("Problem Two Example:",
          SolutionProblemTwo().matrixScore([[0, 0, 1], [1, 1, 1]]))
    print("Problem Three Example:",
          SolutionProblemThree().isNumber("53.5e93"))
