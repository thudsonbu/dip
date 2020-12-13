# LRU cache is a cache data structure that has limited space, and once there are more items in 
# the cache than available space, it will preempt the least recently used item. What counts as 
# recently used is any item a key has 'get' or 'put' called on it.

from collections import OrderedDict

class LRUCache:
  def __init__(self, space):
    self.cache = OrderedDict()
    self.space = space

  def get(self, key):
    if key not in self.cache:
      return None
    val = self.cache[key]
    del self.cache[key]
    self.cache[key] = val

    return val

  def put(self, key, value):
    if key not in self.cache:
      self.cache[key] = value

      if len(self.cache) > self.space:
        self.cache.popitem(last=False)
    else:
      val = self.cache[key]
      del self.cache[key]
      self.cache[key] = val

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
