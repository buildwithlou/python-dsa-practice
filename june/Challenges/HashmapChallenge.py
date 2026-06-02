transactions = [
    {"user": "Carlos", "amount": 120},
    {"user": "Maria",  "amount": 80},
    {"user": "Carlos", "amount": 200},
    {"user": "Ana",    "amount": 150},
    {"user": "Maria",  "amount": 60},
    {"user": "Carlos", "amount": 50},
]

count = {} #empty dictionary to store the total amount spent by each user

for transaction in transactions:
    user = transaction["user"] #get the user from the transaction
    amount = transaction["amount"] #get the amount from the transaction
    if user in count:
        count[user] = count[user] + amount #if we have already seen this user, we add the amount to their total
    else:
        count[user] = amount #if we haven't seen this user before, we add them to the dictionary with their amount

print(count)