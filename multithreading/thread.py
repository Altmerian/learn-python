from threading import Thread
from time import sleep


def runnable():
    for i in range(65, 91):
        print(chr(i))
        sleep(0.1)


class Task(Thread):
    def run(self):
        for i in range(97, 123):
            print(chr(i))
            sleep(0.1)


if __name__ == "__main__":
    thread = Thread(target=runnable)
    thread.start()

    task_thread = Task()
    task_thread.start()

    thread.join()
    task_thread.join()
