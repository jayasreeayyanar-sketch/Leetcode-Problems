class Solution(object):
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0
        n = len(prices)
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
        buy = [float('inf')] * (k + 1)
        sell = [0] * (k + 1)        
        for price in prices:
            for j in range(1, k + 1):
                buy[j] = min(buy[j], price - sell[j-1])
                sell[j] = max(sell[j], price - buy[j])                
        return sell[k]
