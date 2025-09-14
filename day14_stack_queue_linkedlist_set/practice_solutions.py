"""
Day 14: Stack, Queue, LinkedList, Set - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Remove Duplicate Letters (LeetCode 316, Medium)
# Link: https://leetcode.com/problems/remove-duplicate-letters/
# ---------------------------------------------------------
class SolutionRemoveDuplicateLetters:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
        return "".join(stack)


# ---------------------------------------------------------
# Problem 2: Decode String (LeetCode 394, Medium)
# Link: https://leetcode.com/problems/decode-string/
# ---------------------------------------------------------
class SolutionDecodeString:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num, curr_str = 0, ""
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                stack.append((curr_str, curr_num))
                curr_str, curr_num = "", 0
            elif ch == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                curr_str += ch
        return curr_str


# ---------------------------------------------------------
# Problem 3: Build an Array With Stack Operations (LeetCode 1441, Medium)
# Link: https://leetcode.com/problems/build-an-array-with-stack-operations/
# ---------------------------------------------------------
class SolutionBuildArrayWithStackOps:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        res = []
        i = 0
        for num in range(1, n + 1):
            if i == len(target):
                break
            res.append("Push")
            if target[i] == num:
                i += 1
            else:
                res.append("Pop")
        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Remove Duplicate Letters Example:", SolutionRemoveDuplicateLetters().removeDuplicateLetters("bcabc"))
    print("Decode String Example:", SolutionDecodeString().decodeString("3[a2[c]]"))
    print("Build Array Example:", SolutionBuildArrayWithStackOps().buildArray([1,3], 3))
