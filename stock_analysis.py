# stock_analysis.py

# Stock prices for AMC in January 2023
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 
                49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):

    if 1 <= x <= len(stock_prices):
        return stock_prices[x - 1]
    else:
        raise ValueError("Day must be between 1 and 20.")

def max_price(a, b):

    if 1 <= a <= len(stock_prices) and 1 <= b <= len(stock_prices) and a <= b:
        return max(stock_prices[a - 1:b])
    else:
        raise ValueError("Days must be between 1 and 20, and a <= b.")

def min_price(a, b):

    if 1 <= a <= len(stock_prices) and 1 <= b <= len(stock_prices) and a <= b:
        return min(stock_prices[a - 1:b])
    else:
        raise ValueError("Days must be between 1 and 20, and a <= b.")

# Testing the functions
print("Price on day 5:", price_at(5))  # Expected: 34.68
print("Maximum price from day 1 to day 10:", max_price(1, 10))  # Expected: 53.56
print("Minimum price from day 11 to day 20:", min_price(11, 20))  # Expected: 44.21