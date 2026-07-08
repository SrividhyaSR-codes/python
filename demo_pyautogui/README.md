# Python Basics Guide

A comprehensive guide covering fundamental Python concepts for beginners.

---

## Table of Contents

1. [Installation](#installation)
2. [Running Python](#running-python)
3. [Basic Syntax](#basic-syntax)
4. [Variables and Data Types](#variables-and-data-types)
5. [Operators](#operators)
6. [Control Flow](#control-flow)
7. [Functions](#functions)
8. [Data Structures](#data-structures)
9. [String Operations](#string-operations)
10. [File I/O](#file-io)
11. [Error Handling](#error-handling)
12. [Best Practices](#best-practices)

---

## Installation

### Windows
1. Download Python from [python.org](https://www.python.org)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Click "Install Now"

### Verify Installation
```bash
python --version
```

---

## Running Python

### Interactive Mode
```bash
python
```

### Run a Script
```bash
python hello.py
```

### Run a Single Command
```bash
python -c "print('Hello, World!')"
```

---

## Basic Syntax

### Comments
```python
# This is a single-line comment

"""
This is a multi-line comment
or docstring
"""
```

### Indentation
Python uses indentation (spaces) to define code blocks:
```python
if True:
    print("This is indented")
```

### Print Statement
```python
print("Hello, World!")
print("Multiple", "values")
print("Value:", 42)
```

---

## Variables and Data Types

### Variable Assignment
```python
name = "Alice"          # String
age = 25                # Integer
height = 5.7            # Float
is_student = True       # Boolean
```

### Data Types
```python
# String
text = "Python"

# Integer
number = 100

# Float
decimal = 3.14

# Boolean
flag = True

# None (null equivalent)
empty = None

# Check data type
print(type(number))     # <class 'int'>
print(type(text))       # <class 'str'>
```

### Type Conversion
```python
int("10")               # 10
float("3.14")           # 3.14
str(42)                 # "42"
bool(1)                 # True
```

---

## Operators

### Arithmetic Operators
```python
10 + 5      # Addition: 15
10 - 5      # Subtraction: 5
10 * 5      # Multiplication: 50
10 / 5      # Division: 2.0
10 // 3     # Floor Division: 3
10 % 3      # Modulo (remainder): 1
2 ** 3      # Exponentiation: 8
```

### Comparison Operators
```python
10 == 10    # Equal: True
10 != 5     # Not Equal: True
10 > 5      # Greater Than: True
10 < 5      # Less Than: False
10 >= 5     # Greater or Equal: True
10 <= 5     # Less or Equal: False
```

### Logical Operators
```python
True and False   # False
True or False    # True
not True         # False
```

### Assignment Operators
```python
x = 5
x += 3          # x = x + 3 (x = 8)
x -= 2          # x = x - 2 (x = 3)
x *= 2          # x = x * 2 (x = 6)
x /= 2          # x = x / 2 (x = 3.0)
```

---

## Control Flow

### If-Else Statement
```python
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

### Ternary Operator
```python
status = "Adult" if age >= 18 else "Minor"
```

### For Loop
```python
# Loop through range
for i in range(5):
    print(i)            # 0, 1, 2, 3, 4

# Loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control
```python
# break: Exit loop
for i in range(10):
    if i == 5:
        break
    print(i)

# continue: Skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## Functions

### Basic Function
```python
def greet(name):
    return "Hello, " + name

print(greet("Alice"))   # Hello, Alice
```

### Function with Default Parameters
```python
def greet(name="Guest"):
    return "Hello, " + name

print(greet())          # Hello, Guest
print(greet("Bob"))     # Hello, Bob
```

### Multiple Return Values
```python
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)             # 10 20
```

### Variable Arguments
```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))     # 6
```

### Keyword Arguments
```python
def describe_person(name, age=25, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}")

describe_person("Alice")
describe_person("Bob", 30)
describe_person("Charlie", 28, "New York")
```

---

## Data Structures

### Lists (Arrays)
```python
# Create a list
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Access elements
print(numbers[0])       # 1 (first element)
print(numbers[-1])      # 5 (last element)

# Slicing
print(numbers[1:3])     # [2, 3]

# List methods
numbers.append(6)       # Add to end
numbers.insert(0, 0)    # Insert at position
numbers.remove(3)       # Remove value
popped = numbers.pop()  # Remove and return last

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

### Tuples (Immutable Lists)
```python
# Create a tuple
coordinates = (10, 20)
colors = ("red", "green", "blue")

# Access elements (same as lists)
print(coordinates[0])   # 10

# Tuples cannot be modified
# coordinates[0] = 5    # Error!
```

### Dictionaries (Key-Value Pairs)
```python
# Create a dictionary
person = {"name": "Alice", "age": 25, "city": "NY"}

# Access values
print(person["name"])   # Alice

# Add/Update
person["age"] = 26
person["email"] = "alice@example.com"

# Remove
del person["city"]

# Dictionary methods
print(person.keys())    # dict_keys(['name', 'age', 'email'])
print(person.values())  # dict_values(['Alice', 26, 'alice@example.com'])

# Loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")
```

### Sets (Unique Values)
```python
# Create a set
numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4} (duplicates removed)

# Add/Remove
numbers.add(5)
numbers.remove(3)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)            # Intersection: {3}
print(a | b)            # Union: {1, 2, 3, 4, 5}
```

---

## String Operations

### String Basics
```python
text = "Hello, World!"

# Length
print(len(text))        # 13

# Access characters
print(text[0])          # H
print(text[-1])         # !

# Slicing
print(text[0:5])        # Hello
```

### String Methods
```python
text = "  Python Programming  "

# Case
print(text.upper())     # PYTHON PROGRAMMING
print(text.lower())     # python programming

# Whitespace
print(text.strip())     # Python Programming

# Search and Replace
print("Python" in text)         # True
print(text.find("Python"))      # 2
print(text.replace("Python", "Java"))

# Split and Join
words = "apple banana cherry".split()     # ['apple', 'banana', 'cherry']
result = " ".join(words)                  # apple banana cherry
```

### String Formatting
```python
# f-strings (recommended)
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")

# format() method
print("My name is {} and I'm {} years old".format(name, age))

# String concatenation
print("My name is " + name)
```

---

## File I/O

### Reading Files
```python
# Read entire file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines as list
with open("file.txt", "r") as file:
    lines = file.readlines()
```

### Writing Files
```python
# Write to file
with open("file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python is great!")

# Append to file
with open("file.txt", "a") as file:
    file.write("\nNew line")
```

### File Modes
```
"r"   - Read (default)
"w"   - Write (overwrites existing content)
"a"   - Append (adds to end)
"x"   - Create new file
"b"   - Binary mode (e.g., "rb", "wb")
```

---

## Error Handling

### Try-Except
```python
try:
    number = int("hello")
except ValueError:
    print("Invalid input")
except Exception as e:
    print(f"Error: {e}")
```

### Try-Except-Else-Finally
```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
except IOError:
    print("Cannot read file")
else:
    print("File read successfully")
finally:
    print("Cleanup code always runs")
    if 'file' in locals():
        file.close()
```

### Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")
```

---

## Best Practices

### 1. Use Meaningful Variable Names
```python
# Good
user_age = 25
total_price = 99.99

# Bad
a = 25
tp = 99.99
```

### 2. Follow PEP 8 Style Guide
```python
# Good
def calculate_total(price, quantity):
    return price * quantity

# Bad
def calculateTotal(price,quantity):
    return price*quantity
```

### 3. Use Comments for Complex Logic
```python
# Calculate compound interest
principal = 1000
rate = 0.05
years = 2
amount = principal * (1 + rate) ** years
```

### 4. Keep Functions Small and Focused
```python
# Good
def validate_email(email):
    return "@" in email

def save_user(name, email):
    if validate_email(email):
        print(f"Saving {name}")
```

### 5. Use Virtual Environments
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Deactivate
deactivate
```

### 6. Use List Comprehensions
```python
# Good
squares = [x**2 for x in range(10)]

# Less efficient
squares = []
for x in range(10):
    squares.append(x**2)
```

### 7. Handle Exceptions Properly
```python
# Good
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Bad (catches everything silently)
try:
    result = 10 / 0
except:
    pass
```

---

## Common Mistakes to Avoid

### 1. Indentation Errors
```python
# Wrong - inconsistent indentation
if True:
  print("space")
    print("tab")  # Error!

# Correct - consistent indentation
if True:
    print("space")
    print("space")
```

### 2. Off-by-One Errors
```python
numbers = [1, 2, 3, 4, 5]
# Lists are 0-indexed
print(numbers[0])   # 1 (not 0)
print(numbers[4])   # 5 (not 6)
```

### 3. Mutable Default Arguments
```python
# Bad
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

# Good
def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

### 4. Forgetting to Initialize Variables
```python
# Bad
for i in range(5):
    sum += i  # NameError: sum not defined

# Good
sum = 0
for i in range(5):
    sum += i
```

---

## Useful Resources

- **Official Python Docs**: https://docs.python.org/3/
- **Python.org Tutorial**: https://docs.python.org/3/tutorial/
- **Real Python**: https://realpython.com
- **GeeksforGeeks Python**: https://www.geeksforgeeks.org/python-programming-language/
- **PEP 8 Style Guide**: https://www.python.org/dev/peps/pep-0008/

---

## Quick Reference

| Concept | Example |
|---------|---------|
| Print | `print("Hello")` |
| Variable | `x = 10` |
| List | `[1, 2, 3]` |
| Dictionary | `{"key": "value"}` |
| Function | `def func(): return 1` |
| If Statement | `if x > 5: print("yes")` |
| For Loop | `for i in range(5): print(i)` |
| String Format | `f"Value: {x}"` |
| List Comprehension | `[x**2 for x in range(5)]` |
| Try-Except | `try: ... except: ...` |

---

**Happy Learning! 🐍**

Start with small programs and gradually build more complex projects. Practice is key to mastering Python!
