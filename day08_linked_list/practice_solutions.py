"""
Day 08: Linked List - LeetCode Problem Solutions
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------------------------------------------------------
# Problem: Reverse Linked List (LeetCode 206, Easy)
# Link: https://leetcode.com/problems/reverse-linked-list/
# ---------------------------------------------------------
class SolutionReverseList:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# ---------------------------------------------------------
# Problem: Merge Two Sorted Lists (LeetCode 21, Easy)
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# ---------------------------------------------------------
class SolutionMergeTwoLists:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next


# ---------------------------------------------------------
# Problem: Nth Node From End of List (LeetCode 19, Medium)
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# ---------------------------------------------------------
class SolutionRemoveNthNode:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = second = dummy
        # Move first n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        # Move both until first hits end
        while first:
            first = first.next
            second = second.next
        # Remove target node
        second.next = second.next.next
        return dummy.next


# ---------------------------------------------------------
# Example usage (LeetCode cases)
# ---------------------------------------------------------
