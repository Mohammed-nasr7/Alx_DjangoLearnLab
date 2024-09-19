# استلام الدخل الشهري
monthly_income = int(input("Enter your monthly income: "))
# استلام النفقات الشهرية
monthly_expenses = int(input("Enter your total monthly expenses: "))

# حساب المدخرات الشهرية
monthly_savings = monthly_income - monthly_expenses

# حساب المدخرات المتوقعة بعد سنة مع الفائدة
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# طباعة النتائج
print("Your monthly savings are:", monthly_savings)
print("Projected savings after one year, with interest, is:", projected_savings)
