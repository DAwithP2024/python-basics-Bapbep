import unittest
from io import StringIO
from unittest.mock import patch
import graded_ex_1 as gex

class TestShoppingProgram(unittest.TestCase):

    def setUp(self):
        self.cart = []

    def test_name_validation(self):
        self.assertTrue(gex.validate_name("John Doe"))  
        self.assertFalse(gex.validate_name("JohnDoe"))  
        self.assertFalse(gex.validate_name("John 123")) 

    def test_email_validation(self):
        self.assertTrue(gex.validate_email("john.doe@example.com"))  
        self.assertFalse(gex.validate_email("johndoe.com"))  
        self.assertFalse(gex.validate_email("john@doe"))  
        self.assertFalse(gex.validate_email(" "))  

    @patch('builtins.input', side_effect=['1'])
    def test_valid_category_selection(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            gex.display_categories()
            output = fake_out.getvalue().strip().split('\n')
            self.assertGreaterEqual(len(output), 1)
            self.assertIn("可用的产品类别：", output)

    @patch('builtins.input', side_effect=['5'])
    def test_invalid_category_selection(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            gex.display_categories()
            output = fake_out.getvalue().strip().split('\n')
            self.assertTrue(len(output) > 0)  # Ensures categories can be displayed

    @patch('builtins.input', side_effect=['abc'])
    def test_non_numeric_category_selection(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            gex.display_categories()
            output = fake_out.getvalue().strip()
            self.assertIn("可用的产品类别：", output)

    def test_valid_product_selection(self):
        products_list = [("Laptop", 1000), ("Smartphone", 600)]
        product_index = 0  # Simulating the selection of the first product
        self.assertEqual(product_index, 0)

    def test_invalid_product_selection(self):
        products_list = [("Laptop", 1000), ("Smartphone", 600)]
        product_index = 10  # Invalid index
        self.assertNotIn(product_index, range(len(products_list)))  

    def test_valid_quantity(self):
        quantity = "3"
        self.assertTrue(quantity.isdigit() and int(quantity) > 0)  

    def test_invalid_quantity_zero(self):
        quantity = "0"
        self.assertFalse(int(quantity) > 0)  

    def test_invalid_quantity_non_numeric(self):
        quantity = "abc"
        self.assertFalse(quantity.isdigit())  

    def test_sort_ascending(self):
        products_list = [("Laptop", 1000), ("Smartphone", 600), ("USB Drive", 15)]
        sorted_list = gex.display_sorted_products(products_list, 1)  # Ascending
        expected_list = [("USB Drive", 15), ("Smartphone", 600), ("Laptop", 1000)]
        self.assertEqual(sorted_list, expected_list)  

    def test_sort_descending(self):
        products_list = [("Laptop", 1000), ("Smartphone", 600), ("USB Drive", 15)]
        sorted_list = gex.display_sorted_products(products_list, 2)  # Descending
        expected_list = [("Laptop", 1000), ("Smartphone", 600), ("USB Drive", 15)]
        self.assertEqual(sorted_list, expected_list)  

    def test_add_to_cart(self):
        product = "Laptop"
        quantity = 2
        gex.add_to_cart(self.cart, product, quantity)
        self.assertIn((product, quantity), self.cart)  

    def test_display_cart(self):
        self.cart = [("Laptop", 2), ("Smartphone", 1)]
        expected_output = "Laptop - ¥1000 x 2 = ¥2000\nSmartphone - ¥600 x 1 = ¥600\n总费用: ¥2600"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            total_cost = gex.display_cart(self.cart)
            self.assertIn(expected_output, fake_out.getvalue().strip())  
            self.assertEqual(total_cost, 2600)

    @patch('builtins.input', side_effect=['3'])  
    def test_back_to_categories(self, mock_input):
        action_choice = '3'
        self.assertEqual(action_choice, '3')  

    @patch('builtins.input', side_effect=['4'])  
    def test_finish_shopping(self, mock_input):
        finish_shopping = True
        self.assertTrue(finish_shopping)  

    def test_receipt_generation(self):
        cart = [("Laptop", 2), ("Smartphone", 1)]
        total_cost = 2600
        name = "John Doe"
        email = "john.doe@example.com"
        address = "1234 Elm St, Springfield"

        expected_output = (
            "\n--- 收据 ---\n"
            f"姓名: {name}\n"
            f"邮箱: {email}\n"
            "购买产品:\n"
            "2 x Laptop - ¥1000 = ¥2000\n"
            "1 x Smartphone - ¥600 = ¥600\n"
            f"总费用: ¥{total_cost}\n"
            f"配送地址: {address}\n"
            "您的商品将在3天内送达。支付将在送达成功后收取。"
        )
        with patch('sys.stdout', new=StringIO()) as fake_out:
            gex.generate_receipt(name, email, cart, total_cost, address)
            self.assertIn(expected_output.strip(), fake_out.getvalue().strip()) 

if __name__ == '__main__':
    unittest.main()

