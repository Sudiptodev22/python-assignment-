# Problem 2: Simple Shopping Cart

# 1. Customer name input
customer_name = input("Customer Name: ")

# 2. 3 ta product er name and price input
product1_name = input("Product 1 Name: ")
product1_price = float(input(f"Price of {product1_name}: "))

product2_name = input("Product 2 Name: ")
product2_price = float(input(f"Price of {product2_name}: "))

product3_name = input("Product 3 Name: ")
product3_price = float(input(f"Price of {product3_name}: "))

# 3. Subtotal calculate
subtotal = product1_price + product2_price + product3_price

# 4. Discount determine
if subtotal >= 5000:
    discount_percent = 20
elif subtotal >= 3000:
    discount_percent = 10
elif subtotal >= 1000:
    discount_percent = 5
else:
    discount_percent = 0

discount_amount = subtotal * (discount_percent / 100)
final_total = subtotal - discount_amount

# 5. f-string diye summary display
print("\n--- Shopping Summary ---")
print(f"Customer Name: {customer_name}\n")

print(f"Product 1: {product1_name}")
print(f"Price: {product1_price}\n")

print(f"Product 2: {product2_name}")
print(f"Price: {product2_price}\n")

print(f"Product 3: {product3_name}")
print(f"Price: {product3_price}\n")

print(f"Subtotal: {subtotal}")
print(f"Discount: {discount_percent}% ({discount_amount})")
print(f"Final Total: {final_total}")
