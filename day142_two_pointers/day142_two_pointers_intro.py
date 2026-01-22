"""Day 142: Two Pointers
Two-pointer techniques applied to linked lists, strings,
arrays, greedy matching, and binary search optimization.
"""


# Example 1: Remove duplicates from sorted list II
def example_one():
    """
    Use dummy node + two pointers.
    Skip nodes that appear more than once.
    """
    from collections import Counter

    nums = [1, 2, 3, 3, 4, 4, 5]
    count = Counter(nums)
    return [n for n in nums if count[n] == 1]


print("Output Example 1:", example_one())


# Example 2: Check permutation inclusion using sliding window
def example_two():
    """
    Sliding window with two pointers and frequency count.
    """
    from collections import Counter

    s1, s2 = "ab", "eidbaooo"
    need = Counter(s1)
    window = Counter()
    left = 0

    for right in range(len(s2)):
        window[s2[right]] += 1
        if right - left + 1 > len(s1):
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            left += 1
        if window == need:
            return True
    return False


print("Output Example 2:", example_two())
