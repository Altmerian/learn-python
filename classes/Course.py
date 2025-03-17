class Course:
    def __init__(self, name: str, duration: int, *books: str):
        self.name = name
        self.duration = duration
        self.books = [self.Book(book) for book in books]

    def show_details(self):
        print(f"Course: {self.name}, Duration: {self.duration}")
        print("Suggested Books:", ", ".join([str(book) for book in self.books]))


    class Book:
        def __init__(self, title):
            self.title = title

        def __str__(self):
            return self.title


if __name__ == "__main__":
    c = Course("Python", 10, "Book 1", "Book 2", "Book 3")
    c.show_details()

    c2 = Course("Java", 15, "Book 4", "Book 5", "Book 6")
    c2.show_details()


