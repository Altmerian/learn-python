from time import sleep
from threading import Thread, Condition


class MyData:
    def __init__(self):
        self.data = 0
        self.condition = Condition()
        self.data_available = False

    def update_data(self, value):
        with self.condition:
            self.condition.wait_for(lambda: not self.data_available)
            self.data = value
            self.data_available = True
            self.condition.notify()

    def get_data(self):
        with self.condition:
            self.condition.wait_for(lambda: self.data_available)
            value = self.data
            self.data_available = False
            self.condition.notify()
            return value


class Producer(Thread):
    def __init__(self, my_data):
        super().__init__()
        self.my_data = my_data

    def run(self):
        for i in range(10):
            self.my_data.update_data(i)
            print("Producer updated data:", i)
            sleep(1)


class Consumer(Thread):
    def __init__(self, my_data):
        super().__init__()
        self.my_data = my_data

    def run(self):
        for i in range(10):
            print("Consumer got data:", self.my_data.get_data())
            sleep(1)


if __name__ == "__main__":
    my_data = MyData()
    producer = Producer(my_data)
    consumer = Consumer(my_data)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
