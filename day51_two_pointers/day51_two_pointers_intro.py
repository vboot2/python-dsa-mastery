"""
Day 51: Two Pointers
Two Pointers is a fundamental technique used to solve problems involving sorted arrays, linked lists, or strings efficiently by maintaining two indices that move towards each other or in the same direction.
"""


# Example 1: Move zeros to the end of array
def example_one(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums


# Example 2: Check if a string is a palindrome
def example_two(s):
    s = "".join(filter(str.isalnum, s)).lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print("Output Example 1:", example_one([0, 1, 0, 3, 12]))
    print("Output Example 2:", example_two("A man, a plan, a canal: Panama"))
