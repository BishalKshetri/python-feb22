# -------------------------------
# Example 1: Class with attributes and methods
# -------------------------------

class Test():
    a = 10   # class attribute 'a'
    b = 11   # class attribute 'b'

    # These methods are missing 'self', so they try to use variables 'a' and 'b' directly.
    # But since 'a' and 'b' are defined as class attributes, we should use 'self.a' and 'self.b'.
    def sum():
        return a + b   # ❌ This will cause an error because 'a' and 'b' are not defined in this scope

    def mult():
        return a * b   # ❌ Same issue here

    def diff():
        return a - b   # ❌ Same issue here

# Creating objects of the Test class
data = Test()
data1 = Test()
data2 = Test()


# -------------------------------
# Example 2: Correct use of attributes with self
# -------------------------------

class Test():
    a = 10  # class attribute 1
    b = 11  # class attribute 2

    def add(self):  # instance method with 'self'
        print(self.c)  # tries to print attribute 'c' (must be added separately to the object)
        self.d = "this is d attrs"  # creates a new attribute 'd' for this object only
        return self.a + self.b  # uses class attributes 'a' and 'b' correctly

# Create an object of Test
obj = Test()
obj.c = 100  # add a new attribute 'c' to this object manually

# Print attributes 'a', 'b', and 'c'
print(obj.a, obj.b, obj.c)  # Output: 10 11 100

# Try to print 'd' before calling add() → ❌ will cause error because 'd' is not created yet
# print(obj.d)

# Call add() method → this will create 'd' and return sum of a+b
print(obj.add())  # Output: 21

# Now 'd' exists, so we can print it
print(obj.d)  # Output: "this is d attrs"

# If we create another object, it won't have 'c' or 'd' unless we add them
# obj1 = Test()
# print(obj1.c)  # ❌ Error: 'c' not defined for obj1


# -------------------------------
# Example 3: Employee class
# -------------------------------

class Employee():
    name = "Bishall"       # class attribute 'name'
    role = "data analyst"  # class attribute 'role'

    def emp_detail(self):  # instance method
        # Access attributes using self
        print(f"Employee name is {self.name} and role is {self.role}")

# Create an object of Employee
obj = Employee()

# Call emp_detail() method to show details
print(obj.emp_detail())  # Output: Employee name is Bishall and role is data analyst