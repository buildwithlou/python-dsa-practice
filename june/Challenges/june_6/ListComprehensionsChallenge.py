orders = [
    {"id": 1, "item": "Pizza",  "price": 12.99, "status": "delivered"},
    {"id": 2, "item": "Burger", "price": 8.50,  "status": "pending"},
    {"id": 3, "item": "Sushi",  "price": 24.00, "status": "delivered"},
    {"id": 4, "item": "Tacos",  "price": 6.75,  "status": "pending"},
    {"id": 5, "item": "Pasta",  "price": 15.00, "status": "delivered"},
]

# Add a "total" key to every order with price * 1.1 (tax) rounded to 2 decimals

names = [s["item"] for s in orders]
print("Items: ",names)

delivered = [s for s in orders if s["status"] == "delivered"]
print("\nDelivered orders: ")
for s in delivered:
    print(f"{s['item']}: {s['status']}" )

expensive = [s for s in orders if s["price"] > 10]
print("\nExpensive items: (over $10) ")
for s in expensive:
    print(f"{s['item']}: {s['price']}")

totalPrice = [{**s, "total": round(s["price"] * 1.1, 2)} for s in orders]
print("\nOrders with tax: ")
for order in totalPrice:
    print(f"{order['item']}, Final price: ${order['total']}")