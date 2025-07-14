import random

class RandomizedSet:
    def __init__(self):
        self.items = []

    def insert(self, val):
        if val in self.items:
            return False
        self.items.append(val)
        return True

    def remove(self, val):
        if val not in self.items:
            return False
        self.items.remove(val)
        return True

    def getRandom(self):
        return self.items[random.randint(0, len(self.items) - 1)]

# Example usage:
rs = RandomizedSet()
print(rs.insert(1))     # True
print(rs.remove(2))     # False
print(rs.insert(2))     # True
print(rs.getRandom())   # 1 or 2
print(rs.remove(1))     # True
print(rs.insert(2))     # False
print(rs.getRandom())   # Always 2
