#Operators in Python 

# Values
A = 10
B = 5
C = 3

# Arithmetic operators (+, -, *, /, //, %, **)
print(f"Addition: {A} + {B} = {A + B}")
print(f"Subtraction: {A} - {B} = {A - B}")
print(f"Multiplication: {A} * {B} = {A * B}")
print(f"Division: {A} / {B} = {A / B}")
print(f"Floor division: {A} // {B} = {A // B}")
print(f"Modulus: {A} % {B} = {A % B}")
print(f"Exponent: {A} ** {C} = {A ** C}")

# Parentheses affecting precedence 
print(f"Precedence: (A + B) * C = {(A + B) * C}")

# Bitwise operators (&, |, ^, <<, >>)
print(f"Bitwise AND: {A} & {B} = {A & B}")
print(f"Bitwise OR: {A} | {B} = {A | B}")
print(f"Bitwise XOR: {A} ^ {B} = {A ^ B}")
print(f"Left shift A<<1: {A} << 1 = {A << 1}")
print(f"Right shift A>>1: {A} >> 1 = {A >> 1}")

# Comparison operators(==, !=, >, <, >=, <=)
print(f"Equal: {A} == {B} -> {A == B}")
print(f"Not equal: {A} != {B} -> {A != B}")
print(f"Greater: {A} > {B} -> {A > B}")
print(f"Less or equal: {A} <= {B} -> {A <= B}")

# Logical operators (and, or, not)
print(f"Logical and: (A > 0) and (B > 0) -> {(A > 0) and (B > 0)}")
print(f"Logical or: (A < 0) or (B > 0) -> {(A < 0) or (B > 0)}")
print(f"Logical not: not (A == B) -> {not (A == B)}")

# Assignment operators (=, +=, -=, *=, /=, %=, //=, **=)
X = 2
X += 3
print(f"Assignment (+=): X = 2; X += 3 -> {X}")
X *= 4
print(f"Assignment (*=): X *= 4 -> {X}")

# Identity operators (is, is not)
Y = X
Z = X
print(f"is identity: Y is Z -> {Y is Z}")
print(f"is not identity: Y is not Z -> {Y is not Z}")

# Membership operators (in, not in)
items = [A, B, C]
print(f"Membership in list: 5 in items -> {5 in items}")
print(f"Membership not in list: 7 not in items -> {7 not in items}")

# End


