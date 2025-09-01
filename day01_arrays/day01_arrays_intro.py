# day01_arrays_intro.py
# ✅ Day 1: Arrays & Lists (Python Implementation)

# ----------------------------
# 1. Creating arrays (lists in Python)
# ----------------------------
arr = [10, 20, 30, 40, 50]
print("Original array:", arr)

# ----------------------------
# 2. Accessing elements
# ----------------------------
print("First element:", arr[0])   # Index 0
print("Last element:", arr[-1])  # Negative index

# ----------------------------
# 3. Updating elements
# ----------------------------
arr[2] = 35
print("After update:", arr)

# ----------------------------
# 4. Adding elements
# ----------------------------
arr.append(60)      # Add to end
arr.insert(2, 25)   # Insert at index
print("After adding:", arr)

# ----------------------------
# 5. Removing elements
# ----------------------------
arr.pop()           # Removes last element
arr.remove(25)      # Removes first occurrence of 25
print("After removing:", arr)

# ----------------------------
# 6. Iterating through array
# ----------------------------
print("Iterating:")
for num in arr:
    print(num, end=" ")
print()

# ----------------------------
# 7. Slicing (sub-arrays)
# ----------------------------
print("First three:", arr[:3])
print("Last two:", arr[-2:])

# ----------------------------
# 8. Searching
# ----------------------------
if 40 in arr:
    print("40 is present at index", arr.index(40))
