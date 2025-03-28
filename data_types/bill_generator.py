from collections import Counter


class BillGenerator:
    def __init__(self, price_list: dict):
        self.price_list = price_list

    def generate_bill(self, order: dict[str, int]) -> str:
        # Header for the bill
        bill = "BILL\n"
        bill += "=" * 50 + "\n"
        bill += f"{'Product':<20}{'Price':^10}{'Quantity':^10}{'Subtotal':>10}\n"
        bill += "-" * 50 + "\n"

        total = 0.0

        # Add each product to the bill
        for product, quantity in order.items():
            if product in self.price_list:
                price = self.price_list[product]
                subtotal = price * quantity
                total += subtotal

                bill += f"{product:<20}{price:^10.2f}{quantity:^10}{subtotal:>10.2f}\n"
            else:
                bill += f"{product:<20}{'N/A':^10}{quantity:^10}{'N/A':>10}\n"

        # Add the total
        bill += "-" * 50 + "\n"
        bill += f"{'TOTAL':<40}{total:>10.2f}\n"
        bill += "=" * 50 + "\n"

        return bill


if __name__ == "__main__":
    price_list = {"Soap": 10.5, "Shampoo": 20.0, "Conditioner": 30.15, "Lotion": 40.05}
    bill_generator = BillGenerator(price_list)
    order = {"Soap": 2, "Shampoo": 1, "Conditioner": 3, "Lotion": 2}
    print(bill_generator.generate_bill(order))

    # Test with a product not in the price list
    order = {"Soap": 2, "Shampoo": 1, "Conditioner": 3, "Lotion": 2, "Pen": 1}
    print(bill_generator.generate_bill(order))
