shopping_list = []

shop = ""

while shop != "quit":
    shop = input("What do you want to add ? ")
    if shop != "quit":
        shopping_list.append(shop)

print("The shopping list is: ")

for list in shopping_list:
    print(list)

print("")

print(" The shopping list with indexex: ")

print("")

for i in range(len(shopping_list)):
    item  = shopping_list[i]
    print(f"{i} . {item} ")

print("")

remove_item = int(input("Which item would you like to change : "))

if remove_item > len(shopping_list):
    print("Invalid index")
else:
    new_item = input("What is the new item : ")
    shopping_list[remove_item] = new_item

print("")

print(" The shopping list with indexex: ")

for i in range(len(shopping_list)):
    item  = shopping_list[i]
    print(f"{i} . {item} ")