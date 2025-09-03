"""
Day 03: Hashing (Dictionaries & Sets)
"""

# Example 1: Using a dictionary as a hashmap
phone_book = {"Alice": "1234", "Bob": "5678"}
print("Alice's number:", phone_book["Alice"])

# Example 2: Using a set to store unique values
unique_numbers = {1, 2, 3, 2, 1}
print("Unique numbers:", unique_numbers)

# Example 3: Checking membership
if "Bob" in phone_book:
    print("Bob exists in phone book")

# Example 4: Frequency count with dict
s = "leetcode"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print("Frequency map:", freq)
