import sys
import gc
import weakref

# 🔥 Dynamic Typing & Reference Rebinding
x = 42  # x references an integer object
print(f"x ({id(x)}) -> {x}")

x = "hello"  # x now references a string object
print(f"x ({id(x)}) -> {x}")

# ✅ Immutable Objects & Rebinding
x = 10    # Binding: x is now a reference to integer 10
y = x     # Both x and y refer to the same immutable object
x = 20    # Rebinding: x now refers to a new integer 20, y is unchanged

print(f"x ({id(x)}) -> {x}")
print(f"y ({id(y)}) -> {y}")  # y still refers to the original 10

# 🔄 Deleting a Variable
x = 100  
del x  # x is unbound, the object may be garbage collected

# ✅ Mutable Objects & Reference Sharing
a = [1, 2, 3]  # a points to a mutable list object
b = a          # b now also references the same object (shallow copy)

b.append(4)  # Modifying b also affects a
print("a:", a)  # ✅ Output: [1, 2, 3, 4]
print("b:", b)  # ✅ Output: [1, 2, 3, 4]

del a  # a is unbound, but the list object persists because b still refers to it
print("b still holds:", b)

# 🔬 Checking Reference Count
print("Reference Count of b's list:", sys.getrefcount(b))  # 📊 Shows ref count

# ✅ Deep Copy vs. Shallow Copy
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original_list)  # Creates a new outer list, but inner lists are shared
deep_copy = copy.deepcopy(original_list)  # Creates completely independent copies

original_list[0][0] = 99
print("Shallow Copy:", shallow_copy)  # ✅ Changes in original affect the shallow copy
print("Deep Copy:", deep_copy)        # ✅ Deep copy remains unchanged

# 🔗 Weak References (Prevents Garbage Collection Issues)
obj = [10, 20, 30]
weak_ref = weakref.ref(obj)  # Weak reference to obj
print("Weak reference still exists:", weak_ref())

del obj  # Object is now eligible for garbage collection
print("Weak reference after deletion:", weak_ref())  # ✅ None (Object destroyed)

# ✅ Global vs. Local vs. Nonlocal Scope
global_var = "I am global"

def outer_function():
    outer_var = "I am outer"

    def inner_function():
        nonlocal outer_var  # Refers to outer_function's scope
        global global_var   # Refers to the module-level variable
        outer_var = "Modified outer"
        global_var = "Modified global"
        print("Inner Function -> Outer Var:", outer_var)
        print("Inner Function -> Global Var:", global_var)

    inner_function()
    print("Outer Function -> Outer Var:", outer_var)

outer_function()
print("Global Scope -> Global Var:", global_var)

# 🔥 Forcing Garbage Collection
gc.collect()  # ✅ Explicit garbage collection call

