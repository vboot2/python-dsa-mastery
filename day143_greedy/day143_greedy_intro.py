"""Day 143: Greedy
Greedy algorithms make locally optimal choices at each step
with the goal of reaching a globally optimal solution.
"""


# Example 1: Minimum moves to reduce a number to 1
def example_one():
    """
    Greedy choice:
    - If even → divide by 2
    - If odd → increment or decrement to reach power of 2 faster
    """
    n = 7
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n += 1 if n == 3 or n & 2 else -1
        steps += 1

    return steps


print("Output Example 1:", example_one())


# Example 2: Choose best digit swap to maximize number
def example_two():
    """
    Greedy:
    Track last occurrence of each digit,
    swap earliest smaller digit with largest possible later digit.
    """
    num = list("2736")
    last = {d: i for i, d in enumerate(num)}

    for i, d in enumerate(num):
        for x in map(str, range(9, int(d), -1)):
            if x in last and last[x] > i:
                num[i], num[last[x]] = num[last[x]], num[i]
                return "".join(num)
    return "".join(num)


print("Output Example 2:", example_two())
