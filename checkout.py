class Item:
  """
  Represents an item with its individual price and any bulk discounts.
  """
  def __init__(self, individual_price, bulk_quantity=None, bulk_price=None):
    self.individual_price = individual_price
    self.bulk_quantity = bulk_quantity
    self.bulk_price = bulk_price

  def get_individual_price(self):
    return self.individual_price

  def get_bulk_discount(self, quantity):
    if self.bulk_quantity and quantity >= self.bulk_quantity:
      return self.bulk_price - self.individual_price * self.bulk_quantity
    return 0


class Checkout:
  """
  Handles the supermarket checkout process with individual and bulk pricing.
  """
  def __init__(self, pricing_rules):
    self.pricing_rules = {item: Item(**value) for item, value in pricing_rules.items()}
    self.cart = {}

  def scan(self, item):
    """
    Adds an item to the cart or increments its quantity if already present.
    """
    if item in self.cart:
      self.cart[item] += 1
    else:
      self.cart[item] = 1

  def calculate_total(self):
    """
    Calculates the total price of all scanned items based on pricing rules.
    """
    total = 0
    for item, quantity in self.cart.items():
      total += self.calculate_item_price(item, quantity)
    return total

  def calculate_item_price(self, item, quantity):
    if item in self.pricing_rules:
      special_price = self.pricing_rules[item]['special_price']
      regular_price = self.pricing_rules[item]['regular_price']

      if special_price and quantity >= self.pricing_rules[item]['quantity_for_special']:
        discounted_groups = quantity // self.pricing_rules[item]['quantity_for_special']
        remaining_items = quantity % self.pricing_rules[item]['quantity_for_special']
        return discounted_groups * special_price + remaining_items * regular_price
      else:
        return quantity * regular_price
    else:
      return 0
