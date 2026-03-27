# 18 march 2026

"""
Function:
* it should be called for running and should be returned
* It can be reused
* function name should be start with small letter
* function should be created above of its use

# creating function

def test():
    print("This is bishal, fucntin test")
    return("data")

# calling function
test()

# check even number

def check_even_number():
    result = []
    a = [2,3,4,5,1]
    for i in a:
        if(i % 2 == 0):
            result.append(i)
    return result # retun running out of loop shoule be done for running whole loops else return first only

# but we should use inside loop in case when we are searching specific from lists.

print(check_even_number())

# make one function
def intro_print():
    print("Enter information: ")
    name = input("Enter Full Name: ")
    age = int(input("Enter age: "))
    address = input("Enter Address: ")
    print(
        f"Your information is:\nHello {name} !. Nice to meet you. You are {age} years old. you live in {address}"
    )
    return "Print intro"

intro_print()


# Positional Argument 
def user_info(c,a,b):
    fname = a
    lname = b
    relation = c
    return f'my {relation} name is {fname} {lname}.'

print(user_info("wife","Melina", "Baniya"))
print(user_info("father","Ishwori","Budhaksehtri"))
print(user_info("mother","Radhika","Bhandari"))
print(user_info("brother","Badal","Budhakshetri"))


# practice questions



def arth(a,b,c,d):
    multfirst_second = a*b
    sub_third = (a*b) - c
    divide = ((a*b)-c)/d
    return f'firstt mult is {multfirst_second}. Subtract is {sub_third}. Division is {divide}'

print(arth(1,2,3,5))



# day 13 19/03/2026

def calc_percentage(marks):
    total = 0 
    for i in marks:
        total += i 
    percent = total/(len(marks))
    return percent

hari = calc_percentage([100,58,57])
Bishal = calc_percentage([100,12,57])
Melina = calc_percentage([22,58,57])
Suman = calc_percentage([55,58,57])

print(hari,Bishal,Melina,Suman)


# keyword argument
# keyword argument helps for more validations, it doesn't need specific positions for running
# may be less error due to keyword clarity 

def calc_percentage(names,marks):
    total = 0 
    for i in marks:
        total += i 
    percent = total/(len(marks))
    return percent

hari = calc_percentage(marks=[100,58,57], names="Hari")
Bishal = calc_percentage(marks=[100,12,57], names="Bishal")
Melina = calc_percentage(marks=[22,58,57], names= "Melina")
Suman = calc_percentage(marks=[55,58,57], names= "Suman")

print(hari,Bishal,Melina,Suman)


# we can use both positional and keyword argument at once

# positional can't be after keyboard argument

# Questions 
# employee system
# name, position and salary
 
# if position is not sent, it should show position is missing and similar for others 
# total tax paid in a year also need to calculate

def emp_details(name=None, position=None, salary=None):
    result = {
        "Name": name if name else "Name is missing",
        "Position": position if position else "Position is missing",
        "Salary": salary if salary else "Salary is missing"
    }
    return result

def emp_details(name=None, position=None, salary=None):
    result = {
        "Name":name 

        if name:
            print(f"Name: {name}")
    }

emp1 = emp_details(name="Bishal", position= "data analyst", salary= 10000 )
print(emp1)



def employee_detail(emp, position, salary):
    print(emp)


# default argument

def test(fname, lname="sharma"):
    print(fname,lname)

test("Sudan")
test("Sudan","bhandari")

def area_of_circle(r,pie = 3.14):
    print(pie*r**2)

area_of_circle(7,2)


# DATE: 20/2/2026

# arbitory positional argument
def sum(*args): # store data in tuple format
    print(args)
    print(type(args))

sum(1,2,3,4,5,6)
sum(1,2,3)

def user_info(**kwargs):
    print(kwargs)
    print(kwargs.get('phone_num')) # .get will return none and help to handle error
    print(type(kwargs)) # as it store supports multiple data types, hence is dict
    print('----------------')

user_info(name="ram", address="nepal",phone_num="9823546798")
user_info(name="ram", address="nepal")


# positional and keyword arguments together 

def test2(*args, **kwargs):
    print(args)
    print(kwargs)

test2(1,2,3,4,5, name = "bishal", address = "taplejung")



def student_detail(*marks, **student_data):
    print("Marks", marks) 
    print("Std name", student_data)

print(student_detail(10,20,30,40, name="bishal"))
print(student_detail(30,40,50,60, name = "ram"))

# another example 

def student_detail(*marks, **student_data):
    total = 0
    for i in marks:
        total += 1
    return f'{student_data.get('name')} got {total/len(marks)} percentage'

print(student_detail(10,12,40,24, name= "hari", address = "dang"))
print(student_detail(67,70,40,80, name= "ram", address = "taplejung"))


# practice questions
# soln from gpt 
# q1 : Create a function that:

# Takes multiple expense amounts using *args
# Accepts category info using **kwargs (e.g., food=500, travel=300)
# Task:

# track_expenses(100, 200, 50, food=150, travel=300)
# 👉 Requirements:

# Print total of *args
# Print each category with amount
# Show grand total


def track_expenses(*args, **kwargs):
    # total of args
    args_total = sum(args)
    print("Expense from args:", args_total)
    
    # print each category
    print("\nCategory expenses:")
    for category, amount in kwargs.items():
        print(f"{category}: {amount}")
    
    # total of kwargs
    kwargs_total = sum(kwargs.values())
    
    # grand total
    grand_total = args_total + kwargs_total
    print("\nGrand Total:", grand_total)


track_expenses(100, 200, 50, food=150, travel=300)


# soln from sudan sir

def track_expenses(*args, **kwargs):
    total = 0 
    for i in args:
        total +=i
    for j in kwargs: 
        print(j, kwargs[j])
        total += kwargs[j]
    print(total)

track_expenses(200,500,50, food = 110, travel = 3000)
"""

# q3
# 🔹 3. Discount System (E-commerce Logic)
# Create a function:

# *args → product prices
# **kwargs → discount rules like discount=10, tax=13
# Task:

# calculate_bill(1000, 2000, discount=10, tax=13)
# 👉 Requirements:

# Apply discount first
# Then apply tax
# Show final amount


def calc_bill(*args, **kwargs):
    total = 0
    for i in args:
        total +=i
    if kwargs.get('discount'):
        discount = kwargs.get('discount')/100
        total = total - total*discount
    if kwargs.get('tax'):
        tax = kwargs.get('tax')/100
        total = total + total*tax
        print("total:", total)

calc_bill(1000,5000,discount = 10, tax = 13)
calc_bill(1000,1000, discount = 3)
calc_bill(1000,8000, tax = 13)



# COMP REF
# ================================

# 📅 Python Functions Learning Notes

# Date: 18–20 March 2026

# ================================

"""
🔹 FUNCTIONS IN PYTHON

* A function is a reusable block of code.
* It must be called to execute.
* It can return values using `return`.
* Function names should start with lowercase (best practice).
* Always define functions before calling them.
  """

# -------------------------------

# BASIC FUNCTION

# -------------------------------

def test():
# Print a message
print("This is Bishal, function test")

```
# Return a value
return "data"
```

# Calling function

test()

# -------------------------------

# CHECK EVEN NUMBERS

# -------------------------------

def check_even_number():
result = []  # store even numbers
a = [2, 3, 4, 5, 1]

```
for i in a:
    # check if number is even
    if i % 2 == 0:
        result.append(i)

# return after loop completes
return result
```

print(check_even_number())

# -------------------------------

# USER INPUT FUNCTION

# -------------------------------

def intro_print():
print("Enter information: ")

```
# taking inputs
name = input("Enter Full Name: ")
age = int(input("Enter age: "))
address = input("Enter Address: ")

# formatted output
print(
    f"Hello {name}! You are {age} years old and live in {address}."
)

return "Intro printed"
```

intro_print()

# -------------------------------

# POSITIONAL ARGUMENTS

# -------------------------------

def user_info(relation, fname, lname):
# using positional arguments
return f"My {relation}'s name is {fname} {lname}."

print(user_info("wife", "Melina", "Baniya"))
print(user_info("father", "Ishwori", "Budhakshetri"))

# -------------------------------

# SIMPLE ARITHMETIC FUNCTION

# -------------------------------

def arth(a, b, c, d):
mult = a * b
sub = mult - c
div = sub / d

```
return f"Multiply: {mult}, Subtract: {sub}, Divide: {div}"
```

print(arth(1, 2, 3, 5))

# -------------------------------

# PERCENTAGE CALCULATION

# -------------------------------

def calc_percentage(marks):
total = sum(marks)  # sum of marks
percent = total / len(marks)  # average

```
return percent
```

print(calc_percentage([100, 58, 57]))

# -------------------------------

# KEYWORD ARGUMENTS

# -------------------------------

def calc_percentage_kw(names, marks):
total = sum(marks)
percent = total / len(marks)

```
return f"{names} got {percent}%"
```

print(calc_percentage_kw(names="Hari", marks=[100, 58, 57]))

# -------------------------------

# DEFAULT ARGUMENTS

# -------------------------------

def test_default(fname, lname="Sharma"):
# lname has default value
print(fname, lname)

test_default("Sudan")
test_default("Sudan", "Bhandari")

def area_of_circle(r, pi=3.14):
# calculate area
print(pi * r**2)

area_of_circle(7)

# -------------------------------

# ARBITRARY POSITIONAL (*args)

# -------------------------------

def sum_args(*args):
# args is a tuple
print(args)
print(type(args))

sum_args(1, 2, 3, 4)

# -------------------------------

# ARBITRARY KEYWORD (**kwargs)

# -------------------------------

def user_info_kwargs(**kwargs):
# kwargs is a dictionary
print(kwargs)

```
# safe access using .get()
print(kwargs.get('phone_num'))

print(type(kwargs))
print("--------------")
```

user_info_kwargs(name="ram", address="nepal", phone_num="9823")
user_info_kwargs(name="ram", address="nepal")

# -------------------------------

# COMBINING *args AND **kwargs

# -------------------------------

def test2(*args, **kwargs):
print("Args:", args)
print("Kwargs:", kwargs)

test2(1, 2, 3, name="bishal", address="taplejung")

# -------------------------------

# STUDENT DETAIL FUNCTION

# -------------------------------

def student_detail(*marks, **student_data):
# calculate average
avg = sum(marks) / len(marks)

```
# get name safely
name = student_data.get("name", "Unknown")

return f"{name} got {avg}%"
```

print(student_detail(10, 20, 30, name="Bishal"))

# -------------------------------

# EXPENSE TRACKER (PROJECT)

# -------------------------------

def track_expenses(*args, **kwargs):
# total of normal expenses
args_total = sum(args)
print("Expense from args:", args_total)

```
print("\nCategory expenses:")

# loop through categories
for category, amount in kwargs.items():
    print(f"{category}: {amount}")

# total of category expenses
kwargs_total = sum(kwargs.values())

# final total
grand_total = args_total + kwargs_total
print("\nGrand Total:", grand_total)
```

track_expenses(100, 200, 50, food=150, travel=300)

# -------------------------------

# BILL CALCULATION (DISCOUNT + TAX)

# -------------------------------

def calc_bill(*args, **kwargs):
# total product price
total = sum(args)

```
# apply discount if exists
if kwargs.get('discount'):
    discount = kwargs.get('discount') / 100
    total -= total * discount

# apply tax if exists
if kwargs.get('tax'):
    tax = kwargs.get('tax') / 100
    total += total * tax

print("Total:", total)
```

calc_bill(1000, 5000, discount=10, tax=13)
calc_bill(1000, 1000, discount=3)
calc_bill(1000, 8000, tax=13)
