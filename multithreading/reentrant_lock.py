from threading import Thread, RLock, current_thread
from time import sleep

# Create a reentrant lock
rlock = RLock()

class SharedResource:
    def __init__(self):
        self.value = 0
    
    def outer_method(self):
        with rlock:  # First lock acquisition
            print(f"{current_thread().name} acquired lock")
            sleep(0.1)
            self.inner_method()  # Will try to acquire lock again
            
    def inner_method(self):
        with rlock:  # Second lock acquisition (same thread)
            print(f"{current_thread().name} acquired lock")
            self.value += 1
            sleep(0.1)

class Task(Thread):
    def __init__(self, resource):
        super().__init__()
        self.resource = resource
    
    def run(self):
        for _ in range(3):
            self.resource.outer_method()
            sleep(0.1)

if __name__ == "__main__":
    shared_resource = SharedResource()
    
    # Create multiple threads using the same resource
    threads = [Task(shared_resource) for _ in range(3)]
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print(f"Final value: {shared_resource.value}")