receipts = [2, 4, 9, 5]

running_total = 0

for receipt in receipts:
    #running_total = running_total + receipt
    running_total += receipt

print(f"The total is: {running_total:.2f}")