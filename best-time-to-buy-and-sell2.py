"""
You are given an array prices for which the ith element is the price of a given stock on day i.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:



"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        before looking at answer: pattern i see is we must find the greatest difference in the next few numbers. what i mean by that is we must find a "lower number" and see if we can find the "highest" number that comes after that. we then subtract the lowest from the highest and that is our profit.
        
        
        so how to do that: 
        iterate through the array
        keep track of a lowest number
        and a highest number that comes after that
        subtract the highest from lowest
        if nothing then move on
        if nothing then return 0
        
        
        Reread and understand question completely. very important that we can find Max profit andbuy and sell multiple times, so we are adding to a total.
        
        """
        #f prices == NONE or len(prices) = 0:
            #eturn 0        #edge case always add
            
        if len(prices) == 0: 
            return 0
        
        profit = 0                                              #set profit to 0
        for i in range(len(prices)-1):                          # iterate to go through all (-1 because we are ony comparing ones next to each other)
            if prices[i+1] > prices[i]:                         # if the next day is higher than current day,
                profit += prices[i + 1] - prices[i];            # then we would want to buy and sell next day
                                                                #profit = profit + (nexthighday - ccurrentlowday)
        return profit                                           #after that loop is done, we get profit
    
    
    # [1, 2, 3, 4, 5]
    # for 0index in 4index
    # if 2 > 1
    # profit = 2 -1 = 1
    """
    for 1 index in 4 index
    if 3 > 2
    profit = 1 + 3 - 2 = 2
    
    for 2index in 4 index
    if 4 > 3
    profit = 2 + 4 - 3 = 3
    
    for 3 index in 4 index
    if 5 > 3
    profit = 3 + 5 - 4 = 4
    
    return 4
    """

            
