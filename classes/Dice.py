import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(f"Rolling the {self.sides} sided dice...", end=" ")
        return random.randint(1, self.sides)


if __name__ == "__main__":
    dice = Dice()
    print(dice.roll_dice())
    print(dice.roll_dice())

    dice2 = Dice(12)
    print(dice2.roll_dice())
    print(dice2.roll_dice())
