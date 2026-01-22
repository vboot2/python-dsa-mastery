"""Day 142: Two Pointers - LeetCode Problem Solutions"""

from typing import List
from collections import Counter, defaultdict
import bisect


# ---------------------------------------------------------
# Problem: Remove Duplicates from Sorted List II (LeetCode 82)
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# ---------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionProblemOne:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next


# ---------------------------------------------------------
# Problem: Reorder List (LeetCode 143)
# Link: https://leetcode.com/problems/reorder-list/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def reorderList(self, head) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev
        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


# ---------------------------------------------------------
# Problem: String Compression (LeetCode 443)
# Link: https://leetcode.com/problems/string-compression/
# ---------------------------------------------------------
class SolutionProblemThree:
    def compress(self, chars: List[str]) -> int:
        write = i = 0
        n = len(chars)

        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[write] = chars[i]
            write += 1
            if j - i > 1:
                for c in str(j - i):
                    chars[write] = c
                    write += 1
            i = j
        return write


# ---------------------------------------------------------
# Problem: Magical String (LeetCode 481)
# Link: https://leetcode.com/problems/magical-string/
# ---------------------------------------------------------
class SolutionProblemFour:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        i = 2
        num = 1

        while len(s) < n:
            s.extend([num] * s[i])
            num = 3 - num
            i += 1
        return s[:n].count(1)


# ---------------------------------------------------------
# Problem: Longest Uncommon Subsequence II (LeetCode 522)
# Link: https://leetcode.com/problems/longest-uncommon-subsequence-ii/
# ---------------------------------------------------------
class SolutionProblemFive:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(a, b):
            it = iter(b)
            return all(c in it for c in a)

        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            if all(not is_subseq(s, t) for j, t in enumerate(strs) if i != j):
                return len(s)
        return -1


# ---------------------------------------------------------
# Problem: Longest Word in Dictionary through Deleting (LeetCode 524)
# Link: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
# ---------------------------------------------------------
class SolutionProblemSix:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subseq(word):
            it = iter(s)
            return all(c in it for c in word)

        dictionary.sort(key=lambda x: (-len(x), x))
        for w in dictionary:
            if is_subseq(w):
                return w
        return ""


# ---------------------------------------------------------
# Problem: K-diff Pairs in an Array (LeetCode 532)
# Link: https://leetcode.com/problems/k-diff-pairs-in-an-array/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        nums.sort()
        left = 0
        res = set()

        for right in range(1, len(nums)):
            while nums[right] - nums[left] > k:
                left += 1
            if nums[right] - nums[left] == k and left != right:
                res.add((nums[left], nums[right]))
        return len(res)


# ---------------------------------------------------------
# Problem: Next Greater Element III (LeetCode 556)
# Link: https://leetcode.com/problems/next-greater-element-iii/
# ---------------------------------------------------------
class SolutionProblemEight:
    def nextGreaterElement(self, n: int) -> int:
        arr = list(str(n))
        i = len(arr) - 2

        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i < 0:
            return -1

        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1 :] = reversed(arr[i + 1 :])
        res = int("".join(arr))
        return res if res < 2**31 else -1


# ---------------------------------------------------------
# Problem: Permutation in String (LeetCode 567)
# Link: https://leetcode.com/problems/permutation-in-string/
# ---------------------------------------------------------
class SolutionProblemNine:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        left = 0

        for right in range(len(s2)):
            window[s2[right]] += 1
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if window == need:
                return True
        return False


# ---------------------------------------------------------
# Problem: Find K-th Smallest Pair Distance (LeetCode 719)
# Link: https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# ---------------------------------------------------------
class SolutionProblemTen:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count_pairs(mid):
            count = left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if count_pairs(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo


# ---------------------------------------------------------
# Problem: Longest Chunked Palindrome Decomposition (LeetCode 1147)
# Link: https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
# ---------------------------------------------------------
class SolutionProblemEleven:
    def longestDecomposition(self, text: str) -> int:
        l, r = 0, len(text) - 1
        left_str, right_str = "", ""
        res = 0

        while l < r:
            left_str += text[l]
            right_str = text[r] + right_str

            if left_str == right_str:
                res += 2
                left_str = ""
                right_str = ""

            l += 1
            r -= 1

        if l == r or left_str != "":
            res += 1

        return res


# ---------------------------------------------------------
# Problem: Last Substring in Lexicographical Order (LeetCode 1163)
# Link: https://leetcode.com/problems/last-substring-in-lexicographical-order/
# ---------------------------------------------------------
class SolutionProblemTwelve:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        n = len(s)

        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] > s[j + k]:
                j = j + k + 1
                k = 0
            else:
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
        return s[i:]


# ---------------------------------------------------------
# Problem: Get the Maximum Score (LeetCode 1537)
# Link: https://leetcode.com/problems/get-the-maximum-score/
# ---------------------------------------------------------
class SolutionProblemThirteen:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        i = j = 0
        s1 = s2 = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                s1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                s2 += nums2[j]
                j += 1
            else:
                s1 = s2 = max(s1, s2) + nums1[i]
                i += 1
                j += 1

        s1 += sum(nums1[i:])
        s2 += sum(nums2[j:])
        return max(s1, s2) % MOD
