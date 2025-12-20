""" Day 111: Linked List - LeetCode Problem Solutions """

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------------------------------------------------------
# Problem: Remove Duplicates from Sorted List (LeetCode 83, Easy)
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# ---------------------------------------------------------
class SolutionProblemOne:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


# ---------------------------------------------------------
# Problem: Intersection of Two Linked Lists (LeetCode 160, Easy)
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Two-pointer technique:
        Switch heads when reaching end.
        They meet at intersection or None.
        """
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


# ---------------------------------------------------------
# Problem: Remove Linked List Elements (LeetCode 203, Easy)
# Link: https://leetcode.com/problems/remove-linked-list-elements/
# ---------------------------------------------------------
class SolutionProblemThree:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


# ---------------------------------------------------------
# Problem: Convert Binary Number in a Linked List to Integer (LeetCode 1290, Easy)
# Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# ---------------------------------------------------------
class SolutionProblemFour:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        while head:
            num = (num << 1) | head.val
            head = head.next
        return num


# ---------------------------------------------------------
# Problem: Minimum Pair Removal to Sort Array I (LeetCode 3507, Easy)
# Link: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/
# ---------------------------------------------------------
class SolutionProblemFive:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """
        Greedy simulation:
        - Repeatedly merge the adjacent pair with minimum sum
        - Stop once array becomes non-decreasing
        """
        ops = 0

        def is_sorted(arr):
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        while not is_sorted(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum:
                    min_sum = nums[i] + nums[i + 1]
                    idx = i

            nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
            ops += 1

        return ops
