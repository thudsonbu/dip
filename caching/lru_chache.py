# LRU cache is a cache data structure that has limited space, and once there are more items in 
# the cache than available space, it will preempt the least recently used item. What counts as 
# recently used is any item a key has 'get' or 'put' called on it.

class Node:
    def __init__(self, key, value, right):
        self.key = key
        self.value = value
        self.right = right

class LRUCache:
    def __init__(self, space):
        self.space = space
        self.stack = None

    def get(self, key):
        get = None

        if(self.stack): # check there is even a stack
            root = self.stack
            prev = None
            
            while root: # search for key

                if root.key == key: # if key found 
                    get = root.value # aquire value

                    if prev: # if not at front move to front
                        prev.right = root.right
                        root.right = self.stack
                        self.stack = root

                prev = root
                root = root.right
        
        return get

    def put(self, key, value):
        root = self.stack
        prev = None
        idx = 1
        
        while root: # search for key

            if root.key == key: # if key found

                if prev: # and its not at the front move it to the front and change its value
                    prev.right = root.right 
                    root.right = self.stack
                    self.stack = root
                    root.value = value

                else: # and its at the front change its value
                    root.value = value
                
                return # item was found and moved if necessary to return

            if idx == self.space: # if its not found by last node cut the last node
                prev.right = None
            
            prev = root
            root = root.right
            idx += 1

        # either there was no stack or item was not found so place at front
        self.stack = Node(key, value, self.stack)

cache = LRUCache(2)

cache.put(3, 3)
cache.put(4, 4)
print(cache.get(3))
# 3
print(cache.get(2))
# None

cache.put(2, 2)

print(cache.get(4))
# None (pre-empted by 2)
print(cache.get(3))
# 3


                




