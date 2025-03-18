from threading import Thread
from queue import Queue
from time import sleep


class Producer(Thread):
    def __init__(self, data_queue: Queue):
        super().__init__()
        self.queue = data_queue

    def run(self):
        for i in range(10):
            self.queue.put(i)
            print("Producer updated data:", i)
            sleep(1)


class Consumer(Thread):
    def __init__(self, data_queue: Queue):
        super().__init__()
        self.queue = data_queue

    def run(self):
        for i in range(10):
            value = self.queue.get()
            print("Consumer got data:", value)
            self.queue.task_done()  # Signal that the task is complete
            sleep(1)


if __name__ == "__main__":
    data_queue = Queue()
    producer = Producer(data_queue)
    consumer = Consumer(data_queue)
    
    producer.start()
    consumer.start()
    
    producer.join()
    consumer.join()
