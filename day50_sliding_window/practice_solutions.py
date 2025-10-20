""" 
Day 50: Sliding Window - LeetCode Problem Solutions 
"""

from collections import Counter, defaultdict

# ---------------------------------------------------------
# Problem: Substring with Concatenation of All Words (LeetCode 30, Hard)
# Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# ---------------------------------------------------------
class SolutionProblemOne:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        res = []

        for i in range(word_len):
            left = i
            seen = defaultdict(int)
            count = 0
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    seen[word] += 1
                    count += 1
                    while seen[word] > word_count[word]:
                        seen[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1
                    if count == len(words):
                        res.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = j + word_len
        return res


# ---------------------------------------------------------
# Problem: Minimum Window Substring (LeetCode 76, Hard)
# Link: https://leetcode.com/problems/minimum-window-substring/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        t_count = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right, char in enumerate(s):
            window[char] += 1
            if char in t_count and window[char] == t_count[char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""


# ---------------------------------------------------------
# Problem: Longest Repeating Character Replacement (LeetCode 424, Medium)
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/
# ---------------------------------------------------------
class SolutionProblemThree:
    def characterReplacement(self, s, k):
        count = defaultdict(int)
        left = 0
        maxf = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxf = max(maxf, count[s[right]])

            # shrink window if it becomes invalid
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 1 Example:", SolutionProblemOne().findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print("Problem 2 Example:", SolutionProblemTwo().minWindow("ADOBECODEBANC", "ABC"))
    print("Problem 3 Example:", SolutionProblemThree().characterReplacement("AABABBA", 1))
