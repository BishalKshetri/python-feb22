# -------------------------------
# Python Notes: DAY 4 - 27/02/2026
# Python Notes: Single-line if (Ternary Operator)
# -------------------------------

# Syntax:
# value_if_true if condition else value_if_false

# Example 1: Gender mapping
gender = "M"
data = "Male" if gender == "M" else "Female"
print(data)  # Output: Male

# Example 2: Check if number is even or odd
num = 10
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Even

# Example 3: Assign category based on score
score = 85
grade = "Pass" if score >= 50 else "Fail"
print(grade)  # Output: Pass

# Example 4: Using in data science context
# Mapping dataset values quickly
age = 17
age_group = "Minor" if age < 18 else "Adult"
print(age_group)  # Output: Minor

# ✅ Notes:
# - Single-line if is useful for quick assignments based on conditions
# - Common in data preprocessing, e.g., mapping categorical values
# - Can be nested, but for readability, avoid too many nested ternary operations
#   Example:
#   grade = "A+" if score >= 90 else "A" if score >= 80 else "B"