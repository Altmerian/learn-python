from collections import Counter


class Inventory:
    def __init__(self, items: dict[str, int]):
        self.items = items

    def update_inventory(self, order: dict[str, int]) -> None:
        self.items = Counter(self.items) - Counter(order)
    
    def __str__(self) -> str:
        return f"Inventory: {dict(self.items)}"
    
if __name__ == "__main__":
    inventory = Inventory({"apple": 50, "mango": 100, "banana": 120, "orange": 70})
    print(inventory)
    inventory.update_inventory({"apple": 10, "mango": 12, "banana": 15, "orange": 5})
    print(inventory)

