employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
tax_rate = 0

overtime_pay = 35 * overtime_hours
total_income = overtime_pay * base_salary

if tax_status == "Single" and base_salary >= 5000 :
    tax_rate = 0.22
elif tax_status == "Single" and base_salary <= 5000 :
    tax_rate == 0.18
elif tax_status == "Married" and base_salary >= 6000 :
    tax_rate == 0.20
elif tax_status == "Married" and base_salary <= 6000 :
    tax_rate == 0.15
elif tax_status == "Head" and base_salary >= 5500 :
    tax_rate == 0.25
 else:
     tax_rate == 0.19
else:
    tax_rate == 0

after_tax = base_salary -  (base_salary * tax_rate)

epf = base_salary * 0.11
sosco = base_salary * 0.005

net_salary = after_tax - (epf + sosco)

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")