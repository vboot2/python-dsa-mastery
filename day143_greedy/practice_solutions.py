"""Day 143: Greedy - LeetCode Problem Solutions"""

from typing import List
import heapq
from collections import Counter, defaultdict, deque


# ---------------------------------------------------------
# Problem: Integer Replacement (LeetCode 397)
# Link: https://leetcode.com/problems/integer-replacement/
# ---------------------------------------------------------
class SolutionProblemOne:
    def integerReplacement(self, n: int) -> int:
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3:
                    n -= 1
                else:
                    if n & 3 == 1:
                        n -= 1
                    else:
                        n += 1
            steps += 1
        return steps


# ---------------------------------------------------------
# Problem: Valid Triangle Number (LeetCode 611)
# Link: https://leetcode.com/problems/valid-triangle-number/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for k in range(len(nums) - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i
                    j -= 1
                else:
                    i += 1
        return res


# ---------------------------------------------------------
# Problem: Maximum Distance in Arrays (LeetCode 624)
# Link: https://leetcode.com/problems/maximum-distance-in-arrays/
# ---------------------------------------------------------
class SolutionProblemThree:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val, max_val = arrays[0][0], arrays[0][-1]
        res = 0

        for arr in arrays[1:]:
            res = max(res, abs(arr[-1] - min_val), abs(max_val - arr[0]))
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])

        return res


# ---------------------------------------------------------
# Problem: Maximum Length of Pair Chain (LeetCode 646)
# Link: https://leetcode.com/problems/maximum-length-of-pair-chain/
# ---------------------------------------------------------
class SolutionProblemFour:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        curr_end = float("-inf")
        res = 0

        for a, b in pairs:
            if a > curr_end:
                curr_end = b
                res += 1
        return res


# ---------------------------------------------------------
# Problem: Dota2 Senate (LeetCode 649)
# Link: https://leetcode.com/problems/dota2-senate/
# ---------------------------------------------------------
class SolutionProblemFive:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"


# ---------------------------------------------------------
# Problem: Split Array into Consecutive Subsequences (LeetCode 659)
# Link: https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# ---------------------------------------------------------
class SolutionProblemSix:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need = Counter()

        for n in nums:
            if freq[n] == 0:
                continue
            if need[n] > 0:
                need[n] -= 1
                need[n + 1] += 1
            elif freq[n + 1] > 0 and freq[n + 2] > 0:
                freq[n + 1] -= 1
                freq[n + 2] -= 1
                need[n + 3] += 1
            else:
                return False
            freq[n] -= 1
        return True


# ---------------------------------------------------------
# Problem: Maximum Swap (LeetCode 670)
# Link: https://leetcode.com/problems/maximum-swap/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {d: i for i, d in enumerate(digits)}

        for i, d in enumerate(digits):
            for x in map(str, range(9, int(d), -1)):
                if x in last and last[x] > i:
                    digits[i], digits[last[x]] = digits[last[x]], digits[i]
                    return int("".join(digits))
        return num


# ---------------------------------------------------------
# Problem: Valid Parenthesis String (LeetCode 678)
# Link: https://leetcode.com/problems/valid-parenthesis-string/
# ---------------------------------------------------------
class SolutionProblemEight:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for elem in s:

            if elem == "(":
                low += 1
                high += 1
            elif elem == ")":
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1

            low = max(low, 0)
            if high < 0:
                return False
        return low == 0


# ---------------------------------------------------------
# Problem: Strong Password Checker (LeetCode 420)
# Link: https://leetcode.com/problems/strong-password-checker/
# ---------------------------------------------------------
class SolutionProblemNine:
    def strongPasswordChecker(self, password: str) -> int:
        missing_types = 3
        if any(c.islower() for c in password):
            missing_types -= 1
        if any(c.isupper() for c in password):
            missing_types -= 1
        if any(c.isdigit() for c in password):
            missing_types -= 1

        repeats = []
        i = 0
        n = len(password)
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            group_len = j - i
            if group_len >= 3:
                repeats.append(group_len)
            i = j

        if n < 6:
            return max(missing_types, 6 - n)

        if n <= 20:
            replace_needed = sum(g // 3 for g in repeats)
            return max(missing_types, replace_needed)

        over_len = n - 20
        replace_needed = 0

        buckets = [[], [], []]
        for g in repeats:
            buckets[g % 3].append(g)

        def apply_deletions(bucket, cost_per_reduce):
            nonlocal over_len, replace_needed
            for idx in range(len(bucket)):
                if over_len <= 0:
                    break

                deletions = min(cost_per_reduce, over_len)
                bucket[idx] -= deletions
                over_len -= deletions

                if bucket[idx] < 3:
                    continue

        for i in range(len(buckets[0])):
            if over_len == 0:
                break

            del_cnt = min(1, over_len)
            buckets[0][i] -= del_cnt
            over_len -= del_cnt

        for i in range(len(buckets[1])):
            if over_len == 0:
                break
            del_cnt = min(2, over_len)
            buckets[1][i] -= del_cnt
            over_len -= del_cnt

        all_remaining = buckets[0] + buckets[1] + buckets[2]
        for i in range(len(all_remaining)):
            if over_len == 0:
                break

            remove = min(over_len, all_remaining[i] - 2)
            remove = (remove // 3) * 3
            all_remaining[i] -= remove
            over_len -= remove

        replace_needed = sum(g // 3 for g in all_remaining if g >= 3)

        return (n - 20) + max(missing_types, replace_needed)


# ---------------------------------------------------------
# Problem: IPO (LeetCode 502)
# Link: https://leetcode.com/problems/ipo/
# ---------------------------------------------------------
class SolutionProblemTen:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        projects = sorted(zip(capital, profits))
        heap = []
        i = 0

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            if not heap:
                break
            w += -heapq.heappop(heap)
        return w


# ---------------------------------------------------------
# Problem: Super Washing Machines (LeetCode 517)
# Link: https://leetcode.com/problems/super-washing-machines/
# ---------------------------------------------------------
class SolutionProblemEleven:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        if total % len(machines) != 0:
            return -1

        avg = total // len(machines)
        res = curr = 0

        for m in machines:
            curr += m - avg
            res = max(res, abs(curr), m - avg)
        return res


# ---------------------------------------------------------
# Problem: Smallest Range Covering Elements from K Lists (LeetCode 632)
# Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# ---------------------------------------------------------
class SolutionProblemTwelve:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_val = float("-inf")

        for i, lst in enumerate(nums):
            heap.append((lst[0], i, 0))
            max_val = max(max_val, lst[0])

        heapq.heapify(heap)
        res = [-(10**9), 10**9]

        while True:
            val, r, c = heapq.heappop(heap)
            if max_val - val < res[1] - res[0]:
                res = [val, max_val]
            if c + 1 == len(nums[r]):
                break
            nxt = nums[r][c + 1]
            heapq.heappush(heap, (nxt, r, c + 1))
            max_val = max(max_val, nxt)

        return res
