#Added and if statement check if list is empty and lets the user know the list empty
#Added an else statent that exits loop is user enters invalid action

shopping_list = []
prices = []


menu = (
"""
Please select one of the following :
1. Add item 
2. View cart
3. Remove item
4. Compute total
5. Quit
""")

print("Welcome to the Shoppping cart Program!")

action = ""

while action != "5":
    print(menu)

    action = input("Please enter an action : ")

    #adding items
    if action == "1":
            
            #items to add
            shop = input("What do you want to add ? ")        
            price = float(input(f"What is the price of '{shop}'? "))

            #add items to list
            shopping_list.append(shop)
            prices.append(price)

            print(f"'{shop}' has been added to cart ")

    #viewing cart
    elif action == "2":

        #check if list is empty
        if len(shopping_list) == 0:
            print("The cart is empty, Add contents to view cart")
        else:
            #display list
            print("The contents of the shopping cart are : ")

            i = 1
            for index in range(len(shopping_list)) :
                
                print(f"{i}. {shopping_list[index]} - ${prices[index]:.2f}" )

                #add 1 to the counter
                i += 1
          
    #Removing items
    elif action == "3":

        #1st display list
        print("The contents of the shopping cart are : ")

        #initialize normal counter
        i = 1

        for index in range(len(shopping_list)) :
            
            print(f"{i}. {shopping_list[index]} - ${prices[index]:.2f}" )

            #increment normal counter
            i += 1
        print("")

        #Selecting index to remove
        remove_items = int(input("Which item would you like to remove : "))
        
        #Verifying index position
        if remove_items <= len(shopping_list) and remove_items >= 0 :
            #converting user input to match list index
            remove_items -= 1
            
            #Remove item
            remove_item = shopping_list.pop(remove_items)
            
            #Remove price
            remove_price = prices.pop(remove_items)
        else:
            print("Sorry, that is not a valid item number.")             

        print("Item removed.")
    #Calculation total
    elif action == "4":

        total_price = 0
        for i in prices:
            total_price += i
        
        #displaying total price
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}")

    #quit
    elif action == "5":
            print("Thank you. Goodbye")
    else:
        print("Invalid action")
        action = "5"