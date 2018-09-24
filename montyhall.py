#!/bin/env python

import random

class Simulation:

    def __init__(self, options=3):

        self.doors = set(range(0, options))
        self.choice = random.sample(self.doors, 1)[0]
        self.winning = random.sample(self.doors, 1)[0]

    def changeDoor(self):
       
        self.options = set(self.doors)
        if self.choice == self.winning:
            self.options.remove(self.choice)
        else:
            self.options.remove(self.winning)
            self.options.remove(self.choice)

        self.options.remove(random.sample(self.options, 1)[0])
        self.options.add(self.winning)

        self.choice = random.sample(self.options, 1)[0]

        if self.choice == self.winning:
            return 1
        else:
            return 0

    def keepDoor(self):

        if self.choice == self.winning:
            return 1
        else:
            return 0


if __name__ == "__main__":
    changed = map(lambda x: x.changeDoor(),
                map(lambda x: Simulation(), range(10000)))

    kept = map(lambda x: x.keepDoor(),
            map(lambda x: Simulation(), range(10000)))

    print("New door picked: ", sum(changed) / 10000)
    print("New door not picked: ", sum(kept) / 10000)
