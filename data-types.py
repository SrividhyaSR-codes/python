# Python Data Types with Examples

# 1. STRING - sequence of characters/text with quotation marks
print("=== STRING ===")
name = "Alice"
print(f"String: {name}")
print(f"Type: {type(name)}")
print(f"Length: {len(name)}")
print()

# 2. INTEGER - whole numbers
print("=== INTEGER ===")
age = 25
print(f"Integer: {age}")
print(f"Type: {type(age)}")
print(f"Addition: {age + 5}")
print()

# 3. FLOAT - decimal numbers
print("=== FLOAT ===")
height = 5.9
print(f"Float: {height}")
print(f"Type: {type(height)}")
print(f"Multiplication: {height * 2}")
print()

# 4. BOOLEAN - True or False values
print("=== BOOLEAN ===")
is_student = True
print(f"Boolean: {is_student}")
print(f"Type: {type(is_student)}")
print(f"Not is_student: {not is_student}")
print()

# 5. LIST - ordered, mutable collection of items (within square brackets, we can give number of items/ordered collection of items)
print("=== LIST ===")
fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}")
print(f"Type: {type(fruits)}")
print(f"First element: {fruits[0]}")
fruits.append("grapes")
print(f"After append: {fruits}")
fruits.remove("banana")
print(f"After remove: {fruits}")
print(f"Length: {len(fruits)}")
print()

# 6. TUPLE - ordered, immutable collection of items (within parentheses, we can give number of items/ordered collection of items)
print("=== TUPLE ===")
colors = ("red", "green", "blue")
print(f"Tuple: {colors}")
print(f"Type: {type(colors)}")
print(f"Second element: {colors[1]}")
print(f"Length: {len(colors)}")
print()

# 7. DICTIONARY - dict is an unordered collection of key-value pairs (within curly braces, we can give number of items/ordered collection of items)
print("=== DICTIONARY ===")
person = {"name": "Srividhya", "age": 30, "city": "coimbatore"}
print(f"Dictionary: {person}")
print(f"Type: {type(person)}")
print(f"Name: {person['name']}")
person["job"] = "Engineer"
print(f"After adding job: {person}")
person.pop("job") # removes the key-value pair with key "job"
print(f"After removing job: {person}")
print()

# 8. SET - unordered collection of unique items (within curly braces, we can give number of items/ordered collection of items)
print("=== SET ===")
numbers = {1, 2, 3, 4, 5}
print(f"Set: {numbers}")
print(f"Type: {type(numbers)}")
numbers.add(6)
numbers.add(8)  
print(f"After adding 6: {numbers}")
print(f"After adding 8: {numbers}")
numbers.remove(6)
print(f"After removing 6: {numbers}")
print()

# 9. NONE - represents the absence of a value or a null value
print("=== NONE ===")
empty_value = None
print(f"None: {empty_value}")
print(f"Type: {type(empty_value)}")
print()

# 10. TYPE CONVERSION - converting one data type to another
print("=== TYPE CONVERSION ===")
str_num = "42"
int_num = int(str_num)
float_num = float(str_num)
print(f"String to Integer: {int_num}, Type: {type(int_num)}")
print(f"String to Float: {float_num}, Type: {type(float_num)}")
print(f"Integer to String: {str(int_num)}, Type: {type(str(int_num))}")

# List vs Tuple vs Set Vs Dictionary
#Feature        List          Tuple        Set           Dictionary
#Ordered        Yes           Yes          No            Yes
#Mutable        Yes           No           Yes           Yes
#Duplicates     Yes           Yes          No            Yes(Values)
#Indexing       Yes           Yes          No            Yes(by Keys)

