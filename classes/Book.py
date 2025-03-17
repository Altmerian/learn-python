class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        return f"{self.title} by {self.author} - ${self.price}"


if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
    print(book1.show_details())
