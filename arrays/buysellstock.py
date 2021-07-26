
def maxProfit(prices):
    minprice = prices[0]
    maxprofit = 0

    for i in prices:
        if i < minprice:
            minprice = i
        elif i - minprice > maxprofit:
            maxprofit = i - minprice
    
    return maxprofit

if __name__ == '__main__':
    prices = list(map(int, input().strip().split(" ")))
    print(maxProfit(prices))