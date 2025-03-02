
---

# **Python Primitive Data Types** 🧮📊  
Understanding **data types** is essential for mastering Python, as they define the nature of values and the operations that can be performed on them. In Python, every value is an **object**, and each object belongs to a specific type.  

---

## **🔹 What is an Object in Python? 🏗️**  
An **object** is a fundamental concept in Python. It represents an instance of a data type that holds **data (attributes)** and provides **methods (functions)** to operate on that data. Python follows an **object-oriented paradigm**, meaning **everything** in Python is an **object**! 🧱  

### **📝 Key Characteristics of an Object:**  
✔ **Encapsulation**: An object bundles data and methods together.  
✔ **Type Association**: Each object has a defined **type (class)** that dictates its behavior.  
✔ **Instance of a Class**: Objects are created based on **class blueprints**.  

### **💡 Example:**  
```python
x = 42  # An integer object of type 'int'
y = "Hello, World!"  # A string object of type 'str'

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>
```

---

## **🔍 Introduction to Data Types in Python 📂**  
### **🛠️ Key Properties:**  
✅ **Objects**: Every value is an **object** in Python.  
✅ **Type Enforcement**: Each object has a **specific type** that dictates its behavior.  
✅ **Mutability**: Objects can either be **mutable** (modifiable) or **immutable** (unchangeable).  

### **🧩 Mutable vs Immutable Objects**  
🔹 **Mutable Objects** (modifiable) – Example: Lists (`list`), Dictionaries (`dict`).  
🔹 **Immutable Objects** (unchangeable) – Example: Integers (`int`), Strings (`str`), Tuples (`tuple`).  

---

## **🧐 How Does Python Handle Immutable Objects? 🔄**  
Python optimizes memory by **not modifying** immutable objects directly. Instead, when a change is attempted, it **creates a new object** and updates the reference. The original value remains intact.  

### **📝 Example (Immutable Integer & String):**  
```python
x = 42  # Immutable integer
y = "Hello"  # Immutable string

x = x + 1  # A new integer object (43) is created
y += " World"  # A new string object ("Hello World") is created

print(x)  # Output: 43
print(y)  # Output: "Hello World"
```

🔹 **Explanation:**  
✔ **Numbers & Strings don't change**—Python **creates new objects** instead!  
✔ **Original values remain unchanged** unless explicitly stored in another variable.  

---

## **📊 Numeric Data Types in Python 🧮**  
Python provides three primary **numeric types**:  

| Data Type | Description | Example |
|-----------|------------|---------|
| **Integer (`int`)** | Whole numbers, positive or negative | `42`, `-15`, `100000` |
| **Floating-Point (`float`)** | Decimal numbers | `3.14`, `-0.001`, `2.5e3` |
| **Complex (`complex`)** | Numbers with a real and imaginary part | `3 + 4j`, `2.5 - 1.1j` |

---

### **🔢 Integer (`int`) – Whole Numbers**  
Python **integers** are unlimited in precision and can be written in various **number systems**:  

📌 **Supported Bases:**  
- **Decimal (Base-10)** – Default (e.g., `42`)  
- **Binary (Base-2)** – Prefix with `0b` (e.g., `0b101010` → 42)  
- **Octal (Base-8)** – Prefix with `0o` (e.g., `0o52` → 42)  
- **Hexadecimal (Base-16)** – Prefix with `0x` (e.g., `0x2A` → 42)  

🔹 **Example:**  
```python
decimal = 42
binary = 0b101010
octal = 0o52
hexadecimal = 0x2A

print(decimal, binary, octal, hexadecimal)  # Output: 42 42 42 42
```

---

