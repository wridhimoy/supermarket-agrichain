import unittest
from checkout import Checkout

class TestCheckout(unittest.TestCase):

  def setUp(self):
    # Example pricing rules
    self.pricing_rules = {
      'A': {'regular_price': 50, 'special_price': 130, 'quantity_for_special': 3},
      'B': {'regular_price': 30, 'special_price': 45, 'quantity_for_special': 2},
      'C': {'regular_price': 20, 'special_price': None, 'quantity_for_special': None},
      'D': {'regular_price': 15, 'special_price': None, 'quantity_for_special': None},
    }

  def test_empty_cart(self):
    checkout = Checkout(self.pricing_rules)
    print("Cart:", checkout.cart)
    print("Total:", checkout.calculate_total())
    self.assertEqual(checkout.calculate_total(), 0)

  def test_single_item(self):
    checkout = Checkout(self.pricing_rules)
    checkout.scan("A")
    print("Cart:", checkout.cart)
    print("Total:", checkout.calculate_total())
    self.assertEqual(checkout.calculate_total(), 50)

  # ... (add more test cases from the prompt)

if __name__ == '__main__':
  unittest.main()
