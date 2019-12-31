
# 146. LRU Cache

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.val = {}
        self.age = {}
        self.current_age = 0
    def get(self, key: int) -> int:
        self.current_age += 1
        if key in self.val.keys():
            self.age[key] = self.current_age
            return self.val[key]
        else: return -1
        
    def put(self, key: int, value: int) -> None:
        
        # check capacity 
        self.current_age += 1
        if key in self.val.keys():
            self.val[key] = value
            self.age[key] = self.current_age
            
        elif len(self.val) < self.capacity: 
            self.val[key] = value
            self.age[key] = self.current_age
        else:
            lru = min(self.age, key=self.age.get)
            del self.val[lru]
            del self.age[lru]
            self.val[key] = value
            self.age[key] = self.current_age