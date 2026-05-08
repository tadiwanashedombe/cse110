payment = float(input("What is the payment amount? "))

penalty = 0

while payment < 0:

    penalty = 1.50

    print("Sorry payment cannot be a negetive")
    payment = float(input("What is the payment amount? "))



print(f"The payment amount is ${payment:.2f} penaly is ${penalty:.2f}")
