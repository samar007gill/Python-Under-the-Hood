---

# 🔧 Advanced Python Conditional Statements – Solutions  
---
This section provides **well-structured solutions** to the exercises, demonstrating **real-world applications** of Python’s `if`, `if-else`, and `if-elif` conditional statements. Each solution is **optimized for readability, maintainability, and efficiency**.  

---

## ✅ 1. Login System Verification  

### **🔹 Objective:**  
Develop a **secure authentication mechanism** that verifies user credentials against predefined values.  

### **📌 Implementation:**  
```python
# Predefined credentials (Can be stored securely in a database)
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"

# User input for authentication
username = input("🔐 Enter your username: ")
password = input("🔑 Enter your password: ")

# Validation of credentials
if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
    print("\n✨ Access Granted! Welcome back! ✨")
    print(f"👤 User: {username}")
    print("📂 You now have access to all system features.")
else:
    print("\n❌ Authentication Failed! Invalid credentials. Please try again.")
```
### **📢 Explanation:**  
- The script prompts the user to enter a **username** and **password**.  
- It then verifies the input **against predefined credentials**.  
- If they match, access is granted; otherwise, an error message is displayed.  

---

## 🌡️ 2. Temperature-Based Advisory System  

### **🔹 Objective:**  
Implement a **dynamic temperature advisory system** that suggests appropriate actions based on the input temperature.  

### **📌 Implementation:**  
```python
# User input for temperature (Ensuring valid numerical input)
temperature = float(input("🌡️ Enter the current temperature in °C: "))

# Conditional decision-making for temperature advisories
if temperature > 30:
    print("🔥 It's extremely hot! Stay hydrated and avoid direct sunlight. 💧")
elif 20 <= temperature <= 30:
    print("🌤️ The weather is pleasant! A great time for an outdoor walk. 🚶‍♂️")
else:
    print("❄️ It's quite chilly! Consider wearing warm clothes. 🧥")
```
### **📢 Explanation:**  
- The program **takes a temperature input** and converts it into a numerical value.  
- Based on predefined ranges, it advises the user on **weather-appropriate actions**.  

---

## 💰 3. Advanced Tax Calculator  

### **🔹 Objective:**  
Develop a tax calculation system that computes **progressive tax rates** based on annual income.  

### **📌 Implementation:**  
```python
# User input for annual income
income = float(input("💵 Enter your annual income: "))

# Tax computation based on income brackets
if income < 50000:
    tax_rate = 0.10
elif 50000 <= income <= 100000:
    tax_rate = 0.20
else:
    tax_rate = 0.30

# Calculating the tax amount
tax_amount = income * tax_rate
print(f"📊 Tax Rate: {tax_rate*100}%")
print(f"💸 Total Tax Payable: ${tax_amount:.2f}")
```
### **📢 Explanation:**  
- The program applies **progressive tax rates** based on the user's income.  
- It calculates and displays the **effective tax rate and total tax payable**.  

---

## 📅 4. Day of the Week Classifier  

### **🔹 Objective:**  
Build a **weekday-weekend classifier** that determines whether a given day is a **weekday** or a **weekend**.  

### **📌 Implementation:**  
```python
# User input for the day of the week (Converting input to title case for consistency)
day = input("📅 Enter a day of the week: ").strip().capitalize()

# Conditional check for weekdays and weekends
if day in ["Saturday", "Sunday"]:
    print("🎉 It's a weekend! Time to relax and unwind.")
elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("💼 It's a weekday. Stay productive and focused!")
else:
    print("⚠️ Invalid input. Please enter a valid day of the week.")
```
### **📢 Explanation:**  
- The script **normalizes the input** (capitalizing the first letter for uniformity).  
- It **classifies the day** into a **weekend** or **weekday** using a list-based lookup.  

---

## 🚗 5. Driving License Eligibility Checker  

### **🔹 Objective:**  
Develop an eligibility checker that determines if a user **qualifies for a driving license** based on their age.  

### **📌 Implementation:**  
```python
# User input for age
age = int(input("🚦 Enter your age: "))

# Conditional evaluation for driving eligibility
if age < 16:
    print("🚫 You are too young to apply for a driving license.")
elif 16 <= age < 18:
    print("📝 You need parental consent to obtain a driving license.")
else:
    print("✅ You meet the age requirement for a driving license!")
```
### **📢 Explanation:**  
- The program uses **age-based conditions** to determine **eligibility status**.  
- It ensures that users receive **accurate guidance** on legal driving age requirements.  

---
