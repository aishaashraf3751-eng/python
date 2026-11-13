snack_name = "chips"
price = 1.50
quantity = 10
is_available = True

print("Snack:", snack_name)
print("price: $", price)
print("In Stock:", quantity)
print("Available?", is_available)

total = price * quantity
print("Total Value : $" , total)
print("Sale Price: $",price - 0.25)
print("Double stock:", quantity * 2)


print("is price under 2$", price < 2)
print("more than 5 in stock?", quantity > 5)
print("is price exactly 1.50$?", price == 1.50)

price_a = 1.50
price_b = 3.00
print("Before:", price_a, "and" , price_b)