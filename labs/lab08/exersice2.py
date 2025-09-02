# Input Variables

num_friends = 6
main_dishes = 25
appetizer = 12
drinks = 8
servies_tax = 1.10
delivery_fee = 5

cost_main_dishes = (25 * 3)
cost_appetizer = (12 * 2)
cost_drinks = (8 * 4)

# Calculate The Subtotal
total_dish = (cost_main_dishes + cost_appetizer + cost_drinks)
total = (total_dish * servies_tax ) + delivery_fee 
amount_each_person_pay = total // 6
print(amount_each_person_pay)


