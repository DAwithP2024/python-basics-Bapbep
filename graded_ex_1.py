# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)

def display_products(products_list):
    for index, (product, price) in enumerate(products_list):
        print(f"{index + 1}. {product} - ${price}")

def display_categories():
    for index, category in enumerate(products.keys()):
        print(f"{index + 1}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

def display_cart(cart):
    total_cost = 0
    for product, quantity in cart:
        total_cost += product[1] * quantity
        print(f"{product[0]} - ${product[1]} x {quantity} = ${product[1] * quantity}")
    print(f"Total cost: ${total_cost}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}\nEmail: {email}\nItems Purchased:\n")
    for product, quantity in cart:
        print(f"{quantity} x {product[0]} - ${product[1]} = ${product[1] * quantity}")
    print(f"Total: ${total_cost}\nDelivery Address: {address}\nYour items will be delivered in 3 days.\nPayment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def main():
    name = input("Please enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter your name with first and last name, containing only alphabets.")
        name = input("Please enter your name: ")

    email = input("Please enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please include an '@' sign in your email address.")
        email = input("Please enter your email address: ")

    cart = []
    while True:
        display_categories()
        try:
            category_choice = int(input("Please enter the category number you would like to explore: ")) - 1
            if category_choice in range(len(products)):
                category = list(products.keys())[category_choice]
                display_products(products[category])
                while True:
                    print("\n1. Select a product to buy\n2. Sort the products according to the price.\n3. Go back to the category selection.\n4. Finish shopping")
                    action = input("Please enter your choice: ")
                    if action == "1":
                        product_choice = int(input("Please enter the product number you would like to buy: ")) - 1
                        if product_choice in range(len(products[category])):
                            product = products[category][product_choice]
                            quantity = int(input(f"Enter the quantity for {product[0]}: "))
                            add_to_cart(cart, product, quantity)
                        else:
                            print("Invalid product selection. Please try again.")
                    elif action == "2":
                        sort_order = input("Sort ascending (1) or descending (2)? ")
                        sorted_products = display_sorted_products(products[category], "asc" if sort_order == "1" else "desc")
                        display_products(sorted_products)
                    elif action == "3":
                        break
                    elif action == "4":
                        if cart:
                            address = input("Please enter your delivery address: ")
                            total_cost = display_cart(cart)
                            generate_receipt(name, email, cart, total_cost, address)
                        else:
                            print("Your cart is empty. Thank you for browsing.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid category selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

        continue_shopping = input("Would you like to continue shopping? (yes/no): ")
        if continue_shopping.lower() != 'yes':
            print("Thank you for shopping with us. Have a nice day!")
            break

if __name__ == "__main__":
    main()
