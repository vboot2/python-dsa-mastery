"""Day 122: Two Pointers
Two pointers are commonly used to rearrange elements, merge sequences,
or scan strings efficiently with O(1) extra space.
"""


# Example 1: Sort array by parity (even first, odd later)
def example_one():
    """
    Two pointers from both ends:
    - Left finds odd
    - Right finds even
    - Swap when needed
    """
    nums = [3, 1, 2, 4]
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


print("Output Example 1:", example_one())


# Example 2: Merge two strings alternately
def example_two():
    """
    Two pointers over two strings:
    - Append characters alternately
    - Append remaining characters at the end
    """
    word1 = "abc"
    word2 = "pqrs"
    i = j = 0
    result = []

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            result.append(word1[i])
            i += 1
        if j < len(word2):
            result.append(word2[j])
            j += 1

    return "".join(result)


print("Output Example 2:", example_two())
