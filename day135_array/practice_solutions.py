"""Day 135: Array - LeetCode Problem Solutions"""

from typing import List


# ---------------------------------------------------------
# Problem: Count Primes (LeetCode 204, Medium)
# ---------------------------------------------------------
class SolutionProblemOne:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)


# ---------------------------------------------------------
# Problem: H-Index (LeetCode 274, Medium)
# ---------------------------------------------------------
class SolutionProblemTwo:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0

        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
        return h


# ---------------------------------------------------------
# Problem: H-Index II (LeetCode 275, Medium)
# ---------------------------------------------------------
class SolutionProblemThree:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1

        return n - left


# ---------------------------------------------------------
# Problem: Peeking Iterator (LeetCode 284, Medium)
# ---------------------------------------------------------
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_elem = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.next_elem

    def next(self):
        curr = self.next_elem
        self.next_elem = self.iterator.next() if self.iterator.hasNext() else None
        return curr

    def hasNext(self):
        return self.next_elem is not None


# ---------------------------------------------------------
# Problem: Sudoku Solver (LeetCode 37, Hard)
# ---------------------------------------------------------
class SolutionProblemFour:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r // 3) * 3 + c // 3].add(board[r][c])

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != ".":
                return backtrack(r, c + 1)

            for num in map(str, range(1, 10)):
                box_id = (r // 3) * 3 + c // 3
                if (
                    num not in rows[r]
                    and num not in cols[c]
                    and num not in boxes[box_id]
                ):
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)

                    if backtrack(r, c + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_id].remove(num)

            return False

        backtrack(0, 0)


# ---------------------------------------------------------
# Problem: Text Justification (LeetCode 68, Hard)
# ---------------------------------------------------------
class SolutionProblemFive:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, line, length = [], [], 0

        for w in words:
            if length + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - length):
                    line[i % (len(line) - 1 or 1)] += " "
                res.append("".join(line))
                line, length = [], 0
            line.append(w)
            length += len(w)

        res.append(" ".join(line).ljust(maxWidth))
        return res


# ---------------------------------------------------------
# Problem: Best Time to Buy and Sell Stock III (LeetCode 123, Hard)
# ---------------------------------------------------------
class SolutionProblemSix:
    def maxProfit(self, prices: List[int]):
        buy1 = buy2 = float("inf")
        profit1 = profit2 = 0

        for p in prices:
            buy1 = min(buy1, p)
            profit1 = max(profit1, p - buy1)
            buy2 = min(buy2, p - profit1)
            profit2 = max(profit2, p - buy2)

        return profit2


# ---------------------------------------------------------
# Problem: Find Minimum in Rotated Sorted Array II (LeetCode 154, Hard)
# ---------------------------------------------------------
class SolutionProblemSeven:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]


# ---------------------------------------------------------
# Problem: Best Time to Buy and Sell Stock IV (LeetCode 188, Hard)
# ---------------------------------------------------------
class SolutionProblemEight:
    def maxProfit(self, k: int, prices) -> int:
        if not prices:
            return 0

        if k >= len(prices) // 2:
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))

        dp_buy = [float("inf")] * (k + 1)
        dp_sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                dp_buy[i] = min(dp_buy[i], price - dp_sell[i - 1])
                dp_sell[i] = max(dp_sell[i], price - dp_buy[i])

        return dp_sell[k]


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("204 Example:", SolutionProblemOne().countPrimes(20))
    print("274 Example:", SolutionProblemTwo().hIndex([3, 0, 6, 1, 5]))
    print("275 Example:", SolutionProblemThree().hIndex([0, 1, 3, 5, 6]))
    print("123 Example:", SolutionProblemSix().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
