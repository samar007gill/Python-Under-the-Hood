## **🚀 Python Keywords: The Core of Python Syntax 🎯**

## **🔹 What Are Keywords in Python?**
Keywords are **reserved words** in Python that have **predefined meanings** and **cannot** be used as variable names, function names, or identifiers. They define Python's syntax and structure, making them essential for writing correct programs.

## **📌 Characteristics of Python Keywords**
✔ **Case-Sensitive** → `True`, `False`, and `None` must be capitalized.  
✔ **Cannot Be Used as Identifiers** → You cannot name a variable `if`, `def`, or `return`.  
✔ **Only Contain Lowercase Letters** (except `True`, `False`, and `None`).  
✔ **Fixed in Number** → Python has a set number of keywords that **do not change** within a version.  

---

## **📊 Python 2 vs. Python 3 Keywords Comparison**

🔹 **Python 2 Keywords (31 total)**  
Python 2 had **fewer keywords**, with `print` and `exec` as **statements** instead of functions.  

🔹 **Python 3 Keywords (35 total)**  
Python 3 introduced `True`, `False`, `None`, `async`, and `await` as **new keywords**.  
✔ `print` is now a function (`print()` instead of `print "Hello"` in Python 2).  
✔ `exec` is no longer a keyword; it is a built-in function.  

---

## **📚 Categories of Python Keywords**

Python keywords serve different **purposes** in programming. Here’s how they are categorized:  

### **1️⃣ Control Flow Keywords**
These keywords are used for **decision-making and loops**:  
- `if`, `elif`, `else` → Conditional branching.  
- `for`, `while` → Looping structures.  
- `break`, `continue` → Controlling loop execution.  
- `pass` → Placeholder for future code.  
- `return`, `yield` → Used inside functions to return values.  

**Example:**  
```python
x = 10

if x > 5:
    print("Large")
elif x == 5:
    print("Equal to 5")
else:
    print("Small")
```

---

### **2️⃣ Function & Class Definition Keywords**
- `def` → Defines a function.  
- `lambda` → Creates an anonymous function.  
- `class` → Defines a class (Object-Oriented Programming).  

**Example:**  
```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

my_car = Car("Tesla")
print(my_car.get_brand())  # Output: Tesla
```

---

### **3️⃣ Logical & Comparison Operators**
- `and`, `or`, `not` → Boolean logic.  
- `is`, `in` → Identity and membership testing.  

**Example:**  
```python
x = [1, 2, 3]
y = x

print(x is y)  # True (same object reference)
print(2 in x)  # True (2 is in the list)
```

---

### **4️⃣ Exception Handling Keywords**
These keywords are used for handling errors:  
- `try`, `except`, `finally` → Error handling.  
- `raise` → Manually trigger exceptions.  

**Example:**  
```python
try:
    num = int("Python")  # Invalid conversion
except ValueError as e:
    print("Error:", e)
finally:
    print("Execution Completed!")
```

---

### **5️⃣ Asynchronous Programming Keywords**
- `async`, `await` → Used in asynchronous programming to handle non-blocking code execution.  

**Example:**  
```python
import asyncio

async def greet():
    print("Hello, Async World!")
    
asyncio.run(greet())  # Executes asynchronously
```

---

## **📋 Common Keywords and Their Uses**

| **Keyword** | **Description** | **Code Example** |
|------------|---------------|----------------|
| `False`, `True` | Data values from the Boolean data type | `False == (1 > 2)`, `True == (2 > 1)` |
| `and`, `or`, `not` | Logical operators | `(x and y)`, `(x or y)`, `(not x)` |
| `break` | Ends a loop prematurely | `while(True): break` |
| `continue` | Skips current iteration of a loop | `while(True): continue` |
| `class`, `def` | Define classes and functions | `class Car: pass`, `def my_func(): pass` |
| `if`, `elif`, `else` | Conditional execution | `if x > 3: print("Big")` |
| `for`, `while` | Looping constructs | `for i in [0,1,2]: print(i)` |
| `in` | Checks membership in a sequence | `42 in [2, 39, 42]` |
| `is` | Checks reference equality | `x is y` |
| `None` | Represents absence of a value | `def f(): return None` |
| `lambda` | Defines an anonymous function | `(lambda x: x + 3)(3)` |
| `return` | Ends function execution & returns value | `def incrementor(x): return x + 1` |

---

## **⚡ Best Practices for Using Keywords**
✔ **Use Descriptive Variable Names** → Avoid using similar names to keywords.  
✔ **Follow PEP 8 Guidelines** → Python’s official style guide.  
✔ **Use Keywords Properly** → Don't override built-in functions (`def print():`).  

---




