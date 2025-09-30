position = input()
overtime_hours = int(input())
is_weekend = input()
hourly_rate = 0
overtime_pay = 0
# Determine base hours rate
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
else:
    position == "Staff"
    hourly_rate = 18

<<<<<<< HEAD
if is_weekend == "Yes":
    overtime_pay = (1.5 * hourly_rate  * overtime_hours ) + (overtime_hours * 5 )
else:
    overtime_pay = (1.5 * hourly_rate  * overtime_hours )

total_pay = overtime_pay 
=======
# Define base hourly rates
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18

# Calculate overtime pay (1.5x base rate)
overtime_rate = hourly_rate * 1.5
overtime_pay = overtime_hours * overtime_rate

# Add weekend bonus if applicable
if is_weekend.lower() == "yes":
    weekend_bonus = overtime_hours * 6
    overtime_pay += weekend_bonus

# Total pay is same as overtime pay
total_pay = overtime_pay
>>>>>>> 4e634848592fa0576f50e2fd0b00bb211ae47dad

print(hourly_rate)
print(overtime_pay)
print(total_pay)