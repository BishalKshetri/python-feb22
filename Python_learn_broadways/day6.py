# day 6: march 10 2026
# -------------------------------
# Python Notes: Adding Data to Lists
# -------------------------------

# Sample list
data = [1, 2, 3, 4]

# 1️⃣ append() — Add element at the end
data.append(1)
print(data)  
# Output: [1, 2, 3, 4, 1]
# Explanation: Adds '1' at the end of the list

# 2️⃣ insert() — Add element at a specific position
data.insert(0, "hello")  # 0 is the index
print(data)
# Output: ['hello', 1, 2, 3, 4, 1]
# Explanation: 'hello' inserted at index 0 (start of the list)

# 3️⃣ extend() — Add elements of another list to the end
a = [1, 2, 3]
b = [5, 6, 7]

a.extend(b)
print(a)  # Output: [1, 2, 3, 5, 6, 7]
print(b)  # Output: [5, 6, 7]
# Explanation: extend() modifies list 'a', adds elements of 'b'; 'b' remains unchanged

# 4️⃣ Concatenation (+) — Combine two lists to create a new list
c = a + b
print(c)  
# Output: [1, 2, 3, 5, 6, 7, 5, 6, 7]
# Explanation: '+' creates a new list; original lists 'a' and 'b' remain unchanged

# ✅ Summary:
# - append(x) → add single element at the end
# - insert(i, x) → add element x at index i
# - extend(list2) → add all elements of list2 to list1
# - a + b → concatenate two lists into a new list

# Deleting items/elements from existing list
# Del, remove[particular value], pop[last value], clear[clear list]

# del will is function of python not only list.
# del
data = ["Kathmandu", "nepal","nepal", "US", "Iran", "election", "balen"]
del data[0] # if we don't mention index like 0, whole vairable will be deleted from here.
print(data)

# remove
data = ["Kathmandu", "nepal","nepal", "US", "Iran", "election", "balen"]
data.remove("nepal") # it will remove first nepal only and don't work for duplciates. 
print(data)

# pop
data = ["Kathmandu", "nepal","nepal", "US", "Iran", "election", "balen"]
remove_data = data.pop(0)
remove_data1 = data.pop()
print(data)
print(remove_data, remove_data1)

# data.clear()
print(data)

# Other methods
# count, index, reverse, sort
# count() - count occurances of value
data = ["Kathmandu", "nepal","nepal", "US", "Iran", "election", "balen"]
print("Count of nepal:", data.count("nepal"))

# index(): find first index of a value
# finds position of "us" in the list
print("Index of US: ", data.index("US"))

# 3️⃣ reverse() — Reverse the list in place
# Reverses the order of elements
data.reverse()
print("Reversed list:", data)  
# Output: ['balen', 'election', 'Iran', 'US', 'nepal', 'nepal', 'Kathmandu']

# 4️⃣ sort() — Sort the list in place
# Sorting strings alphabetically
data.sort()
print("Sorted list:", data)

# Sorting numbers example
numbers = [5, 2, 9, 1]
numbers.sort()  # Sort ascending
print("Numbers sorted ascending:", numbers)  # Output: [1, 2, 5, 9]

numbers.sort(reverse=True)  # Sort descending
print("Numbers sorted descending:", numbers)  # Output: [9, 5, 2, 1]


# -------------------------------
# Python Notes: Nested Lists
# -------------------------------

# A nested list is a list that contains another list as an element
a = [1, 2, 3, ["hello", "hi"], 19]

# 1️⃣ len() — Counts only top-level elements
print(len(a))  # Output: 5
# Explanation:
# Top-level elements are: 1, 2, 3, ["hello","hi"], 19
# The sublist ["hello","hi"] counts as 1 element

# 2️⃣ Accessing nested list
b = a[3]  # b is now the sublist ["hello", "hi"]
print(b[1])  # Output: 'hi'
# Explanation:
# b[0] = "hello"
# b[1] = "hi"

# 3️⃣ Directly accessing nested element in one step
b = a[3][1]
print(b)  # Output: 'hi'
# Explanation:
# a[3] → ["hello","hi"]
# a[3][1] → 'hi'

# ✅ Summary:
# - Nested lists are lists inside lists
# - len() counts only top-level elements
# - Access nested elements using multiple indexing: list[index1][index2]


# -------------------------------
# Python Notes: Dictionaries (dict)
# -------------------------------

# 1️⃣ Creating a dictionary
# Dictionaries store data in key:value pairs
# Keys must be unique, values can be anything
a = {
    "name": "hari",
    "address": "Nepal",
    "age": 1,
    "age": 13  # Duplicate key! Only last value is kept
}

# 2️⃣ Checking type
print(type(a))  
# Output: <class 'dict'>
# Explanation: 'a' is a Python dictionary

# 3️⃣ Length of dictionary
print(len(a))  
# Output: 3
# Explanation: Only unique keys count (name, address, age)

# 4️⃣ Accessing values by key
print(a["name"])  
# Output: 'hari'

# 5️⃣ Access all keys
print(a.keys())  
# Output: dict_keys(['name', 'address', 'age'])

# 6️⃣ Access all values
print(a.values())  
# Output: dict_values(['hari', 'Nepal', 13])

# ✅ Extra tips:
# - Check if key exists: "name" in a → True / False
# - Add new key-value: a["gender"] = "male"
# - Update value: a["age"] = 14
# - Remove key: a.pop("address") or del a["address"]
# - Nested dictionary: a key can hold another dictionary → useful for JSON

# -------------------------------
# Practical use in Data Science:
# -------------------------------
# 1. Storing metadata about datasets
dataset_info = {
    "dataset_name": "students_scores",
    "rows": 1000,
    "columns": 5,
    "source": "Kaggle"
}

# 2. Counting occurrences (like a frequency table)
data = ["Nepal","USA","Nepal","Iran","USA","Nepal"]
freq = {}
for item in data:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
print(freq)
# Output: {'Nepal': 3, 'USA': 2, 'Iran': 1}

# 3. Storing JSON-like API responses
api_response = {
    "user": {"id": 101, "name": "Hari"},
    "status": "active",
    "roles": ["admin", "editor"]
}
print(api_response["user"]["name"])  # Output: 'Hari'

# ✅ Notes:
# - Dictionaries are very useful in data analysis for **frequency counts, mapping, storing metadata, and JSON handling**
# - Keys should be unique, immutable (str, int, tuple), values can be anything

