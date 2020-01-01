# ```
# 460. LFU Cache
# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

# Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

 

# Follow up:
# Could you do both operations in O(1) time complexity?

 

# Example:

# LFUCache cache = new LFUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# ```
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frequency = {}
        self.age = {}
        self.items = {}
        self.current_age = 0
        

    def get(self, key: int) -> int:
        self.current_age += 1
        if key in self.items.keys():
            self.age[key] = self.current_age
            self.frequency[key] += 1
            return self.items[key]
        else: return -1
        

    def put(self, key: int, value: int) -> None:
        self.current_age += 1
        if self.capacity == 0:
            return None 
        
        if len(self.items) < self.capacity:
            pass
        elif key in self.items.keys():
            self.items[key] = value
        else: 
            min_value = min(self.frequency.values())
            lfu_keys = [k for k in self.frequency if self.frequency[k] == min_value]
            if len(lfu_keys) == 1:
                del self.items[lfu_keys[0]]
                del self.frequency[lfu_keys[0]]
                del self.age[lfu_keys[0]]
                
            else:
                ages = {x: self.age[x] for x in lfu_keys}
                lru_key = min(ages, key = ages.get)
                del self.items[lru_key]
                del self.frequency[lru_key]
                del self.age[lru_key]
                
        if key in self.items.keys():
            self.frequency[key] += 1
        else: self.frequency[key] = 1
        self.items[key] = value
        self.age[key] = self.current_age  

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)