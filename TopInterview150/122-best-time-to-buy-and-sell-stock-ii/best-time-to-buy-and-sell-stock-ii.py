class Solution(object):
    def maxProfit(self, prices):
        leng=len(prices)
        sum = 0
        for i in range(len(prices)):
            if i < leng-1 and prices[i]<prices[i+1]:
                sum += (prices[i+1]-prices[i])
        return sum
        