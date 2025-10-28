
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'quantity': quantity, 'price': price}

    def remove_item(self, name, quantity):
        if name in self.items and self.items[name]['quantity'] >= quantity:
            self.items[name]['quantity'] -= quantity
            if self.items[name]['quantity'] == 0:
                del self.items[name]
        else:
            print("Item not found or insufficient stock")

    def display_inventory(self):
        print("\n--- Current Inventory ---")
        for item, info in self.items.items():
            print(f"{item}: {info['quantity']} units @ ${info['price']} each")


if __name__ == "__main__":
    inv = Inventory()
    inv.add_item("Apple", 50, 0.5)
    inv.add_item("Banana", 30, 0.3)
    inv.remove_item("Apple", 10)
    inv.display_inventory()
