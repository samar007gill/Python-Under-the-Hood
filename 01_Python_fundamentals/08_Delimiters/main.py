# 📌 Understanding Escape Characters & Strings in Python 🚀🐍

# Single-line comment explaining the purpose of this script

# Defining a string variable using double quotes
text = "Hello, World!"  # Double quotes are commonly used for defining strings in Python

# Defining another string variable using single quotes
greeting = 'Welcome to Python programming!'  # Strings can also be enclosed in single quotes

# Using an escape character to include double quotes inside a string
quote = "He said, \"Python is amazing!\""  # The backslash (\) escapes the double quotes

# Using an escape character for a newline (\n) and a tab space (\t)
formatted_text = "Line 1\nLine 2\t(Tabbed)"  
# \n moves the text to a new line, \t adds a tab space

# Using an escape character for a file path in Windows
path = 'C:\\Users\\Hashim\\Documents\\file.txt'  
# Double backslashes (\\) are required to avoid interpreting \U as a Unicode escape sequence

# Using a raw string (r'') to avoid escape sequence interpretation
raw_path = r'C:\Users\Hashim\Documents\file.txt'  
# The 'r' before the string makes it a raw string, treating backslashes literally

# Multi-line string using triple quotes
multiline_string = """This is a 
multi-line string example.
It spans multiple lines.
"""

# Printing all the defined variables
print("📢 Output of Escape Character Examples:\n")
print("🔹 Regular String:", text)
print("🔹 Greeting Message:", greeting)
print("🔹 String with Double Quotes:", quote)
print("🔹 Formatted Text with \\n and \\t:\n", formatted_text)
print("🔹 File Path with Escape Characters:", path)
print("🔹 Raw String File Path:", raw_path)
print("🔹 Multi-line String:\n", multiline_string)

# Demonstrating backslash usage in actual file handling
print("\n📢 Demonstrating Backslashes in File Handling:")
file_path = "C:\\Users\\Hashim\\Documents\\example.txt"  # Using escaped backslashes
print(f"Opening file: {file_path}")
try:
    with open(file_path, "w") as file:
        file.write("This is a test file.\nPython is powerful!")
    print("✅ File written successfully!")
except Exception as e:
    print("❌ Error:", e)


