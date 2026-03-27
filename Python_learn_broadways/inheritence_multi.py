
# multilevel, 24/03/2026
'''
class A():
    a = 10

class B(A):
    c = 1000

class C(B):
    d = 2

obj = C() # Object should be made of child c lass

print(obj.d)
print(obj.c)
print(obj.a)


# Question 

# create a base class Person
# Dervie Student from Person.
# Derive GraduateStudent from Student.
# Add attributes like grade and theseis topic.
# Implement a method to display full academic profile. 

class Person():
    name = "Bishal"
    age = 25

class Student(Person):
    grade = "Bacheor first year" 
    std_id = 5

class GraduateStudent(Student):
    college_name = "Kathford"
    University = "TU"

obj = GraduateStudent()

print(f"Full Academic Profile\nName: {obj.name}\nAge: {obj.age}\nUniversity: {obj.University}College Name: {obj.college_name}\nGrade: {obj.grade}")

# by sudan without constructor
class Person():
    name = "Sudan"
    age = 26

    def __init__(self):
        pass

class Student(Person):
    school = "KMC"
    student_id = "KMC12"

    def __init__(self):
        super().__init__


class GraduateStudent(Student):
    grade = 4
    thesis_topic = "Database"

    def profile(self):
        result = f'{self.name}'
'''

# constructor

# Define the base class Person
class Person:
    # Constructor (__init__) takes name and age
    def __init__(self, name, age):
        self.name = name      # Assign name to the object
        self.age = age        # Assign age to the object


# Define Student class that inherits from Person
class Student(Person):
    # Constructor takes school, student_id, plus *args for name and age
    def __init__(self, school, student_id, *args):
        self.school = school          # Assign school
        self.student_id = student_id  # Assign student_id
        # Call the parent (Person) constructor with name and age from args
        super().__init__(args[0], args[1])


# Define GraduateStudent class that inherits from Student
class GraduateStudent(Student):
    # Class-level attributes (shared by all GraduateStudent objects)
    grade = 4.0
    thesis_topic = "Database"

    # Constructor takes keyword arguments (**kwargs)
    def __init__(self, **kwargs):
        # Pass school, student_id, name, age to Student constructor
        super().__init__(
            kwargs.get('school'),      # school from kwargs
            kwargs.get('student_id'),  # student_id from kwargs
            kwargs.get('name'),        # name from kwargs
            kwargs.get('age'),         # age from kwargs
        )

    # Method to return a profile string
    def profile(self):
        result = f'Name: {self.name}, Age: {self.age}, Id: {self.student_id}, School: {self.school}'
        return result


# Create an object of GraduateStudent using keyword arguments
obj = GraduateStudent(
    name="sudan",       # name passed as keyword
    age=26,             # age passed as keyword
    school="KMC",       # school passed as keyword
    student_id=123,     # student_id passed as keyword
)

# Call the profile method and print the result
print(obj.profile())

# Another qn 
# Create a base class Employee. Derive Developer from Employee. 
# Derive SeniorDeveloper from Developer. 
# 👉 Add programming language and project responsibility. 
# 👉 Create a method to display role hierarchy.

# Answer from Santosh

class Employee:  # Base class representing a generic employee
    def __init__(self, name, employeeId):  # Constructor initializes name and ID
        self.name = name  # Store employee name
        self.employeeId = employeeId  # Store employee ID

    def display_employee_info(self):  # Method to display employee details
        print(f"Employee Name: {self.name} and Employee Id : {self.employeeId}")


class Developer(Employee):  # Developer inherits from Employee
    def __init__(self, name, employeeId, programming_language):  # Constructor adds programming language
        super().__init__(name, employeeId)  # Call parent constructor for name and ID
        self.programming_language = programming_language  # Store developer's language

    def developer_info(self):  # Method to show developer details
        self.display_employee_info()  # Call base method to show name and ID
        print(f"Programming language: {self.programming_language}")  # Show programming language


class SeniorDeveloper(Developer):  # SeniorDeveloper inherits from Developer
    def __init__(self, name, employeeId, programming_language, project_responsibility):  
        super().__init__(name, employeeId, programming_language)  # Call Developer constructor
        self.project_responsibility = project_responsibility  # Store project responsibility

    def display_role(self):  # ✅ FIXED: properly indented method
        self.developer_info()  # Show developer info first
        print(f"Project responsibility: {self.project_responsibility}")  # Show senior role responsibility


# Create an instance of SeniorDeveloper
senior_dev = SeniorDeveloper(
    "Santosh Luitel",  # Name
    101,               # Employee ID
    "Python",          # Programming language
    "Leading backend project"  # Project responsibility
)

# Call methods
senior_dev.developer_info()   # Shows employee + developer info
senior_dev.display_role()     # ✅ Now works: shows developer info + project responsibility


# Multiple inheritence: FOR CHECKING hierarchy of where will searching will go

class A(): # Base class A
    def __init__(self,a,b): # constructor requires a and b
        self.a = a # stores value of a
        self.b = b

class B(A): #class B inherits from A
    def __init__(self,a,b,c,d): # constructor req a,b (fro A) and c,d(for B
        super().__init__(a,b) # Calls A's constructor to initialize a and b 
        self.c = c
        self.d = d


class C(B, A): # class c inherits from B and A
    def __init__(self, a, b, c, d,e): # constructor also req e
        super().__init__(a, b, c, d) # calls B's constructor(which calls A too)
        self.e = e # store calues of e as instance variable

# Create object of class C, passing all required arguments
obj = C(
    a = 10, # value for a (used by A)
    b = 20,
    c = 30,
    d = 40,
    e = 50,
)







# for looking hieracy : MRO 
print(C.__mro__)