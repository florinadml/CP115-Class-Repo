# FLORINA PIDILIS
#Calculate the ammount of bill to be paid after receving discount

usage = int(input("Enter your monthly usage"))
discount_rate = 0 

# Determine Discount Rate
if usage < 50:
    discount_rate = 0
elif usage <= 100:
    discount_rate = 0.05
else:
    usage > 100
    discount_rate = 0.20

discount_ammount = usage * discount_rate
final_bill = usage - discount_ammount

print (discount_rate)
print(discount_ammount)
print(final_bill)




