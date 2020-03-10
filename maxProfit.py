def maxProfit(prices):
    if prices is None or len(prices) == 0:
        return 0
    minSoFar = prices[0]
    maxProfitSoFar = 0
    for i in range(1, len(prices)):
        currentPrice = prices[i]
        currentProfit = currentPrice - minSoFar
        maxProfitSoFar = max(maxProfitSoFar, currentProfit)
        minSoFar = min(minSoFar, currentPrice)
    return maxProfitSoFar
