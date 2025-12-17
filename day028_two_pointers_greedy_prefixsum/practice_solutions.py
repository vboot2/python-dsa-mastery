"""
Day 28: Two Pointers, Greedy, Prefix Sum - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Interval List Intersections (LeetCode 986, Medium)
# Link: https://leetcode.com/problems/interval-list-intersections/
# ---------------------------------------------------------
class SolutionIntervalIntersections:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            # Compute overlap
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                res.append([start, end])

            # Move pointer with smaller end
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res


# ---------------------------------------------------------
# Problem 2: Remove Covered Intervals (LeetCode 1288, Medium)
# Link: https://leetcode.com/problems/remove-covered-intervals/
# ---------------------------------------------------------
class SolutionRemoveCovered:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        # Sort: start ascending, end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        prev_end = 0

        for _, end in intervals:
            if end > prev_end:
                count += 1
                prev_end = end

        return count


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Interval Intersections:",
          SolutionIntervalIntersections().intervalIntersection(
              [[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]
          ))

    print("Remove Covered Intervals:",
          SolutionRemoveCovered().removeCoveredIntervals([[1,4],[3,6],[2,8]]))
