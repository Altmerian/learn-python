class Computer:
    def __init__(self, name, make, os):
        self.name = name
        self.cpu = self.CPU(make)
        self.os = self.OS(os)

    def show_details(self):
        print(f"Computer: {self.name}, CPU: {self.cpu.get_make()}, OS: {self.os.get_os()}")

    class CPU:
        def __init__(self, make):
            self.make = make

        def get_make(self):
            return self.make

    class OS:
        def __init__(self, os):
            self.os = os

        def get_os(self):
            return self.os


if __name__ == "__main__":
    c = Computer("MacBook", "Apple", "macOS")
    c.show_details()

    c2 = Computer("Dell", "Intel", "Windows")
    c2.show_details()



