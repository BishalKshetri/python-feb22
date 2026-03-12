# -------------------------------
# Python Notes: DAY 1 - 23/02/2026
# -------------------------------

# 1️⃣ Virtual Environment
# Helps to manage packages for different projects
# Create environment:
# python -m venv env_name
# Activate environment (Windows):
# env_name\Scripts\activate
# Activate environment (Linux/Mac):
# source env_name/bin/activate

# -------------------------------
# 2️⃣ Hello World & Variables
print("Hello World", "I am Bishal")

# Variables
a = "hello"
b = 10
print(b)  # 10

# -------------------------------
# 3️⃣ Data Types
# a = "1.6"  -> str
# a = 10     -> int
# a = -10    -> int (whole number)
# a = 1.5    -> float
# a = None   -> NoneType
# a = True   -> bool
# a = 2+2j   -> complex
# a = '' vs a = None → '' is empty string, None is absence of value

# Check type
a = 10
print(type(a))  # <class 'int'>

# -------------------------------
# 4️⃣ Arithmetic Operators
a = 10
b = 20

# Addition, Subtraction, Multiplication
sum_val = a + b
diff = b - a
mult = a * b

# Printing results directly
print(a + b, a - b, b / a)  # Output: 30 -10 2.0

# Other useful arithmetic operators:
# b // a -> Floor division (lowest whole number)
# a ** b -> Exponentiation (a raised to power b)
# a % b  -> Modulus (remainder, useful for checking even/odd)

# Example: check if a number is even
num = 11
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# -------------------------------
# 5️⃣ String Concatenation
a = "Bishal"
b = "Kshetri"
print(a + b)  # Output: BishalKshetri

# Extra tips:
# - Use a + " " + b to add space → "Bishal Kshetri"
# - Strings can be repeated: print(a * 3) → BishalBishalBishal
# - Strings are immutable → cannot change a character directly
# - Useful in data science:
#    • Concatenate column names or strings
#    • Generate labels, file names dynamically

# -------------------------------
# ✅ Extra Learning Notes:
# - Python variable types are dynamic; no need to declare type
# - None is different from empty string or 0
# - Arithmetic operators are essential for calculations in data processing
# - String operations are foundational for text preprocessing (NLP, CSV handling)