class Checkout:
    def __init__(self, pricing_rules):
        self.cart = {}
        self.pricing_rules = pricing_rules

    def scan(self, item):
        if item not in self.cart:
            self.cart[item] = 1
        else:
            self.cart[item] += 1

    def calculate_total(self):
        total_price = 0

        for item, quantity in self.cart.items():
            if item in self.pricing_rules:
                total_price += self.apply_discount(item, quantity)
            else:
                total_price += quantity * self.pricing_rules.get(item, 0)

        return total_price

    def apply_discount(self, item, quantity):
        rule_quantity, rule_price = self.pricing_rules[item]
        discounted_groups = quantity // rule_quantity
        remaining_items = quantity % rule_quantity
        return discounted_groups * rule_price + remaining_items * self.pricing_rules[item]


# Example Pricing Rules
pricing_rules = {
    'A': (3, 130),
    'B': (2, 45),
    'C': 20,
    'D': 15,
}

# Example Usage
checkout = Checkout(pricing_rules)

# Scanning items
checkout.scan("A")
checkout.scan("B")
checkout.scan("A")
checkout.scan("C")
checkout.scan("D")

# Calculating total price
total_price = checkout.calculate_total()
print(f"Total Price: {total_price}")
