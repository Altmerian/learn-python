from calendar import c


class CurrencyConverter:
    def __init__(self, currency: str, rate: float):
        self.currency = currency
        self.rate = rate

    def get_currency(self):
        return self.currency

    def get_rate(self):
        return self.rate
    
    def set_currency(self, currency: str):
        self.currency = currency

    def set_rate(self, rate: float):
        self.rate = rate

    def convert(self, amount: float):
        return self.currency + " conversion: " + str(amount * self.rate)


if __name__ == "__main__":
    converter = CurrencyConverter("PLN", 4.0)
    print(converter.convert(100))
    
    converter.set_currency("INR")
    converter.set_rate(70.0)
    print(converter.convert(100))
