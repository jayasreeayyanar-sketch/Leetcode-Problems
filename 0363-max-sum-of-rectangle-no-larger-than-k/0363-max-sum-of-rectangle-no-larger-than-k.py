class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        import bisect
        rows = len(matrix)
        cols = len(matrix[0])
        result = float('-inf')
        if rows > cols:
            matrix = list(map(list, zip(*matrix)))
            rows, cols = cols, rows
        for top in range(rows):
            sums = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    sums[col] += matrix[bottom][col]
                prefix = [0]
                current = 0
                for num in sums:
                    current += num
                    index = bisect.bisect_left(prefix, current - k)

                    if index < len(prefix):
                        result = max(result, current - prefix[index])
                    bisect.insort(prefix, current)
                    if result == k:
                        return k
        return result