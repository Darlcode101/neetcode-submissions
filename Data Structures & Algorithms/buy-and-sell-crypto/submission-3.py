class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 , 1 
        Profit = 0

        while r < len(prices):
            if prices[l]<prices[r]:
                profitdsa = prices[r] - prices[l]
                Profit = max(Profit, profitdsa)
            else:
                l = r
            r += 1 
        return Profit
