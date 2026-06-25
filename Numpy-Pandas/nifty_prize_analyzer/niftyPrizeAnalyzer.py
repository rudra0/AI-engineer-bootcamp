import numpy as np

prices = np.array([100, 200, 300, 400, 500])

increasedPrices = prices * 1.02

print("Prices:", prices.min(), prices.max(), prices.mean(), prices.std())
print("Increased Prices:", increasedPrices.min(), increasedPrices.max(), increasedPrices.mean(), increasedPrices.std())

print('Difference between increased and original prices:', increasedPrices - prices)

stockPrices = np.array([
    [250,180,300],
    [255,175,305],
    [260,190,310],
    [258,195,320],
    [270,200,330]
])

print('average stock prices for each day:', stockPrices.mean(axis=1))
print('max stock prices for each day:', stockPrices.max(axis=1))
print('min stock prices for each day:', stockPrices.min(axis=1))
print('stock with highest average price:', stockPrices.mean(axis=0).argmax())