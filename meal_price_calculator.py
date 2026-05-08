#Added drinks at a discount of 30%
#added a tip calculator

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
drinks_price = float(input("Price of drinks with '30% discount?' "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

subtotal = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults) + (drinks_price * (30/100))

print()  # print a blank line for spacing

print(f"Subtotal: ${subtotal:.2f}")

print()  # print a blank line for spacing

#Tip amout
tip_percentage = float(input("What is the tip percentage? "))
tip_amount = (subtotal * tip_percentage) / 100
print(f"Tip : ${tip_amount:.2f}")

print()  # print a blank line for spacing

#Tax amout
sales_tax = float(input("What is the sales tax rate% ? "))
tax_amount = (subtotal * sales_tax) / 100
print(f"Sales Tax : ${tax_amount:.2f}")


total_price = subtotal + tax_amount + tip_amount

print(f"Total : ${total_price:.2f}")

print()  # print a blank line for spacing

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total_price
print(f"Change : ${change:.2f}")
