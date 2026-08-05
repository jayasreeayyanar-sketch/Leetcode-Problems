class Solution(object):
    def maxEnvelopes(self, envelopes):
        import bisect
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []
        for w, h in envelopes:
            index = bisect.bisect_left(lis, h)
            if index == len(lis):
                lis.append(h)
            else:
                lis[index] = h
        return len(lis)