# ==========================================
# 15/03/2026, Day 9 - Python Notes
# TOPIC: LOOPS, RANGE, DICTIONARIES, MULTIPLICATION TABLE, BREAK/CONTINUE, TYPE CHECKING
# ==========================================

# -----------------------------
# FOR LOOP IN LIST
# -----------------------------
for i in [1,2,3,4,5,6,7]:
    # Print square of each number
    print(i*i)
    
    # Print only even numbers
    if i % 2 == 0:
        print(i)

# -----------------------------
# FOR LOOP IN STRING
# -----------------------------
for i in "Bishal":
    # Loops through each character of the string
    print(i)

# -----------------------------
# LOOP IN DICTIONARY
# -----------------------------
dict_data = {
    "name": "Bishal",
    "address": "KTM"
}

# Looping through keys
for key in dict_data:
    print(dict_data[key])

# Looping through values directly
for value in dict_data.values():
    print(value)

# -----------------------------
# USING RANGE
# -----------------------------
# range(start, stop, step)
for i in range(1, 15, 2):  # 1 to 14, step=2
    print(i)

# Range with negative step
for i in range(10, 1, -1):  # 10 to 2
    print(i)

# Odd numbers from 1 to 99
for i in range(1, 100, 2):
    print(i)

# Alternative way using condition
for i in range(1, 100):  # default step=1
    if i % 2 != 0:
        print(i)

# -----------------------------
# MULTIPLICATION TABLE (Dynamic)
# -----------------------------
n = int(input("Enter number for multiplication: "))
for i in range(1, 11):
    # Using f-string for clean formatting
    print(f"{n} * {i} = {n*i}")

# -----------------------------
# BREAK AND CONTINUE
# -----------------------------
# Example BREAK - stops loop when i==3
for i in [1,2,3,4,5,6,7,9]:
    if i == 3:
        break
    print(i)

# Example CONTINUE - skips iteration when i==3
for i in [1,2,3,4,5,6,7,9]:
    if i == 3:
        continue
    print(i)

# -----------------------------
# SEPARATE DATA TYPES INTO LISTS
# -----------------------------
a = [1,2,"hello","test",1.6,"nepal",1,7,"balen","rap"]

strings = []   # To store string values
ints = []      # To store integer values
floats = []    # To store float values

for i in a:
    if isinstance(i, str):   # Check if type is string
        strings.append(i)
    elif isinstance(i, int):  # Check if type is integer
        ints.append(i)
    elif isinstance(i, float):  # Check if type is float
        floats.append(i)

print("Strings:", strings)
print("Integers:", ints)
print("Floats:", floats)