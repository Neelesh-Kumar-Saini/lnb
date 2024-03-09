#1
no_of_pizzas = int(input("Enter the no of pizzas bought: "))
no_of_puffs = int(input("Enter the no of puffs bought: "))
no_of_cooldrinks = int(input("Enter the no of cool drinks bought: "))
price_per_pizza = 100
price_per_puff = 20
price_per_cooldrink = 10
total_price = (no_of_pizzas * price_per_pizza) + (no_of_puffs * price_per_puff) + (no_of_cooldrinks * price_per_cooldrink)

print("Bill Details")
print("No of pizzas:", no_of_pizzas)
print("No of puffs:", no_of_puffs)
print("No of cooldrinks:", no_of_cooldrinks)
print("Total price =", total_price)
