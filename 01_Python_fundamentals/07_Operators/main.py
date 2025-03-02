# 1️⃣ Arithmetic Operators ➕➖✖️➗
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)      # 13
print("Subtraction:", a - b)   # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)      # 3.3333...
print("Modulus:", a % b)       # 1
print("Exponentiation:", a ** b) # 1000
print("Floor Division:", a // b) # 3
print("\n")

# 2️⃣ Comparison Operators 🔍⚖️
print("Comparison Operators:")
print("a < b:", a < b)   # False
print("a <= b:", a <= b)  # False
print("a > b:", a > b)   # True
print("a >= b:", a >= b)  # True
print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("\n")

# 3️⃣ Logical Operators 🧠💡
x = True
y = False

print("Logical Operators:")
print("x and y:", x and y)  # False
print("x or y:", x or y)    # True
print("not x:", not x)      # False
print("\n")

# 4️⃣ Bitwise Operators 🧮🖥️
a = 5  # 101 in binary
b = 3  # 011 in binary

print("Bitwise Operators:")
print("Bitwise AND:", a & b)  # 1
print("Bitwise OR:", a | b)   # 7
print("Bitwise XOR:", a ^ b)  # 6
print("Bitwise NOT (~a):", ~a) # -6
print("Left Shift (a << 1):", a << 1) # 10
print("Right Shift (a >> 1):", a >> 1) # 2
print("\n")

# 5️⃣ Assignment Operators 🖊️📝
x = 5
print("Assignment Operators:")
x += 3  # x = x + 3
print("x after += 3:", x)  # 8

x *= 2  # x = x * 2
print("x after *= 2:", x)  # 16
print("\n")

# 6️⃣ Identity & Membership Operators 🔍👁️
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("Identity & Membership Operators:")
print("a is b:", a is b)  # True
print("a is c:", a is c)  # False (different memory locations)
print("2 in a:", 2 in a)  # True
print("5 not in a:", 5 not in a)  # True

