"""
Day 27: Two Pointers, Greedy, Prefix Sum - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Merge Intervals (LeetCode 56, Medium)
# Link: https://leetcode.com/problems/merge-intervals/
# ---------------------------------------------------------
class Solution56:
    def merge(self, intervals):
        # 🔹 Sort by start time
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)  # no overlap
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])  # merge
        return merged


# ---------------------------------------------------------
# Problem: Insert Interval (LeetCode 57, Medium)
# Link: https://leetcode.com/problems/insert-interval/
# ---------------------------------------------------------
class Solution57:
    def insert(self, intervals, newInterval):
        res = []
        for i in range(len(intervals)):
            # Before newInterval
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            # After newInterval
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            # Overlap case
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        res.append(newInterval)
        return res


# ---------------------------------------------------------
# Problem: Non-overlapping Intervals (LeetCode 435, Medium)
# Link: https://leetcode.com/problems/non-overlapping-intervals/
# ---------------------------------------------------------
class Solution435:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        # 🔹 Sort by end time
        intervals.sort(key=lambda x: x[1])
        count, end = 0, intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1  # overlap, remove
            else:
                end = intervals[i][1]  # update end
        return count


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 56 Example:", Solution56().merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
    print("Problem 57 Example:", Solution57().insert([[1,3],[6,9]], [2,5]))  # [[1,5],[6,9]]
    print("Problem 435 Example:", Solution435().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # 1
