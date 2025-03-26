from collections import deque

class BarberQueue:
    def __init__(self):
        self.queue = deque()

    def walk_in(self, customer: str):
        self.queue.append(customer)

    def service_customer(self) -> str:
        return self.queue.popleft()
    
    def __str__(self) -> str:
        return f"Barbershop queue: {list(self.queue)}"
    
if __name__ == "__main__":
    barber_queue = BarberQueue()
    barber_queue.walk_in("John")
    barber_queue.walk_in("Jane")
    barber_queue.walk_in("Jim")
    print(barber_queue)
    print(barber_queue.service_customer())
    print(barber_queue)
    barber_queue.walk_in("Jill")
    print(barber_queue)
    print(barber_queue.service_customer())
    print(barber_queue)
