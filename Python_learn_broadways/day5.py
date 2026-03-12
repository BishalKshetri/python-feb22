
# Python Notes: DAY 5 - 09/03/2026
# Lists
# Lists of ordered collection of data items
# they store multiple itesms in single variable
# lists are changeable meaning we can alter then after creation
# list items are seperated by commas and enclosed with square brackets [].set
# lists are mutable, means data inside can be changed when needed.

# -------------------------------
# Python Notes: List Basics & Indexing
# -------------------------------

# 1️⃣ Creating a list with mixed types
a = [1, 2, 3, 4, 5, "Bishal", "Melina"]

# 2️⃣ Checking type of the list
print(type(a))  
# Output: <class 'list'>
# Explanation: 'a' is a Python list. Lists can store multiple data types (int, str, float, etc.)
# Note: In traditional arrays (e.g., C, Java), all elements must be same type

# 3️⃣ Printing the list
print(a)
# Output: [1, 2, 3, 4, 5, 'Bishal', 'Melina']

# 4️⃣ Length of list
print(len(a))
# Output: 7
# len() counts all top-level elements
# Important: Indexing in Python starts from 0, so last index = len(a)-1

# 5️⃣ Indexing — Access elements using position
print(a[4])  
# Output: 5
# Index 4 → fifth element (count starts from 0)

# 6️⃣ Slicing — Extract a portion of the list
print(a[2:5])  
# Output: [3, 4, 5]
# From index 2 up to (but not including) index 5

print(a[:5])  
# Output: [1, 2, 3, 4, 5]
# From start up to index 5 (exclusive)

print(a[1:])  
# Output: [2, 3, 4, 5, 'Bishal', 'Melina']
# From index 1 to end

# 7️⃣ Extra tips for learning:
# - Negative indexing: a[-1] → last element, a[-2] → second last element
# - Copying list: b = a[:] → creates a shallow copy
# - Nested lists: a list can contain another list → access using multiple indices
# - Lists are mutable: a[0] = 100 → changes the first element
# - Lists support operations: + (concat), * (repeat), in (membership check)

# 8️⃣ Examples of extra tips:
print(a[-1])  # Output: 'Melina' (last element)
b = a[:]      # Copying the list
a[0] = 100
print(a)      # Output: [100, 2, 3, 4, 5, 'Bishal', 'Melina']
