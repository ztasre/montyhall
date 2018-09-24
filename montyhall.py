#!/bin/env python

import random

class Simulation:

    def __init__(self):

        self.doors = set(range(0, 3))
        self.choice = random.sample(self.doors, 1)[0]
        self.winning = random.sample(self.doors, 1)[0]

    def changeDoor(self):
        """
            Initial choice is made in __init__,

            A door that does not contain the prize
            is opened.

        """

        if self.choice == self.winning:
            return 0
        else:
            return 1

    def keepDoor(self):

        if self.choice == self.winning:
            return 1
        else:
            return 0


if __name__ == "__main__":
    x = 10000
    changed = map(lambda x: x.changeDoor(),
                map(lambda x: Simulation(), range(x)))

    kept = map(lambda x: x.keepDoor(),
            map(lambda x: Simulation(), range(x)))

    print("New door picked: ", sum(changed) / x)
    print("New door not picked: ", sum(kept) / x)
