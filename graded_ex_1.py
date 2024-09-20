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

def display_categories():
    """Display the product categories."""
    print("可用的产品类别：")
    for idx, category in enumerate(products.keys(), start=1):
        print(f"{idx}. {category}")

def display_products(products_list):
    """Display the products in a given category."""
    print("可用的产品：")
    for idx, (product, price) in enumerate(products_list, start=1):
        print(f"{idx}. {product} - ¥{price}")

def display_sorted_products(products_list, sort_order):
    """Sort and display products based on user choice."""
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))
    return sorted_products

def add_to_cart(cart, product, quantity):
    """Add the selected product and quantity to the shopping cart."""
    cart.append((product, quantity))

def display_cart(cart):
    """Display the contents of the shopping cart and total cost."""
    total_cost = 0
    print("购物车内容：")
    for product, quantity in cart:
        # Find the price of the product
        price = next((p[1] for p in products[product.split()[0]] if p[0] == product), 0) 
        total = price * quantity
        total_cost += total
        print(f"{product} - ¥{price} x {quantity} = ¥{total}")
    print(f"总费用: ¥{total_cost}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    """Generate a receipt for the purchase."""
    print("\n--- 收据 ---")
    print(f"姓名: {name}")
    print(f"邮箱: {email}")
    print("购买产品:")
    for product, quantity in cart:
        price = next((p[1] for p in products[product.split()[0]] if p[0] == product), 0) 
        total = price * quantity
        print(f"{quantity} x {product} - ¥{price} = ¥{total}")
    print(f"总费用: ¥{total_cost}")
    print(f"配送地址: {address}")
    print("您的商品将在3天内送达。支付将在送达成功后收取。")

def validate_name(name):
    """Validate the user's name, ensuring it contains both first and last names."""
    names = name.strip().split()
    return len(names) == 2 and all(part.isalpha() for part in names)

def validate_email(email):
    """Validate the email format based on the presence of '@'."""
    return '@' in email

def main():
    cart = []

    # Input user name
    while True:
        name = input("请输入您的姓名（包含名和姓）：")
        if validate_name(name):
            break
        else:
            print("姓名无效，请确保输入名和姓，且只能包含字母。")

    # Input user email
    while True:
        email = input("请输入您的邮箱地址：")
        if validate_email(email):
            break
        else:
            print("邮箱地址无效，请包含 @ 符号。")

    while True:
        # Display product categories
        display_categories()
        
        # Category selection
        while True:
            category_choice = input("请选择要探索的产品类别（输入数字）：")
            if category_choice.isdigit() and 1 <= int(category_choice) <= len(products):
                category_index = int(category_choice) - 1
                selected_category = list(products.keys())[category_index]
                break
            else:
                print("输入无效，请选择正确的数字。")

        while True:
            # Display products in the selected category
            selected_products = products[selected_category]
            display_products(selected_products)

            # User actions
            print("\n请选择操作：")
            print("1. 选择购买产品")
            print("2. 按价格排序产品")
            print("3. 返回类别选择")
            print("4. 完成购物")

            action_choice = input("请输入您的选择（1-4）：")
            if action_choice == '1':
                while True:
                    product_choice = input("请选择要购买的产品（输入产品编号）：")
                    if product_choice.isdigit() and 1 <= int(product_choice) <= len(selected_products):
                        product_index = int(product_choice) - 1
                        selected_product = selected_products[product_index][0]

                        while True:
                            quantity = input(f"请输入要购买的数量：")
                            if quantity.isdigit() and int(quantity) > 0:
                                quantity = int(quantity)
                                add_to_cart(cart, selected_product, quantity)
                                print(f"{selected_product} 已添加到购物车。")
                                break
                            else:
                                print("请输入有效的数量。")
                        break
            elif action_choice == '2':
                sort_order = input("请选择排序方式（1-升序，2-降序）：")
                if sort_order in ['1', '2']:
                    sorted_products = display_sorted_products(selected_products, int(sort_order))
                    display_products(sorted_products)  # Display sorted products
                else:
                    print("无效的选择，返回产品列表。")
            elif action_choice == '3':
                break  # Go back to category selection
            elif action_choice == '4':
                if cart:
                    total_cost = display_cart(cart)
                    address = input("请输入送货地址：")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("感谢使用我们的服务，希望下次您能购买！")
                return
            else:
                print("无效的选择。请重新输入。")

if __name__ == "__main__":
    main()

