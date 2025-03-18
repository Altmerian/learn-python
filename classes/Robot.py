class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Hi, my name is {self.name}")


class PoliceRobot(Robot):
    def say_hi(self):
        print(f"Hi, my name is {self.name} and I am a police robot")


if __name__ == "__main__":
    robot = Robot("R2-D2")
    robot.say_hi()
    police_robot = PoliceRobot("PR-D5")
    police_robot.say_hi()
