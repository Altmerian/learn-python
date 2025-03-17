class Customer:
    def __init__(self, name: str, phone: int):
        self._name = name
        self.phone = phone

    def get_name(self):
        return self._name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone


if __name__ == "__main__":
    customer1 = Customer("John", 1234567890)
    print("Name:", customer1.get_name())
    print("Phone:", customer1.get_phone())
    customer1.set_phone(9876543210)
    print("Phone:", customer1.get_phone())
