class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        seen = {}        
        s1_count, s2_count = 0, 0
        s2_idx = 0        
        while s1_count < n1:
            s1_count += 1
            for ch in s1:
                if ch == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len(s2):
                        s2_count += 1
                        s2_idx = 0
            if s2_idx in seen:
                prev_s1_count, prev_s2_count = seen[s2_idx]
                cycle_s1_len = s1_count - prev_s1_count
                cycle_s2_count = s2_count - prev_s2_count
                remaining_s1 = n1 - s1_count
                num_cycles = remaining_s1 // cycle_s1_len
                s1_count += num_cycles * cycle_s1_len
                s2_count += num_cycles * cycle_s2_count
                seen.clear()
            else:
                seen[s2_idx] = (s1_count, s2_count)
        return s2_count // n2