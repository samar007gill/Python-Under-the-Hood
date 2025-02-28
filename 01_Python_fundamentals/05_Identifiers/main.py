# ✅ Valid Identifiers
employee_salary = 50000  # Uses snake_case (recommended for variable names)
EmployeeSalary = 60000   # Different from 'employee_salary' due to case sensitivity
_underscore_prefix = "Private variable"  # Single underscore suggests internal use

# ❌ Invalid Identifiers
# 2023_revenue = 1000000  # ❌ Cannot start with a digit
# company-name = "Tech Corp"  # ❌ Hyphens are not allowed
# break = "Reserved Word"  # ❌ Cannot use Python keywords as identifiers

# 🌍 Using Unicode Identifiers (Python 3+ allows non-English characters)
वेतन = 70000  # "वेतन" means "salary" in Hindi
تنخواہ = 75000  # "تنخواہ" means "salary" in Urdu

# 🏦 Calculating total salary across different regions
total_salary = वेतन + تنخواہ
print("Total Salary:", total_salary)  # Output: 145000

# 🎯 Explanation:
# - Identifiers must follow proper naming rules.
# - Unicode characters allow writing identifiers in native languages.
# - Using meaningful variable names improves readability.

