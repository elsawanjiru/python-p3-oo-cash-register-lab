class CashRegister:
    def __init__(self, initial_balance=0, discount=0):
        self.balance = initial_balance
        self.discount = discount / 100  # Convert discount to a decimal

        # Initialize an empty list to store items
        self.items = []

    def add_item(self, item_name, price):
        self.items.append({"item_name": item_name, "price": price})

    def calculate_total(self):
        total = sum(item["price"] for item in self.items)
        return total - (total * self.discount)

    def apply_discount(self, discount_percentage):
        self.discount = discount_percentage / 100

    def process_payment(self, amount_paid):
        total_cost = self.calculate_total()
        change = amount_paid - total_cost

        if change >= 0:
            self.balance += total_cost  # Add the total cost to the balance
            self.items = []  # Clear the list of items
            return change
        else:
            return "Insufficient payment"

    def reset(self):
        self.balance = 0
        self.items = []
        self.discount = 0

# Example usage:
cash_register_with_discount = CashRegister(20, 20)  # Create a CashRegister with an initial balance of 20 and a 20% discount
