class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        rounds = minutesToTest // minutesToDie
        states = rounds + 1        
        pigs = 0
        current_buckets_covered = 1        
        while current_buckets_covered < buckets:
            current_buckets_covered *= states
            pigs += 1            
        return pigs
