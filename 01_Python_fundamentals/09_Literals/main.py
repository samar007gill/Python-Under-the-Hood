# 📌 NUMERIC LITERALS 🔢  

# Integer literals (whole numbers, positive or negative, without decimals)  
int_literal = 42  # Standard integer  
neg_int = -10  # Negative integer  
binary_int = 0b101010  # Binary representation (42 in decimal)  
octal_int = 0o52  # Octal representation (42 in decimal)  
hex_int = 0x2A  # Hexadecimal representation (42 in decimal)  

print("Integer Literals:", int_literal, neg_int, binary_int, octal_int, hex_int)  

# Floating-point literals (numbers with decimals)  
float_literal = 3.14  # Standard floating-point number  
scientific_float = 1.5e3  # 1.5 * 10^3 = 1500.0  

print("Floating-Point Literals:", float_literal, scientific_float)  

# Complex number literals (real + imaginary part)  
complex_literal = 1.0 + 2.5j  # 1.0 is real, 2.5j is imaginary  
print("Complex Number Literal: Real:", complex_literal.real, "Imaginary:", complex_literal.imag)  

print("\n" + "="*50 + "\n")  # Separator  

# ------------------------------------------  

# 📌 STRING LITERALS 📝  
# Single-quoted string  
single_quoted = 'hello'  

# Double-quoted string  
double_quoted = "world"  

# Triple-quoted string (multi-line)  
triple_quoted = """This is a  
multi-line string  
in Python."""  

# Escape sequences in strings  
escaped_string = "Hello \"Python\" \nNew line added!"  # \" to include quotes, \n for a new line  

print("String Literals:")
print("Single-Quoted:", single_quoted)
print("Double-Quoted:", double_quoted)
print("Triple-Quoted:", triple_quoted)
print("Escaped String:", escaped_string)

print("\n" + "="*50 + "\n")  # Separator  

# ------------------------------------------  

# 📌 COLLECTION (CONTAINER) LITERALS 📦  

# 🔹 LIST LITERAL (Ordered, Mutable, Allows Duplicates)  
my_list = [42, 3.14, 'hello']  # A list containing an integer, a float, and a string  
empty_list = []  # Empty list  

print("List Literal:", my_list)
print("Empty List:", empty_list)

# 🔹 TUPLE LITERAL (Ordered, Immutable, Allows Duplicates)  
my_tuple = (100, 200, 300)  # Tuple with integer values  
empty_tuple = ()  # Empty tuple  

print("Tuple Literal:", my_tuple)
print("Empty Tuple:", empty_tuple)

# 🔹 DICTIONARY LITERAL (Key-Value Pairs, Unordered, Mutable, Unique Keys)  
my_dict = {'x': 42, 'y': 3.14, 'message': "Python"}  
empty_dict = {}  # Empty dictionary  

print("Dictionary Literal:", my_dict)
print("Empty Dictionary:", empty_dict)

# Accessing dictionary values  
print("Accessing Dictionary Values:", "x =", my_dict['x'], ", y =", my_dict.get('y'))

# 🔹 SET LITERAL (Unordered, Unique Values, Mutable)  
my_set = {1, 2, 4, 8, 'string', 4, 2}  # Duplicates are automatically removed  
print("Set Literal:", my_set)

# Creating an empty set (⚠️ {} creates an empty dictionary, not a set)  
empty_set = set()  # Correct way to create an empty set  

print("Empty Set Type:", type(empty_set))  # Output: <class 'set'>  
print("Empty Dictionary Type:", type(empty_dict))  # Output: <class 'dict'>  
