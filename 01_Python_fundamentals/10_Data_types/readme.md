# 🚀✨Python Primitive Data Types: The Core of Python Programming🎯

Understanding Python's **primitive data types** is crucial for mastering the language. These fundamental elements dictate how **data is stored, manipulated, and processed**. In Python, **everything is an object**, and each object has a specific type that defines its **behavior, operations, and memory allocation**.

---

## 1️⃣ What is an Object in Python? 🏗️
An **object** in Python is an **instance** of a data type that contains both **data (attributes)** and **methods (functions)** that operate on the data. Python follows an **object-oriented programming (OOP)** paradigm, treating every value as an object.

### 🔹 Key Characteristics of Objects:
- **Encapsulation**: Objects encapsulate both data and behavior.
- **Type System**: Every object belongs to a class, defining its attributes and operations.
- **Instance-Based**: Objects are created from classes, which serve as blueprints.
- **Memory Allocation**: Python dynamically manages memory using **reference counting** and **garbage collection**.
- **Dynamic Typing**: Objects can change types at runtime.

### ✨ Example:
```python
x = 42       # x is an object of type 'int'
y = "Hello"  # y is an object of type 'str'
print(x.__class__)  # Output: <class 'int'>
print(y.__class__)  # Output: <class 'str'>
```

---

## 2️⃣ Introduction to Data Types 📜
Each object in Python has a **type** that determines:
- **What operations can be performed**
- **Whether it is mutable (modifiable) or immutable (unchangeable)**
- **How it is stored in memory**
- **Performance implications**: Immutable objects are faster due to memory caching.

Python's built-in function `type()` can be used to determine an object’s data type.

### ✨ Example:
```python
print(type(42))         # Output: <class 'int'>
print(type(3.14))       # Output: <class 'float'>
print(type("Python"))  # Output: <class 'str'>
```

---

## 3️⃣ Mutable vs Immutable: Understanding Data Variability 🔄
- **Mutable Objects**: Can be changed after creation (e.g., **lists, dictionaries**).
- **Immutable Objects**: Cannot be modified once created (e.g., **integers, floats, strings, tuples**).

### ✨ Example:
```python
# Mutable Example
lst = [1, 2, 3]
lst.append(4)  # Modifies the existing object
print(lst)  # Output: [1, 2, 3, 4]

# Immutable Example
x = 5
y = x  # Copy reference
x = x + 1  # Creates a new object
print(x, y)  # Output: 6 5 (y remains unchanged)
```

### 🚀 Memory Optimization Insight:
Python **caches immutable objects** (like small integers and strings) for performance optimization. Modifying immutable objects creates **new memory allocations**, whereas mutable objects allow in-place modifications.

---

## 4️⃣ How are Objects Immutable? 🔐
When an **immutable object** is modified, Python **creates a new object** rather than altering the existing one.

### ✨ Example:
```python
x = 42  # Immutable integer object
y = "Hello"  # Immutable string object

x = x + 1  # Creates a new object 43
y += " World"  # Creates a new object "Hello World"
```
Here, `x` and `y` now reference **new objects**, while the original ones remain unchanged.

---

## 5️⃣ Type Checking in Python 🕵️‍♂️
Python provides built-in functions to **verify an object’s type**:

- `type(obj)`: Returns the type of the object.
- `isinstance(obj, type)`: Checks if an object is an instance of a specific type.
- `issubclass(cls1, cls2)`: Checks if a class is a subclass of another class.

### ✨ Example:
```python
x = 42
print(type(x))  # Output: <class 'int'>
print(isinstance(x, int))  # Output: True
print(isinstance(x, float))  # Output: False
```

---

## 6️⃣ Accessing Previous Object Values 🔄
Since **immutable objects cannot be modified**, storing previous values in a **separate variable** allows access to older states.

### ✨ Example:
```python
x = 42
original_x = x  # Preserve the original value
x = x + 1  # x now references 43

print("Current x:", x)  # Output: 43
print("Original x:", original_x)  # Output: 42
```

---

## 7️⃣ Key Takeaways 🎯
- **Immutable objects create new instances rather than modifying existing ones**, ensuring **data integrity and predictability**.
- **Memory efficiency**: Python optimizes immutable objects by storing commonly used values (e.g., small integers, strings) in a shared memory space known as **interning**.
- **Thread safety**: Since immutable objects cannot be changed, they can be safely shared across multiple threads without causing unexpected side effects.
- **Hashability**: Immutable objects (like tuples and strings) can be used as dictionary keys and set elements because they have a fixed hash value.

### ✨ Example:
```python
# Immutable objects as dictionary keys
data = {
    (1, 2, 3): "Tuple as a key",
    "name": "Python"
}
print(data[(1, 2, 3)])  # Output: Tuple as a key
```
This demonstrates how **immutability benefits data structures like dictionaries and sets**.

---

## 8️⃣ Numeric Data Types 🔢
Python supports three fundamental **numerical types**:
- **Integers (`int`)** - Whole numbers (e.g., `42`, `-10`, `1000`).
- **Floating-Point Numbers (`float`)** - Numbers with decimal precision (e.g., `3.14`, `2.5e-3`).
- **Complex Numbers (`complex`)** - Numbers with real and imaginary components (e.g., `3 + 4j`).

### ✨ Example:
```python
num1 = 10  # Integer
num2 = 3.14  # Floating point
num3 = 2 + 3j  # Complex number

print(type(num1))  # Output: <class 'int'>
print(type(num2))  # Output: <class 'float'>
print(type(num3))  # Output: <class 'complex'>
```

---
---

---

# **9️⃣ Integer Numbers 🏛️➕➖✖️➗**  
Python’s `int` type supports **arbitrary-precision arithmetic** (only limited by memory), and can be used in **scientific computing, cryptography, and data processing**.

### **Multiple Number Bases Supported**:  
🔹 **Decimal (Base-10)**: `3493`  
🔹 **Binary (Base-2)**: `0b10101` → `21`  
🔹 **Octal (Base-8)**: `0o6645` → `3429`  
🔹 **Hexadecimal (Base-16)**: `0xDA5` → `3493`  

🔍 **Advanced Integer Operations**:  
- **Bitwise Manipulation** (`&`, `|`, `^`, `~`, `<<`, `>>`)  
- **Mathematical Operations** (`pow()`, `divmod()`, `abs()`)  
- **Arbitrary-precision calculations**  

### **Examples:**
```python
# Integer representation in different bases
print(3493)         # Decimal
print(0b10101)      # Binary (Output: 21)
print(0o6645)       # Octal (Output: 3429)
print(0xDA5)        # Hexadecimal (Output: 3493)

# Advanced operations
print(pow(2, 10))     # 2^10 (Output: 1024)
print(divmod(10, 3))  # (Quotient, Remainder) -> Output: (3, 1)
print(abs(-25))       # Absolute value -> Output: 25

# Bitwise operations
x, y = 0b1101, 0b1011
print(x & y)  # Bitwise AND -> Output: 9
print(x | y)  # Bitwise OR -> Output: 15
print(x ^ y)  # Bitwise XOR -> Output: 6
```

---

# **🔟 Floating-Point Numbers 🌊🧮**  
Python’s `float` type follows the **IEEE 754 standard** (double-precision floating-point arithmetic).  

### **Key Features**:  
✅ **Scientific Notation**: `1.23e4 == 12300.0`  
✅ **Infinity & NaN Support**: `float('inf')`, `float('-inf')`, `float('nan')`  
✅ **Floating-Point Precision Issues**  

### **Examples:**
```python
import math
from decimal import Decimal

# Standard float examples
print(3.14, 1e3, 2.5e-2)  # Output: 3.14, 1000.0, 0.025

# Special floating-point values
print(float('inf'))   # Infinity
print(float('-inf'))  # Negative Infinity
print(float('nan'))   # Not-a-Number (NaN)

# Precision issue in floating points
print(0.1 + 0.2)  # Output: 0.30000000000000004 (Precision issue)

# Fixing precision issues using Decimal
print(Decimal('0.1') + Decimal('0.2'))  # Output: 0.3 (Corrected)
```

---

# **1️⃣1️⃣ Complex Numbers 🌀🔢**  
Python **natively supports complex numbers** using `a + bj` notation.  

### **Key Features**:  
✅ **Real & Imaginary Parts** (`z.real`, `z.imag`)  
✅ **Magnitude & Conjugates** (`abs(z)`, `z.conjugate()`)  
✅ **Operations using `cmath` module**  

### **Examples:**
```python
import cmath

z = 3 + 4j
print(z.real, z.imag)  # Output: 3.0 4.0

# Magnitude (Modulus)
print(abs(z))  # Output: 5.0

# Complex exponential function
print(cmath.exp(1j * cmath.pi))  # Euler’s identity: e^(iπ) = -1

# Square root of negative numbers
print(cmath.sqrt(-16))  # Output: 4j
```

---

# **1️⃣2️⃣ Underscores in Numeric Literals 🔍🔢**  
Introduced in **Python 3.6**, underscores (`_`) improve readability in large numbers.

### **Use Cases**:  
✅ **Readable large numbers**: `1_000_000_000`  
✅ **Hexadecimal memory addresses**: `0xDEAD_BEEF`  
✅ **Binary machine code**: `0b1101_0101`  

### **Examples:**
```python
num = 1_000_000_000  # Equivalent to 1000000000
hex_val = 0xDEAD_BEEF  # Readable hex representation
bin_val = 0b1101_0101  # Readable binary representation

print(num, hex_val, bin_val)
```

---

# **1️⃣3️⃣ String Data Type 📜📝**  
Python **strings (`str`) are immutable Unicode sequences**.

### **Advanced String Techniques**:  
✅ **Multiline Strings** (`""" """`)  
✅ **Raw Strings (`r"..."`)** → Used for regex & file paths  
✅ **String Interpolation (`f-strings`)**  

### **Examples:**
```python
# Multi-line string
multi_line = """This
is
a multi-line string."""
print(multi_line)

# Raw String (useful for file paths and regex)
path = r"C:\Users\Samar\Documents"
print(path)  # Output: C:\Users\Samar\Documents

# f-strings for dynamic formatting
name = "Samar"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

---

# **1️⃣4️⃣ Boolean Data Type 🎭💡**  
Python's `bool` type represents **binary truth values** (`True` or `False`).  

### **Boolean Behavior**:  
✅ **`True` is equivalent to `1`**  
✅ **`False` is equivalent to `0`**  
✅ **Booleans can be used in arithmetic**  

### **Examples:**
```python
is_python_fun = True
print(type(is_python_fun))  # Output: <class 'bool'>

# Boolean arithmetic
print(True + True)   # Output: 2
print(False * 10)    # Output: 0
print(True * 5 - 3)  # Output: 2
```

---

# **1️⃣5️⃣ Logical Operations ⚖️🤖**  
Logical operators are essential for **control flow, AI, and decision-making systems**.

### **Logical Operators**:  
✅ **`and`** → True if **both** values are True  
✅ **`or`** → True if **at least one** is True  
✅ **`not`** → Inverts the truth value  

### **Examples:**
```python
a, b = True, False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False

# Short-circuit behavior
print(5 > 3 and "Hello")  # Output: "Hello"
print(False or 42)        # Output: 42
```

---

# **1️⃣6️⃣ Primitive Data Types Overview 🧩🚀**  
### **Python’s Core Data Types:**
| **Data Type** | **Description** | **Example** |
|--------------|----------------|------------|
| `int`       | Whole numbers | `42`, `-7` |
| `float`     | Decimal numbers | `3.14`, `-2.5e2` |
| `complex`   | Real & imaginary | `3 + 4j` |
| `str`       | Text data | `"Python"`, `'Data'` |
| `bool`      | Boolean values | `True`, `False` |

---

# **🎯 Conclusion: Becoming a Python Master 🧠💡**  
🚀 **Master these types to write efficient Python code!**
