"""
Day 24: Two Pointers, Greedy, Prefix Sum - LeetCode Problem Solutions
"""

from typing import List

# ---------------------------------------------------------
# Problem: Partition Labels (LeetCode 763, Medium)
# Link: https://leetcode.com/problems/partition-labels/
# ---------------------------------------------------------
class SolutionPartitionLabels:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c: i for i, c in enumerate(s)}
        result = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last_index[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result


# ---------------------------------------------------------
# Problem: Gas Station (LeetCode 134, Medium)
# Link: https://leetcode.com/problems/gas-station/
# ---------------------------------------------------------
class SolutionGasStation:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total, start = 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = i + 1
                total = 0
        return start


# ---------------------------------------------------------
# Problem: Candy (LeetCode 135, Hard)
# Link: https://leetcode.com/problems/candy/
# ---------------------------------------------------------
class SolutionCandy:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Right to left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 763 Example:", SolutionPartitionLabels().partitionLabels("ababcbacadefegdehijhklij"))
    print("Problem 134 Example:", SolutionGasStation().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
    print("Problem 135 Example:", SolutionCandy().candy([1,0,2]))
