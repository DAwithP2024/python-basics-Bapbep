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
    else:
        return products_list

def display_products(products_list):
    for index, (product, price) in enumerate(products_list):
        print(f"{index + 1}. {product} - ${price}")

def display_categories():
    for index, category in enumerate(products.keys()):
        print(f"{index + 1}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product, *product[0], quantity))

def display_cart(cart):
    total_cost = 0
    for item in cart:
        product, price, quantity = item
        total_cost += price * quantity
        print(f"{product} - ${price} x {quantity} = ${price * quantity}")
    print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}\nEmail: {email}\nItems Purchased:\n")
    for item in cart:
        product, price, quantity = item
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}\nDelivery Address: {address}\nYour items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def main():
    name = input("Please enter your name: ")
    while not validate_name(name):
        name = input("Invalid name. Please enter your name with first and last name: ")

    email = input("Please enter your email address: ")
    while not validate_email(email):
        email = input("Invalid email. Please enter a valid email address: ")

    while True:
        display_categories()
        category_choice = input("Please enter the category number you would like to explore: ")
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(products):
            category_index = int(category_choice) - 1
            products_list = products[list(products.keys())[category_index]]
            display_products(products_list)

            while True:
                print("\n1. Select a product to buy\n2. Sort the products according to the price.\n3. Go back to the category selection.\n4. Finish shopping")
                action_choice = input("Please enter your choice: ")
                if action_choice == "1":
                    product_choice = input("Please enter the product number you would like to buy: ")
                    if product_choice.isdigit() and 1 <= int(product_choice) <= len(products_list):
                        product_index = int(product_choice) - 1
                        product = products_list[product_index]
                        quantity = int(input("Please enter the quantity you want to buy: "))
                        add_to_cart(cart, product, quantity)
                    else:
                        print("Invalid product selection. Please try again.")
                elif action_choice == "2":
                    print("1. Sort ascending\n2. Sort descending")
                    sort_choice = input("Please enter your choice: ")
                    sorted_products = display_sorted_products(products_list, "asc" if sort_choice == "1" else "desc")
                    display_products(sorted_products)
                elif action_choice == "3":
                    break
                elif action_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

            if cart:
                address = input("Please enter your delivery address: ")
                total_cost = sum(item[1] * item[2] for item in cart)
                generate_receipt(name, email, cart, total_cost, address)
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
            break
        else:
            print("Invalid category selection. Please try again.")

if __name__ == "__main__":
    main()
