# Python Primitive Data Types - A Detailed Exploration

# ---------------------- INTEGER TYPE ----------------------
print("\n🔹 Integer Type (int) 🔹")

x = 42  # Immutable integer
y = -15  # Negative integer
z = 0  # Zero is also an integer

print("x:", x, "Type:", type(x))  # Output: 42 <class 'int'>
print("y:", y, "Type:", type(y))  # Output: -15 <class 'int'>
print("z:", z, "Type:", type(z))  # Output: 0 <class 'int'>

# Integer operations
a = 10
b = 3
print("Addition:", a + b)  # 13
print("Subtraction:", a - b)  # 7
print("Multiplication:", a * b)  # 30
print("Division (Floating Point):", a / b)  # 3.333...
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)  # 1
print("Exponentiation:", a ** b)  # 1000 (10^3)

# Binary, Octal, Hexadecimal
binary_num = 0b1010  # 10 in binary
octal_num = 0o12  # 10 in octal
hex_num = 0xA  # 10 in hexadecimal
print("Binary 0b1010:", binary_num)
print("Octal 0o12:", octal_num)
print("Hexadecimal 0xA:", hex_num)

# ---------------------- FLOAT TYPE ----------------------
print("\n🔹 Float Type (float) 🔹")

f1 = 3.14  # Floating-point number
f2 = -0.001  # Negative float
f3 = 1.5e3  # Scientific notation (1.5 * 10^3 = 1500.0)

print("f1:", f1, "Type:", type(f1))
print("f2:", f2, "Type:", type(f2))
print("f3:", f3, "Type:", type(f3))

# Float precision issue
print("0.1 + 0.2 == 0.3?", 0.1 + 0.2 == 0.3)  # False due to floating-point precision errors

# ---------------------- COMPLEX TYPE ----------------------
print("\n🔹 Complex Type (complex) 🔹")

c1 = 2 + 3j  # Complex number
c2 = complex(5, -4)  # Another way to create a complex number

print("c1:", c1, "Type:", type(c1))
print("c2:", c2, "Type:", type(c2))

# Complex number operations
print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)
print("Real part of c1:", c1.real)
print("Imaginary part of c1:", c1.imag)

# ---------------------- STRING TYPE ----------------------
print("\n🔹 String Type (str) 🔹")

s1 = "Hello, Python!"  # Double quotes
s2 = 'Single quotes work too'  # Single quotes
s3 = """Triple-quoted strings can span multiple lines."""
s4 = "Python" * 3  # String repetition

print("s1:", s1, "Type:", type(s1))
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)  # Output: PythonPythonPython

# String operations
print("Uppercase:", s1.upper())
print("Lowercase:", s1.lower())
print("String length:", len(s1))
print("Substring check:", "Python" in s1)  # True

# ---------------------- BOOLEAN TYPE ----------------------
print("\n🔹 Boolean Type (bool) 🔹")

is_python_fun = True
is_python_hard = False

print("is_python_fun:", is_python_fun, "Type:", type(is_python_fun))
print("is_python_hard:", is_python_hard)

# Boolean logic
print("AND:", is_python_fun and is_python_hard)  # False
print("OR:", is_python_fun or is_python_hard)  # True
print("NOT:", not is_python_fun)  # False

# Boolean with numbers
print("bool(1):", bool(1))  # True
print("bool(0):", bool(0))  # False
print("bool(-42):", bool(-42))  # True
print("bool(0.0):", bool(0.0))  # False

# ---------------------- NONE TYPE ----------------------
print("\n🔹 None Type (NoneType) 🔹")

nothing = None
print("nothing:", nothing, "Type:", type(nothing))

# None is used as a placeholder or to indicate "no value"
def example_function():
    return None  # Function with no return value

print("Function returns:", example_function())

# ---------------------- IMMUTABILITY CONCEPT ----------------------
print("\n🔹 Immutability Concept 🔹")

x = 10
print("Original x:", x, "Memory Address:", id(x))

x = x + 1  # This creates a new integer object
print("Modified x:", x, "New Memory Address:", id(x))

s = "Python"
print("Original string:", s, "Memory Address:", id(s))

s = s + " Rocks!"  # This creates a new string object
print("Modified string:", s, "New Memory Address:", id(s))

# ---------------------- TYPE CONVERSIONS ----------------------
print("\n🔹 Type Conversions 🔹")

# Converting between types
num = 100
float_num = float(num)
str_num = str(num)
bool_num = bool(num)

print("int to float:", float_num, "Type:", type(float_num))
print("int to str:", str_num, "Type:", type(str_num))
print("int to bool:", bool_num, "Type:", type(bool_num))

# String to int/float
str_val = "42"
int_val = int(str_val)
float_val = float(str_val)

print("String to int:", int_val, "Type:", type(int_val))
print("String to float:", float_val, "Type:", type(float_val))

# Invalid conversions (will raise errors)
# print(int("hello"))  # ValueError
# print(float("abc"))  # ValueError

# ---------------------- SUMMARY ----------------------
print("\n🔹 Summary of Primitive Data Types 🔹")
primitive_data_types = {
    "Integer (int)": "Whole numbers, positive/negative, e.g., 42, -7, 0",
    "Float (float)": "Decimal numbers, e.g., 3.14, -0.001, 1.5e3",
    "Complex (complex)": "Numbers with real and imaginary parts, e.g., 2+3j",
    "String (str)": "Text enclosed in quotes, e.g., 'Hello'",
    "Boolean (bool)": "True or False values, e.g., True, False",
    "NoneType (None)": "Represents 'no value', e.g., None",
}

for dtype, desc in primitive_data_types.items():
    print(f"{dtype}: {desc}")

print("\n✅ Script Execution Complete!")
