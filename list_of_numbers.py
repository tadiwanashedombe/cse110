numbers = []

number = ""

print("Enter a list of numbers, type 0 when finished")
#adding numbers to the list
while number != "0":
    number = input("Enter Number : ")
    if number != "0":
        
        number = int(number)
        numbers.append(number)

#total for numbers
total = 0
for i in numbers:

    total += i

#average
average = total/len(numbers)

#largest positive number
largest_number = 0

for i in numbers:
    if i > largest_number:
        largest_number = i

#smallest number
small_number = 10000000
for i in numbers:
    if i < small_number:
        small_number = i


print(f"The sum is : {total}")
print(f"The average is : {average}")
print(f"The largest number is : {largest_number}")
print(f"The smallest number is : {small_number}")
