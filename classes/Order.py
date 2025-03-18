class Order:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def remove(self, item):
        self.cart.remove(item)

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        return f"Order: total items: {len(self.cart)}, items: {self.cart}"


if __name__ == "__main__":
    order = Order()
    order.add_to_cart("Item 1")
    order.add_to_cart("Item 2")
    order.add_to_cart("Item 3")
    print(order)
    order.remove("Item 2")
    print(order)
