temperature = float(input("What is your temperature in degrees Celsius ? "))

if temperature > 48.5:
    print("Go to the hospital")
elif temperature > 39.4:
    print("Call the doctor")
else:
    print("Consider rest or medicine")

print("Have a good day")
