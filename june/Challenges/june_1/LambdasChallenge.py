orders = [
    {"id": 1, "item": "Pizza", "price": 12.99, "delivered": True},
    {"id": 2, "item": "Burger", "price": 8.50, "delivered": False},
    {"id": 3, "item": "Sushi", "price": 24.00, "delivered": True},
    {"id": 4, "item": "Tacos", "price": 6.75, "delivered": False},
]
# filtering only delivered orders
delivered_order = list(filter(lambda order: order["delivered"], orders))
print(delivered_order)
print("*" * 10)

# Add a "total" key to each that is price * 1.1 (tax)
total_price = list(map(lambda order: {**order, "total": order["price"] * 1.1}, 2))
print(total_price)
print("*" * 10)

# Sort the orders by total price in descending order
ranked = sorted(total_price, key=lambda order: order["total"], reverse=True)
print(ranked)

for order in ranked:
    print(f"{order['item']}: ${order['total']}")
