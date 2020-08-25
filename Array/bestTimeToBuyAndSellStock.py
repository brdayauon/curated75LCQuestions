class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        if len(prices) == 0:
            return 0
        
        minPrice = prices[0]  
        maxProfit = 0
        
        for i in range(0, len(prices)): #iterate through the price list
            if prices[i] < minPrice: #if theres a smaller number later on, then minPrice is set to that
                minPrice = prices[i]  
            elif prices[i] - minPrice  > maxProfit: 
                maxProfit = prices[i] - minPrice 
                #print(minPrice)
                
        return maxProfit