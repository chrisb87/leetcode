class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.use_counter = {}


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache[key]['uses'] += 1
        value = self.cache[key]['value']
        self._set_use_counter(key, self.cache[key]['uses'])
        return value
    
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                least_used = next(iter(self.use_counter))
                to_evict = self.use_counter[least_used].pop()
                if len(self.use_counter[least_used]) == 0:
                    del self.use_counter[least_used]
                del self.cache[to_evict]

            self.cache[key] = {'value': value, 'uses': 1}
            if 1 not in self.use_counter:
                self.use_counter[1] = []
            self.use_counter[1].append(key)

        else:
            self.cache[key]['value'] = value
            self.cache[key]['uses'] += 1
            self._set_use_counter(key, self.cache[key]['uses'])

    def _set_use_counter(self, key: int, newvalue: int) -> None:
        oldvalue = newvalue - 1
        self.use_counter[oldvalue].remove(key)
        if len(self.use_counter[oldvalue]) == 0:
            del self.use_counter[oldvalue]
        if newvalue not in self.use_counter:
            self.use_counter[newvalue] = []
        self.use_counter[newvalue].insert(0, key)



def test_lfu_cache():
    cache = LFUCache(3)
    cache.put(2,2)
    cache.put(1,1)
    assert cache.get(2) == 2
    assert cache.get(1) == 1
    assert cache.get(2) == 2
    cache.put(3,3)
    cache.put(4,4)
    import pdb; pdb.set_trace()
    assert cache.get(3) == -1
    assert cache.get(2) == 2
    assert cache.get(1) == 1
    assert cache.get(4) == 2
    
    
#import pdb
#pdb.set_trace()
