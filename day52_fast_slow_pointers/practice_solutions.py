"""
Day 52: Fast & Slow Pointers - LeetCode Problem Solutions
"""


# ---------------------------------------------------------
# Problem: Linked List Cycle II (LeetCode 142, Medium)
# Link: https://leetcode.com/problems/linked-list-cycle-ii/
# ---------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionProblemOne:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle

        # Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


# ---------------------------------------------------------
# Problem: Palindrome Linked List (LeetCode 234, Easy)
# Link: https://leetcode.com/problems/palindrome-linked-list/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def isPalindrome(self, head):
        slow = fast = head
        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare halves
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


# ---------------------------------------------------------
# Problem: Middle of the Linked List (LeetCode 876, Easy)
# Link: https://leetcode.com/problems/middle-of-the-linked-list/
# ---------------------------------------------------------
class SolutionProblemThree:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Helper to create a list
    def create_list(values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    # Problem 1 Example
    head = create_list([3, 2, 0, -4])
    head.next.next.next.next = head.next  # Create cycle
    print(
        "Cycle starts at node with value:", SolutionProblemOne().detectCycle(head).val
    )

    # Problem 2 Example
    head = create_list([1, 2, 2, 1])
    print("Problem 2 Example:", SolutionProblemTwo().isPalindrome(head))

    # Problem 3 Example
    head = create_list([1, 2, 3, 4, 5])
    print("Problem 3 Example:", SolutionProblemThree().middleNode(head).val)
