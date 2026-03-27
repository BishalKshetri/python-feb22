# -------------------------------
# Python Notes: DAY 3 - 26/02/2026
# -------------------------------

# 1️⃣ Python String Methods
a = "Bishal Kshetri"
print(a.upper())  # BISHAL KSHETRI
print(a.lower())  # bishal kshetri
print(a.title())  # Bishal Kshetri
print(a.strip())  # Remove leading/trailing spaces
print(a.replace("Bishal", "Hari"))  # Hari Kshetri
print(a.split())  # ['Bishal', 'Kshetri']
print(" ".join(["Hello", "World"]))  # Join list into string

# -------------------------------
# 2️⃣ Simple if / else
age = int(input("Enter age: "))
if age < 25:
    print("Age is less than 25")
else:
    print("Age is 25 or more")

# -------------------------------
# 3️⃣ Positive / Negative number check
n = int(input("Enter a number: "))
if n > 0:
    print("Number entered is positive")
elif n == 0:
    print("Number entered is zero")
else:
    print("Number entered is negative")

# -------------------------------
# 4️⃣ Nested if for GPA grading (with input validation)
n = input("Enter your GPA to check your grade: ")

# Basic numeric check
if '.' in n or n.isdigit():  
    n = float(n)
    if n >= 0 and n <= 4:
        if n >= 3.6:
            print("Grade: A+")
        elif n >= 3.2:
            print("Grade: A")
        elif n >= 2.8:
            print("Grade: B+")
        elif n >= 2.4:
            print("Grade: B-")
        elif n >= 2:
            print("Grade: C")
        else:
            print("Fail")
    else:
        print("Please enter a valid GPA between 0 and 4")
else:
    print("Invalid input. Please enter a number.")

# -------------------------------
# 5️⃣ Practical Examples for Data Science Learning

# Example 1: Check if a dataset value is missing or invalid
value = input("Enter dataset value: ")
if value != "" and value != "NA":
    print("Valid value:", value)
else:
    print("Missing value detected!")

# Example 2: Categorize age groups
age = int(input("Enter age for category: "))
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teen"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"
print("Age category:", category)

# Example 3: Check if number is divisible by multiple conditions
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("Number is divisible by 2 and 3")
elif num % 2 == 0:
    print("Number is divisible by 2")
elif num % 3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 2 or 3")

# Example 4: String-based conditions
name = input("Enter your name: ")
if name.isalpha():  # Check if input contains only letters
    print("Hello", name)
else:
    print("Invalid name. Only letters allowed.")

# Example 5: Nested condition for text processing
text = input("Enter feedback (good/average/bad): ").lower()
if "good" in text:
    print("Positive feedback detected")
elif "average" in text:
    print("Neutral feedback detected")
elif "bad" in text:
    print("Negative feedback detected")
else:
    print("Feedback not recognized")