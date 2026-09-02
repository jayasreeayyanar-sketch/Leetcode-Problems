from collections import defaultdict, OrderedDict

class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.vals = {}
        self.freqs = defaultdict(OrderedDict)
        self.min_freq = 0
    def _update_frequency(self, key, val=None):
        old_val, freq = self.vals[key]
        new_val = val if val is not None else old_val
        del self.freqs[freq][key]
        if not self.freqs[freq]:
            del self.freqs[freq]            
            if self.min_freq == freq:
                self.min_freq += 1
        self.vals[key] = (new_val, freq + 1)
        self.freqs[freq + 1][key] = True
    def get(self, key):
        if key not in self.vals:
            return -1
        self._update_frequency(key)
        return self.vals[key][0]
    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key in self.vals:
            self._update_frequency(key, value)
        else:
            if len(self.vals) >= self.capacity:
                evict_key, _ = self.freqs[self.min_freq].popitem(last=False)
                del self.vals[evict_key]
            self.vals[key] = (value, 1)
            self.freqs[1][key] = True
            self.min_freq = 1  
