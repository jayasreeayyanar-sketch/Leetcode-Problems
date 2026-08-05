class SummaryRanges(object):

    def __init__(self):
        self.intervals = []

    def addNum(self, value):
        intervals = self.intervals
        new_interval = [value, value]
        result = []
        placed = False
        for start, end in intervals:
            if end + 1 < new_interval[0]:
                result.append([start, end])
            elif new_interval[1] + 1 < start:
                if not placed:
                    result.append(new_interval)
                    placed = True
                result.append([start, end])
            else:
                new_interval[0] = min(new_interval[0], start)
                new_interval[1] = max(new_interval[1], end)
        if not placed:
            result.append(new_interval)
        self.intervals = result
    def getIntervals(self):
        return self.intervals