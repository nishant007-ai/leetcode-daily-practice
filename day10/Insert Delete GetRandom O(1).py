import random

class RandomizedSet:
    def __init__(self):
        self.nums = []

    def insert(self, val):
        if val in self.nums:
            return False
        self.nums.append(val)
        return True

    def remove(self, val):
        if val in self.nums:
            self.nums.remove(val)
            return True
        return False

    def getRandom(self):
        return random.choice(self.nums)
