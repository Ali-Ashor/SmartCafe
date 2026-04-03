# =========================
# MenuItem Class
# =========================
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} - ${self.price}")

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


# =========================
# Order Class
# =========================
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.get_name() != name]

    def display_order(self):
        if not self.items:
            print("No items in order.")
            return
        for item in self.items:
            item.display()

    def calculate_total(self):
        total = sum(item.get_price() for item in self.items)
        return total


# =========================
# Customer Class
# =========================
class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def add_order_item(self, item):
        self.order.add_item(item)

    def remove_order_item(self, name):
        self.order.remove_item(name)

    def display_order(self):
        print(f"\nOrder for {self.name}:")
        self.order.display_order()

    def checkout(self):
        total = self.order.calculate_total()
        print(f"Total: ${total}")


# =========================
# Main Program
# =========================
def main():
    # Create Menu Items
    coffee = MenuItem("Coffee", 3.50)
    sandwich = MenuItem("Sandwich", 5.00)
    burger = MenuItem("Burger", 7.00)

    # Create Customer
    customer = Customer("Ali")

    # Add Items
    customer.add_order_item(coffee)
    customer.add_order_item(sandwich)
    customer.add_order_item(burger)

    # Display Order
    customer.display_order()

    # Remove Item (optional test)
    customer.remove_order_item("Sandwich")

    print("\nAfter removing Sandwich:")
    customer.display_order()

    # Checkout
    customer.checkout()


# Run Program
if __name__ == "__main__":
    main()