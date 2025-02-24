# Shopping Cart Program
# This program allows the user to add items to a shopping cart, view the cart, remove items, and compute the total cost.
# Extra feature: The program aligns the prices properly for better readability.

# List to store item names and their respective prices
cart_items = []
cart_prices = []

# Function to display the menu
def display_menu():
    print("\nWelcome to the Shopping Cart Program!")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

# Function to add an item to the cart
def add_item():
    item_name = input("What item would you like to add? ")
    while True:
        try:
            item_price = float(input(f"What is the price of '{item_name}'? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid price.")
    
    cart_items.append(item_name)
    cart_prices.append(item_price)
    print(f"'{item_name}' has been added to the cart.")

# Function to display the cart contents
def view_cart():
    if not cart_items:
        print("The shopping cart is empty.")
    else:
        print("\nThe contents of the shopping cart are:")
        for index, (item, price) in enumerate(zip(cart_items, cart_prices), start=1):
            print(f"{index}. {item} - ${price:.2f}")

# Function to remove an item from the cart
def remove_item():
    if not cart_items:
        print("The shopping cart is empty. Nothing to remove.")
        return
    
    view_cart()
    while True:
        try:
            item_number = int(input("Which item would you like to remove? "))
            if 1 <= item_number <= len(cart_items):
                removed_item = cart_items.pop(item_number - 1)
                cart_prices.pop(item_number - 1)
                print(f"'{removed_item}' has been removed from the cart.")
                break
            else:
                print("Invalid item number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to compute the total cost
def compute_total():
    total = sum(cart_prices)
    print(f"The total price of the items in the shopping cart is ${total:.2f}")

# Main program loop
while True:
    display_menu()
    choice = input("Please enter an action: ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        view_cart()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        compute_total()
    elif choice == "5":
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

# Prevent the program from closing immediately
input("\nPress Enter to exit...")
