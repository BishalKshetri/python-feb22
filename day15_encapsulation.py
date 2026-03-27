# encapsulation or data access modifier

# Topics Overview:
# - Classes: Blueprints for creating objects in Python.
# - Attributes: Variables inside a class (public or private).
# - Private attributes: Start with __, name-mangled by Python (harder to access directly).
# - Methods: Functions inside a class that operate on attributes.
# - Inheritance: Child classes can reuse Parent class attributes/methods.
# - Objects: Instances created from a class.
# - Practical use: This design models authentication systems (username/password checks),
#   role-based access control (Parent = base login, Child = extended roles),
#   and secure data handling (private attributes hide sensitive info).

class Parent():  # Define a base class called Parent
    __a = 1  # Private attribute (name-mangled, not directly accessible outside the class)
    __username = "sudan"  # Private attribute storing a username
    __password = "123"    # Private attribute storing a password
    b = __a + 20  # Public attribute, calculated using private __a
    print("this is from class ", __a)  # Executes immediately when the class is defined
    _protected = "I am protected"
    __private = "I am private"

    def __login(self):  # Private method for login validation
        # Hypothetical check function (not defined here, would raise error if called)
        data = self.check(self.__username, self.__password)
        if data:  # If credentials are valid
            return True
        return False  # Otherwise return False


class Child(Parent):  # Child class inherits everything from Parent
    pass  # Could extend login logic for specific roles (e.g., Admin, Customer)


obj = Parent()  # Create an object (instance) of Parent class
print("this is from obj", obj.b)  # Access public attribute 'b' from the object
# protected can be used in object but private can't 

# question: 
# 🔹 1. Employee Salary System
# A company wants to keep employee salaries partially hidden.

# Create a class Employee with a protected variable _salary.
# Create a subclass Manager.
# Allow the manager to access and modify employee salary internally.
# Prevent direct salary modification from outside the class.
# 👉 Real-life angle: HR systems restrict salary visibility but allow managers limited access.

# 🔹 Employee Salary System
# Practical Use:
# In HR systems, employee salaries are sensitive data.
# - Employees should not directly modify their own salary.
# - Managers (or HR staff) can view and adjust salaries internally.
# - Protected attributes (_salary) allow controlled access:
#   visible inside the class and subclasses, but hidden from outside.
# 👉 Real-life angle: HR systems restrict salary visibility but allow managers limited access.

class Employee:  # Base class representing a generic employee
    def __init__(self, name, salary):  # Constructor initializes employee name and salary
        self.name = name  # Public attribute: employee name
        self._salary = salary  # Protected attribute: salary (not meant for direct outside access)

    def show_info(self):  # Public method to display employee details
        print(f"Employee: {self.name}, Salary: [Hidden for privacy]")  # Salary hidden externally


class Manager(Employee):  # Manager inherits from Employee
    def __init__(self, name, salary, department):  # Constructor adds department info
        super().__init__(name, salary)  # Call Employee constructor for name and salary
        self.department = department  # Public attribute: manager's department

    def view_salary(self):  # Manager can view salary internally
        print(f"Manager {self.name} sees salary: {self._salary}")

    def update_salary(self, new_salary):  # Manager can update salary internally
        self._salary = new_salary
        print(f"Manager {self.name} updated salary to: {self._salary}")


# Create an employee object
emp = Employee("Sudan", 50000)
emp.show_info()  # Shows employee info but hides salary externally

# Create a manager object
mgr = Manager("Santosh", 70000, "IT Department")
mgr.show_info()  # Shows manager info (salary hidden externally)
mgr.view_salary()  # Manager can view salary internally
mgr.update_salary(75000)  # Manager updates salary internally
mgr.view_salary()  # Manager sees updated salary

