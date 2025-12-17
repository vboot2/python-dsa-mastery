"""
Day 51: Two Pointers - LeetCode Problem Solutions
"""


# ---------------------------------------------------------
# Problem: Partition List (LeetCode 86, Medium)
# Link: https://leetcode.com/problems/partition-list/
# ---------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionProblemOne:
    def partition(self, head, x):
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next
        return before_head.next


# ---------------------------------------------------------
# Problem: Backspace String Compare (LeetCode 844, Easy)
# Link: https://leetcode.com/problems/backspace-string-compare/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def backspaceCompare(self, s, t):
        def build(string):
            stack = []
            for ch in string:
                if ch != "#":
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return "".join(stack)

        return build(s) == build(t)


# ---------------------------------------------------------
# Problem: Squares of a Sorted Array (LeetCode 977, Easy)
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# ---------------------------------------------------------
class SolutionProblemThree:
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] ** 2
                left += 1
            else:
                res[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Problem 1
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    x = 3
    res = SolutionProblemOne().partition(head, x)
    while res:
        print(res.val, end=" -> ")
        res = res.next
    print("None")

    # Problem 2
    print("Problem 2 Example:", SolutionProblemTwo().backspaceCompare("ab#c", "ad#c"))

    # Problem 3
    print(
        "Problem 3 Example:", SolutionProblemThree().sortedSquares([-4, -1, 0, 3, 10])
    )
