""" Day 93: Backtracking - LeetCode Problem Solutions """

from typing import List


# ---------------------------------------------------------
# Problem: Binary Tree Paths (LeetCode 257, Easy)
# Link: https://leetcode.com/problems/binary-tree-paths/
# ---------------------------------------------------------

class SolutionProblemOne:
    def binaryTreePaths(self, root) -> List[str]:
        """
        Backtracking:
        Build path as you traverse.
        At leaf, add path to result.
        """
        if not root:
            return []

        result = []

        def dfs(node, path):
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return

            if node.left:
                dfs(node.left, path + str(node.val) + "->")
            if node.right:
                dfs(node.right, path + str(node.val) + "->")

        dfs(root, "")
        return result


# ---------------------------------------------------------
# Problem: Matchsticks to Square (LeetCode 473, Medium)
# Link: https://leetcode.com/problems/matchsticks-to-square/
# ---------------------------------------------------------

class SolutionProblemTwo:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        Try assigning each stick to one of 4 sides.
        Backtracking with pruning:
        - Sort descending for better pruning
        - If a stick doesn't fit, skip
        - Avoid repeating same-length side case
        """
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        side = total // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def backtrack(i):
            if i == len(matchsticks):
                return all(s == side for s in sides)

            for j in range(4):
                if sides[j] + matchsticks[i] <= side:
                    sides[j] += matchsticks[i]

                    if backtrack(i + 1):
                        return True

                    sides[j] -= matchsticks[i]

                # prune duplicates
                if sides[j] == 0:
                    break

            return False

        return backtrack(0)


# ---------------------------------------------------------
# Problem: Remove Invalid Parentheses (LeetCode 301, Hard)
# Link: https://leetcode.com/problems/remove-invalid-parentheses/
# ---------------------------------------------------------

class SolutionProblemThree:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        Backtracking + pruning:
        - First compute min number of removals needed for '(' and ')'
        - Then backtrack:
            - At each char choose to remove or keep
            - Maintain balance
        - Avoid duplicates using a set
        """
        # Step 1: compute removals needed
        left_remove = right_remove = 0
        for c in s:
            if c == '(':
                left_remove += 1
            elif c == ')':
                if left_remove == 0:
                    right_remove += 1
                else:
                    left_remove -= 1

        result = set()

        def backtrack(i, left_count, right_count, left_rem, right_rem, path):
            if i == len(s):
                if left_rem == 0 and right_rem == 0 and left_count == right_count:
                    result.add(path)
                return

            c = s[i]

            # Case 1: remove '('
            if c == '(' and left_rem > 0:
                backtrack(i + 1, left_count, right_count, left_rem - 1, right_rem, path)

            # Case 2: remove ')'
            if c == ')' and right_rem > 0:
                backtrack(i + 1, left_count, right_count, left_rem, right_rem - 1, path)

            # Case 3: keep character
            if c not in "()":
                backtrack(i + 1, left_count, right_count, left_rem, right_rem, path + c)
            else:
                if c == '(':
                    backtrack(i + 1, left_count + 1, right_count, left_rem, right_rem, path + c)
                elif c == ')' and right_count < left_count:
                    backtrack(i + 1, left_count, right_count + 1, left_rem, right_rem, path + c)

        backtrack(0, 0, 0, left_remove, right_remove, "")
        return list(result)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example: Paths require tree input")
    print("Problem Two Example:", SolutionProblemTwo().makesquare([1,1,2,2,2]))
    print("Problem Three Example:", SolutionProblemThree().removeInvalidParentheses("()())()"))
