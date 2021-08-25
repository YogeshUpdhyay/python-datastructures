def maxProfit(prices):
    maxProf = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            maxProf += prices[i] - prices[i-1]
    return maxProf


print(maxProfit([7,1,5,3,6,4]))