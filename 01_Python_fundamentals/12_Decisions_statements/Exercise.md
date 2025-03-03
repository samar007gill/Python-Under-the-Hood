# 📝 Python Decision-Making Exercises

This repository contains a set of **decision-making exercises in Python**, focusing on conditional statements and logical flow control. These exercises are designed to **enhance problem-solving skills** and improve understanding of fundamental **conditional logic**.

---

## 📌 **1. Login System Verification**

**Objective:** Implement a basic login authentication system that verifies user credentials.

### 🔹 **Steps:**
1. Prompt the user to input a **username**.
2. Prompt the user to input a **password**.
3. Validate the entered credentials against predefined values.
4. If both the username and password match, display **"✅ Login successful!"**.
5. If either is incorrect, display **"❌ Invalid credentials!"**.

### 💡 **Example Code:**
```python
# Predefined credentials
correct_username = "admin"
correct_password = "securepass"

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Authentication check
if username == correct_username and password == correct_password:
    print("✅ Login successful!")
else:
    print("❌ Invalid credentials!")
```

---

## 🌡 **2. Temperature Advisor**

**Objective:** Provide **weather-based suggestions** based on the current temperature.

### 🔹 **Steps:**
1. Ask the user to input the **current temperature** (in °C).
2. If the temperature is **above 30°C**, suggest **"Stay hydrated!"**.
3. If the temperature is **between 20°C and 30°C**, suggest **"It's a nice day for a walk!"**.
4. If the temperature is **below 20°C**, suggest **"Wear a jacket!"**.

### 💡 **Example Code:**
```python
temperature = float(input("Enter the current temperature (°C): "))

if temperature > 30:
    print("🔥 Stay hydrated!")
elif 20 <= temperature <= 30:
    print("🌤️ It's a nice day for a walk!")
else:
    print("🧥 Wear a jacket!")
```

---

## 💰 **3. Simple Tax Calculator**

**Objective:** Compute the tax amount based on the user's annual income.

### 🔹 **Steps:**
1. Prompt the user to input their **annual income**.
2. Apply tax rates based on the income brackets:
   - **Below 50,000:** Tax rate **10%**.
   - **Between 50,000 and 100,000:** Tax rate **20%**.
   - **Above 100,000:** Tax rate **30%**.
3. Calculate and display the **total tax amount**.

### 💡 **Example Code:**
```python
income = float(input("Enter your annual income: "))

if income < 50000:
    tax_rate = 0.10
elif income <= 100000:
    tax_rate = 0.20
else:
    tax_rate = 0.30

tax_amount = income * tax_rate
print(f"💵 Your total tax is: ${tax_amount:.2f}")
```

---

## 📅 **4. Day of the Week Checker**

**Objective:** Identify whether the inputted day is a **weekday or a weekend**.

### 🔹 **Steps:**
1. Ask the user to input a **day of the week**.
2. Convert the input to lowercase for **case-insensitive comparison**.
3. If the day is **Saturday or Sunday**, print **"It's a weekend!"**.
4. Otherwise, print **"It's a weekday!"**.

### 💡 **Example Code:**
```python
day = input("Enter a day of the week: ").strip().lower()

if day in ["saturday", "sunday"]:
    print("🎉 It's a weekend!")
else:
    print("📆 It's a weekday!")
```

---

## 🚗 **5. Driving Eligibility Checker**

**Objective:** Determine if a person is **eligible for a driving license** based on their age.

### 🔹 **Steps:**
1. Prompt the user to input their **age**.
2. Apply the following eligibility rules:
   - **Below 16:** "You are too young to get a driving license."
   - **Between 16 and 18:** "You need parental consent to get a driving license."
   - **18 or older:** "You are eligible to get a driving license."

### 💡 **Example Code:**
```python
age = int(input("Enter your age: "))

if age < 16:
    print("🚫 You are too young to get a driving license.")
elif 16 <= age < 18:
    print("📝 You need parental consent to get a driving license.")
else:
    print("✅ You are eligible to get a driving license.")
```

---


