print()

print("Please answer the following on a scale of 1 - 10 ")

print()
loan = int(input("How large is your loan ? "))
credit_history = int(input("How good is your credit history ? "))
income = int(input("How high is your income ? "))
down_payment = int(input("How large is your dowb payment ? "))

if loan >= 5:
    if credit_history >= 7 and income >= 7:
        decision = "Yes"
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            decision = "Yes"
        else:
            decision = "No"
    else:
        decision = "No"
else:
    if credit_history < 4:
        decision = "No"
    elif income >= 7 or down_payment >= 7:
        decision = "Yes"
    elif income >= 4 and down_payment >= 4:
        decision = "Yes"
    else:
        decision = "No"

print()
print(f"Decision : {decision}")


#level of confidence