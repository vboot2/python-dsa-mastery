"""
Day 55: Merge Intervals - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Summary Ranges (LeetCode 228, Easy)
# Link: https://leetcode.com/problems/summary-ranges/
# ---------------------------------------------------------


class SolutionProblemOne:
    def solve(self, nums):
        if not nums:
            return []

        res = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                start = nums[i]
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")
        return res


# ---------------------------------------------------------
# Problem: Maximum Count of Positive Integer and Negative Integer
# (LeetCode 2529, Easy)
# Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
# ---------------------------------------------------------


class SolutionProblemTwo:
    def solve(self, nums):
        pos = sum(1 for x in nums if x > 0)
        neg = sum(1 for x in nums if x < 0)
        return max(pos, neg)


# ---------------------------------------------------------
# Problem: Rectangle Area II (LeetCode 850, Hard)
# Link: https://leetcode.com/problems/rectangle-area-ii/
# ---------------------------------------------------------


class SolutionProblemThree:
    def solve(self, rectangles):
        OPEN, CLOSE = 1, -1
        events = []
        y_coords = set()

        for x1, y1, x2, y2 in rectangles:
            events.append((x1, OPEN, y1, y2))
            events.append((x2, CLOSE, y1, y2))
            y_coords.update([y1, y2])

        y_list = sorted(y_coords)
        y_index = {v: i for i, v in enumerate(y_list)}
        active = [0] * len(y_list)

        def compute_y_coverage():
            covered = 0
            count = 0
            for i in range(len(y_list) - 1):
                if active[i] > 0:
                    covered += y_list[i + 1] - y_list[i]
            return covered

        events.sort()
        prev_x = 0
        prev_y_coverage = 0
        area = 0
        MOD = 10**9 + 7

        for x, typ, y1, y2 in events:
            area += (x - prev_x) * prev_y_coverage
            for i in range(y_index[y1], y_index[y2]):
                active[i] += typ
            prev_x = x
            prev_y_coverage = compute_y_coverage()

        return area % MOD


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().solve([0, 1, 2, 4, 5, 7]))
    print("Problem Two Example:", SolutionProblemTwo().solve([-5, -3, -1, 0, 2, 3, 4]))
    print(
        "Problem Three Example:",
        SolutionProblemThree().solve([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]),
    )
