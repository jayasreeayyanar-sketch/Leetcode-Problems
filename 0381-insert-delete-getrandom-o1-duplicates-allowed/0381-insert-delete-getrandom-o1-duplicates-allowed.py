import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initializes the empty RandomizedCollection object.
        """
        self.nums = []          # List to store the elements
        self.idx_map = {}       # Dictionary mapping values to a set of their indices in self.nums

    def insert(self, val):
        not_present = val not in self.idx_map or not self.idx_map[val]        
        if not_present:
            self.idx_map[val] = set()
        self.idx_map[val].add(len(self.nums))
        self.nums.append(val)        
        return not_present
    def remove(self, val):
        if val not in self.idx_map or not self.idx_map[val]:
            return False
        remove_idx = self.idx_map[val].pop()
        last_idx = len(self.nums) - 1
        last_val = self.nums[last_idx]
        self.nums[remove_idx] = last_val
        self.idx_map[last_val].add(remove_idx)
        self.idx_map[last_val].discard(last_idx)
        self.nums.pop()        
        return True
    def getRandom(self):
        return random.choice(self.nums)
