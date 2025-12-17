""" Day 96: Linked List / Array - LeetCode Problem Solutions """

from typing import List, Optional


# ---------------------------------------------------------
# Problem: Copy List with Random Pointer (LeetCode 138, Medium)
# Link: https://leetcode.com/problems/copy-list-with-random-pointer/
# ---------------------------------------------------------

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


class SolutionProblemOne:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Three-pass solution:
        1. Insert cloned nodes after each original node.
        2. Assign random pointers.
        3. Detach cloned list from original list.
        """
        if not head:
            return None

        # Step 1: clone nodes
        curr = head
        while curr:
            nxt = curr.next
            clone = Node(curr.val)
            curr.next = clone
            clone.next = nxt
            curr = nxt

        # Step 2: assign random pointers for clones
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: separate lists
        curr = head
        clone_head = head.next
        while curr:
            clone = curr.next
            curr.next = clone.next
            curr = curr.next
            if curr:
                clone.next = curr.next

        return clone_head


# ---------------------------------------------------------
# Problem: Sort List (LeetCode 148, Medium)
# Link: https://leetcode.com/problems/sort-list/
# ---------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionProblemTwo:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge Sort on linked list:
        - Find middle using slow/fast pointers
        - Recursively sort halves
        - Merge sorted lists
        """
        if not head or not head.next:
            return head

        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None  # split list

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next


# ---------------------------------------------------------
# Problem: Max Points on a Line (LeetCode 149, Hard)
# Link: https://leetcode.com/problems/max-points-on-a-line/
# ---------------------------------------------------------

class SolutionProblemThree:
    def maxPoints(self, points: List[List[int]]) -> int:
        from math import gcd

        n = len(points)
        if n <= 2:
            return n

        max_points = 1

        for i in range(n):
            slopes = {}
            same = 0
            local_max = 1

            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    same += 1
                    continue

                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1
                local_max = max(local_max, slopes[(dx, dy)])

            max_points = max(max_points, local_max + same)

        return max_points


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem Three Example:", SolutionProblemThree().maxPoints([[1,1],[2,2],[3,3]]))
    print("Problem Two Example: Sorting requires linked list input")
    print("Problem One Example: Random pointer copy requires linked list input")
