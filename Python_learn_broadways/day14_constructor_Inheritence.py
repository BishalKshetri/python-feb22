# 24/02/2026


# Define a class named Employee
class Employee:

    # Constructor method (__init__) is called automatically when an object is created
    # It initializes the object with given values for name and address
    def __init__(self, name, address):  
        print(name, address)  # Print the values passed during object creation
        self.name = name      # Assign the 'name' argument to the object's 'name' attribute
        self.address = address  # Assign the 'address' argument to the object's 'address' attribute

    # Instance method to return details of the employee
    def detail(self):
        # Use f-string to format and return the employee's details
        return f'name = {self.name}, address = {self.address}'


# Create an object (instance) of the Employee class with specific values
obj = Employee("suman", "biratnagar")

# Call the detail() method on the object and print the returned string
print(obj.detail())

# QUESTION 1 

# Define a class named Math
class Math:
    # Constructor method (__init__) runs automatically when an object is created
    # It initializes the object with values for 'a' and 'b'
    def __init__(self, a, b):
        self.a = a        # Assign the argument 'a' to the instance variable self.a
        self.b = b        # Assign the argument 'b' to the instance variable self.b

    # Instance method to add the two numbers
    def add(self):
        return self.a + self.b   # Return the sum of self.a and self.b
    
    # Instance method to multiply the sum (from add()) by 10
    def multi(self):             # Correct spelling: 'multi' not 'mutli'
        return self.add() * 10   # Call the add() method, then multiply its result by 10
    
# Create an object (instance) of the Math class with values 2 and 3
obj = Math(2, 3)

# Call the multi() method on the object and print the result
print(obj.multi())   # Expected output: (2 + 3) * 10 = 50

# Call the add() method on the object and print the result
print(obj.add())     # Expected output: 2 + 3 = 5


# -------------------------------
# INHERITANCE in Python
# -------------------------------
# Inheritance allows one class (child) to reuse attributes and methods of another class (parent).
# It helps reduce code duplication and models "is-a" relationships.
#
# Types of Inheritance:
# 1. Single Inheritance: One parent → one child (A → B).
# 2. Multi-level Inheritance: Chain of inheritance (A → B → C).
# 3. Multiple Inheritance: One child inherits from multiple parents (A, B → C).
#
# In this example, we demonstrate SINGLE INHERITANCE:
# Parent class = Parent
# Child class = Child (inherits from Parent)

# -------------------------------
# Define Parent class
# -------------------------------
class Parent():
    a = 100   # class attribute 'a'
    b = 1000  # class attribute 'b'

    def __init__(self):  # constructor of Parent class
        print("I am from parent class")  # runs automatically when Parent object is created

    def test(self):  # method in Parent class
        return self.a  # returns attribute 'a'

# -------------------------------
# Define Child class (inherits from Parent)
# -------------------------------
class Child(Parent):  # Child inherits all attributes and methods from Parent
    a = 1   # overrides attribute 'a' from Parent
    c = 2   # new attribute 'c' added in Child

    def __init__(self):  # constructor of Child class
        print("I am from child class")  # runs automatically when Child object is created
        super().__init__()  # calls Parent class constructor explicitly

    def test(self):  # overrides Parent's test() method
        return self.c  # now returns Child's attribute 'c' instead of Parent's 'a'

# -------------------------------
# Create object of Child class
# -------------------------------
obj = Child()  # constructor of Child runs first, then Parent's constructor via super()

# Access Child's attribute 'c'
print(obj.c)  # Output: 2

# Call Child's test() method (overridden version)
print(obj.test())  # Output: 2


