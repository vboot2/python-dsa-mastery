""" 
Day 97: Linked List / Matrix - LeetCode Problem Solutions 
"""
from typing import Optional, List

# ---------------------------------------------------------
# Problem: Insertion Sort List (LeetCode 147, Medium)
# Link: https://leetcode.com/problems/insertion-sort-list/
# ---------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionProblemOne:
    def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Perform insertion sort on a singly linked list.
        """
        dummy = ListNode(0)
        curr = head

        while curr:
            prev = dummy
            # find correct place to insert
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            nxt = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = nxt

        return dummy.next


# ---------------------------------------------------------
# Problem: Rotate List (LeetCode 61, Medium)
# Link: https://leetcode.com/problems/rotate-list/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # compute length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # make circular
        tail.next = head

        # find new tail (length - k steps)
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head


# ---------------------------------------------------------
# Problem: Game of Life (LeetCode 289, Medium)
# Link: https://leetcode.com/problems/game-of-life/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, board: List[List[int]]) -> List[List[int]]:
        rows, cols = len(board), len(board[0])

        def count_neighbors(r, c):
            live = 0
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                    live += 1
            return live

        # in-place update using encoded states
        for r in range(rows):
            for c in range(cols):
                live = count_neighbors(r, c)

                if board[r][c] == 1 and (live < 2 or live > 3):
                    board[r][c] = -1  # alive → dead
                if board[r][c] == 0 and live == 3:
                    board[r][c] = 2   # dead → alive

        # finalize states
        for r in range(rows):
            for c in range(cols):
                board[r][c] = 1 if board[r][c] > 0 else 0

        return board


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Problem One test
    head = ListNode(4, ListNode(2, ListNode(1)))
    sorted_list = SolutionProblemOne().solve(head)
    out = []
    while sorted_list:
        out.append(sorted_list.val)
        sorted_list = sorted_list.next
    print("Problem One Example:", out)

    # Problem Two test
    head2 = ListNode(1, ListNode(2, ListNode(3)))
    rotated = SolutionProblemTwo().solve(head2, 1)
    out2 = []
    while rotated:
        out2.append(rotated.val)
        rotated = rotated.next
    print("Problem Two Example:", out2)

    # Problem Three test
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print("Problem Three Example:", SolutionProblemThree().solve(board))
