""" Day 114: Array - LeetCode Problem Solutions """

from typing import List


# ---------------------------------------------------------
# Problem: Find All Numbers Disappeared in an Array (LeetCode 448, Easy)
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# ---------------------------------------------------------
class SolutionProblemOne:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# ---------------------------------------------------------
# Problem: Island Perimeter (LeetCode 463, Easy)
# Link: https://leetcode.com/problems/island-perimeter/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2

        return perimeter


# ---------------------------------------------------------
# Problem: Max Consecutive Ones (LeetCode 485, Easy)
# Link: https://leetcode.com/problems/max-consecutive-ones/
# ---------------------------------------------------------
class SolutionProblemThree:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count


# ---------------------------------------------------------
# Problem: Teemo Attacking (LeetCode 495, Easy)
# Link: https://leetcode.com/problems/teemo-attacking/
# ---------------------------------------------------------
class SolutionProblemFour:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total = 0
        for i in range(len(timeSeries) - 1):
            total += min(duration, timeSeries[i + 1] - timeSeries[i])

        return total + duration


# ---------------------------------------------------------
# Problem: Keyboard Row (LeetCode 500, Easy)
# Link: https://leetcode.com/problems/keyboard-row/
# ---------------------------------------------------------
class SolutionProblemFive:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        result = []
        for word in words:
            lower = set(word.lower())
            for row in rows:
                if lower <= row:
                    result.append(word)
                    break

        return result


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print("Problem Two Example:", SolutionProblemTwo().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print("Problem Three Example:", SolutionProblemThree().findMaxConsecutiveOnes([1,1,0,1,1,1]))
    print("Problem Four Example:", SolutionProblemFour().findPoisonedDuration([1,4], 2))
    print("Problem Five Example:", SolutionProblemFive().findWords(["Hello","Alaska","Dad","Peace"]))
