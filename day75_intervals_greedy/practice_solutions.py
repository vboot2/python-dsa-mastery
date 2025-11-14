"""
Day 75: Intervals / Greedy - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Minimum Number of Arrows to Burst Balloons (LeetCode 452, Medium)
# Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# ---------------------------------------------------------
class SolutionMinArrows:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])  # sort by ending point
        arrows = 1
        end = points[0][1]

        for s, e in points[1:]:
            if s > end:      # need new arrow
                arrows += 1
                end = e
        return arrows


# ---------------------------------------------------------
# Problem 2: Corporate Flight Bookings (LeetCode 1109, Medium)
# Link: https://leetcode.com/problems/corporate-flight-bookings/
# ---------------------------------------------------------
class SolutionFlightBookings:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff = [0] * (n + 1)

        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        result = []
        running = 0
        for i in range(n):
            running += diff[i]
            result.append(running)

        return result


# ---------------------------------------------------------
# Example usage (quick test)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Min Arrows:", SolutionMinArrows().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))  # 2
    print("Flight Bookings:", SolutionFlightBookings().corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))
    # [10,55,45,25,25]
