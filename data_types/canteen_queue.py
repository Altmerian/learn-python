from collections import deque
from re import L

class CanteenQueue:
    def __init__(self, students: list[str]):
        self.queue = deque(students)

    def serve_student(self):
        print(f"Students are served in order: {self.queue}")
        self.queue.rotate(-1)
    
    def __str__(self) -> str:
        return f"Canteen queue: {list(self.queue)}"
    
if __name__ == "__main__":
    students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    canteen_queue = CanteenQueue(students)
    print("Breakfast time!")
    canteen_queue.serve_student()
    print("Lunch time!")
    canteen_queue.serve_student()
    print("Dinner time!")
    canteen_queue.serve_student()

