def best_price_to_buy_stock(N, changes):
    min_price = 0
    sum = 0
    
    for change in changes:
        sum += change
        min_price = min(min_price, sum)
    
    return min_price

N = 5
changes = [-39957, -17136, 35466, 21820, -26711]
print(best_price_to_buy_stock(N, changes))
