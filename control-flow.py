# Python Control Flow - Its how python decides what to do next - like asking questions and making decisions based on the answers

# 1. If else
print("=== IF-ELSE ===")
python = int(input("Enter a amount: "))
if python == 30:
    print("You have enough money to buy python course")
else:
    print("You don't have enough money to buy python course")

# 2. IF-ELIF-ELSE
print("=== IF-ELIF-ELSE ===")
age = 20
if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")


# 3. Nested if
print("\n=== NESTED IF ===")  
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
    citizenship = input("Are you a citizen of the country? (yes/no): ")
    if citizenship.lower() == "yes":
        print("You can vote in the elections")
    else:
        print("You cannot vote as you are not a citizen")

# 4. FOR LOOP - until a certain condition is met, we can use for loop to iterate over a sequence of items
print("\n=== FOR LOOP ===")
for i in range(1,6):
    print(f"Number: {i}")

# 5. FOR LOOP with LIST - we can use for loop to iterate over a list of items
print("\n=== FOR LOOP with LIST ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# 6. WHILE LOOP - continues as long as a condition is true
print("\n=== WHILE LOOP ===")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# 7. BREAK STATEMENT - used to exit a loop prematurely when a certain condition is met
print("\n=== BREAK STATEMENT ===")
for i in range(10):
    if i == 5:
        break
    print(f"Value: {i}")

# 8. CONTINUE STATEMENT - used to skip the current iteration of a loop and move to the next iteration
print("\n=== CONTINUE STATEMENT ===")
for i in range(5):
    if i == 2:
        continue
    print(f"Value: {i}")

# 9. NESTED LOOPS - loops inside other loops
print("\n=== NESTED LOOPS ===")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 10. TERNARY OPERATOR - a shorthand way of writing an if-else statement in a single line
print("\n=== TERNARY OPERATOR ===")
score = 85
result = "Pass" if score >= 50 else "Fail"
print(f"Result: {result}")

# 11. LOGICAL OPERATORS (AND, OR, NOT)
print("\n=== LOGICAL OPERATORS ===")
x = 10
y = 20
if x > 5 and y < 30:
    print("Both conditions are true")
if x > 15 or y < 30:
    print("At least one condition is true")
if not (x > 20):
    print("x is not greater than 20")

# 12. TRY-EXCEPT (Error Handling)
print("\n=== TRY-EXCEPT ===")
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid integer conversion")
