# day02_strings_intro.py

# Strings are immutable in Python
s = "hello world"

# 1. Basic operations
print(s.upper())       # HELLO WORLD
print(s.lower())       # hello world
print(s.title())       # Hello World
print(s.strip("hd"))   # ello worl  (removes 'h' and 'd' from ends)

# 2. Substring check
print("hello" in s)    # True
print("bye" not in s)  # True

# 3. Slicing
print(s[0:5])          # hello
print(s[::-1])         # dlrow olleh (reverse string)

# 4. Splitting and joining
words = s.split()      # ['hello', 'world']
print(words)
joined = "-".join(words)
print(joined)          # hello-world

# 5. Palindrome check
def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("Racecar"))      # True
print(is_palindrome("hello"))        # False
