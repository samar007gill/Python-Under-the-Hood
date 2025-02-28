x = 50  # Assigning an integer value
y = 100  # Another integer assignment

# Using a backslash to continue the statement (not recommended)
result = 10 * 2 + 3 ** 2 + \
         5 // 2 - 7

# Using parentheses to continue the statement (preferred method)
result = (10 * 2 + 3 ** 2 +
          5 // 2 - 7)

# Multi-line string (often used for docstrings or formatted text)
text = """Advanced Python example:
- Using expressions
- Handling conditions
- Defining functions"""

if x % 2 == 0:
    print("Even number")
    y = x ** 2  # Square of x
else:
    print("Odd number")
    y = x ** 3  # Cube of x

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")  # Using f-string for formatting

