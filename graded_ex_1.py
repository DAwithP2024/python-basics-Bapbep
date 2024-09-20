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
    # Sorts the products based on price in ascending or descending order
    return sorted(products_list, key=lambda x: x[1], reverse=sort_order == 'desc')

def display_products(products_list):
    # Displays each product with its price
    for index, product in enumerate(products_list):
        print(f"{index + 1}. {product[0]} - ${product[1]}")

def display_categories():
    # Displays categories
    for index, category in enumerate(products.keys(), 1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    # Adds product and quantity to the cart
    cart.append((product, quantity))

def display_cart(cart):
    # Displays the cart contents
    total_cost = sum(product[1] * quantity for product, quantity in cart)
    print("Cart contents:")
    for product, quantity in cart:
        print(f"{quantity} x {product[0]} - ${product[1]} each = ${product[1] * quantity}")
    print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    # Generates and displays the receipt
    print(f"Receipt for {name}\nEmail: {email}\n")
    for product, quantity in cart:
        print(f"{quantity} x {product[0]} - ${product[1]} each = ${product[1] * quantity}")
    print(f"Total: ${total_cost}\nDelivery address: {address}\nYour items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    # Validates name format
    return name.replace(" ", "").isalpha() and " " in name

def validate_email(email):
    # Validates email format
    return "@" in email

def main():
    name = input("Please enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name (must contain both first and last name, with alphabets only).")
        name = input("Please enter your name: ")
    
    email = input("Please enter your email address: ")
    while not validate_email(email):
        print("Invalid email address.")
        email = input("Please enter your email address: ")
    
    display_categories()
    while True:
        try:
            category_choice = int(input("Please select a category (number): ")) - 1
            if category_choice < 0 or category_choice >= len(products):
                print("Invalid category selection. Please try again.")
                continue
            category = list(products.keys())[category_choice]
            display_products(products[category])
            
            while True:
                print("\n1. Select a product to buy\n2. Sort the products according to the price.\n3. Go back to the category selection.\n4. Finish shopping")
                choice = input("Please make a choice: ")
                if choice == "1":
                    try:
                        product_index = int(input("Enter the product number (1-8): ")) - 1
                        quantity = int(input("Enter the quantity: "))
                        if product_index < 0 or product_index >= len(products[category]):
                            print("Invalid product selection.")
                            continue
                        add_to_cart(cart, products[category][product_index], quantity)
                    except (ValueError, IndexError):
                        print("Invalid input. Please enter a number.")
                elif choice == "2":
                    sort_order = input("Sort ascending (asc) or descending (desc)? ").lower()
                    sorted_products = display_sorted_products(products[category], sort_order)
                    display_products(sorted_products)
                elif choice == "3":
                    break
                elif choice == "4":
                    if cart:
                        address = input("Please enter your delivery address: ")
                        total_cost = sum(product[1] * quantity for product, quantity in cart)
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid category selection. Please try again.")

if __name__ == "__main__":
    main()
