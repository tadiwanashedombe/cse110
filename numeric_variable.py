age = int(input("Enter your age : "))
print("On your next birthday, you will be " + str(age + 1))
print()

eggs = int(input("Enter the number of egg cartons you have : "))
print("You have " + str(eggs * 12) + " eggs.")
print()

cookies = int(input("Enter the number of cookies : "))
people = int(input("Enter the number of people : "))

cookies_per_person = float(cookies / people)

print("Each person may have " + str(cookies_per_person) + " cookies.")
