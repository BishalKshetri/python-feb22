# -------------------------------
# Python Notes DAY 2: Operators, Input, Casting, Type Checking
# Date: 24/02/2026
# -------------------------------

# -------------------------------
# 1️⃣ Flake8 & Black Formatter
# -------------------------------
# flake8 → checks Python syntax and style issues
# black formatter → auto-formats Python code
# Usage in VS Code:
#   1. Right-click the file → Format Document → Select Black Formatter
#   2. Check syntax manually: flake8 filename.py

# -------------------------------
# 2️⃣ Comparison Operators
# -------------------------------
# Return Boolean: True / False
# == → comparison, = → assignment

a = 10
b = 5

print(a > b, a < b, a >= a, b <= b, a == b, a != b)
# Output: True False True True False True

print(6 > 2)  # True
print(2 == 2)  # True
# print(2 = "2")  # ❌ Invalid, = is assignment

# -------------------------------
# 3️⃣ Logical Operators
# -------------------------------
# AND → all conditions must be True
# OR → at least one condition is True

print(2 == 2 and 1 != 1)  # False
print(a == 10 and b)  # True (b is True)
print(a == 10 or a < 5)  # True

# Practical example: Traffic lights, system control checks

# -------------------------------
# 4️⃣ Input Function
# -------------------------------
# input() always returns a string
# Use type casting to convert to int, float, etc.

a = input("Enter a number: ")
b = input("Enter second number: ")

print("You entered:", a, b)
print(type(a), type(b))  # Both are <class 'str'>

# -------------------------------
# 5️⃣ Type Casting
# -------------------------------
# Convert string to integer

a = "10"
print("Before casting:", type(a))  # str

b = int(a)
print("After casting:", type(b))  # int

# -------------------------------
# 6️⃣ Input & Sum Example
# -------------------------------
# Cast input values directly when performing arithmetic

a = input("Enter a number: ")
b = input("Enter second number: ")

total_sum = int(a) + int(b)
print("Total sum:", total_sum)

# -------------------------------
# 7️⃣ Checking Data Type
# -------------------------------

# Proper way
print(isinstance(total_sum, int))  # True

# Not recommended
print(type(total_sum) == float)  # False

# ✅ Extra tips for learning:
# - isinstance() works for subclasses as well → safer in practice
# - Avoid using 'sum' as variable name because it overwrites Python built-in sum()
# - Always cast input before math operations
# - Logical operators are used in real-world data science:
#   → Filtering data (AND, OR)
#   → Conditional checks
#   → Data validation in ETL pipelines
# - Comparison operators are foundation for:
#   → Filtering datasets
#   → Feature engineering
#   → Model thresholding
