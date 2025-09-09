"""
Day 09: Stacks - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Valid Parentheses (LeetCode 20, Easy)
# Link: https://leetcode.com/problems/valid-parentheses/
# ---------------------------------------------------------
class SolutionValidParentheses:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in mapping:
                top = stack.pop() if stack else '#'
                if mapping[ch] != top:
                    return False
            else:
                stack.append(ch)
        return not stack


# ---------------------------------------------------------
# Problem: Min Stack (LeetCode 155, Medium)
# Link: https://leetcode.com/problems/min-stack/
# ---------------------------------------------------------
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# ---------------------------------------------------------
# Problem: Next Greater Element I (LeetCode 496, Easy)
# Link: https://leetcode.com/problems/next-greater-element-i/
# ---------------------------------------------------------
class SolutionNextGreaterElement:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack, mapping = [], {}
        for num in nums2:
            while stack and stack[-1] < num:
                mapping[stack.pop()] = num
            stack.append(num)
        return [mapping.get(num, -1) for num in nums1]


# ---------------------------------------------------------
# Example usage (LeetCode cases)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Valid Parentheses Example 1:", 
          SolutionValidParentheses().isValid("()"))
    print("Valid Parentheses Example 2:", 
          SolutionValidParentheses().isValid("()[]{}"))
    print("Valid Parentheses Example 3:", 
          SolutionValidParentheses().isValid("(]"))
    print("Valid Parentheses Example 4:", 
          SolutionValidParentheses().isValid("([])"))
    print("Valid Parentheses Example 5:", 
          SolutionValidParentheses().isValid("([)]"))

    print("Next Greater Element I Example 1:", 
          SolutionNextGreaterElement().nextGreaterElement([4,1,2], [1,3,4,2]))
    print("Next Greater Element I Example 2:", 
          SolutionNextGreaterElement().nextGreaterElement([2,4], [1,2,3,4]))
