product = ""
price = 0
quantity = 0
product_and_price = {}
product_and_quanity = {}
result = {}
while True:
    orders = input().split()
    if orders[0]=='buy': break
    
    product = orders[0]
    price = float(orders[1])
    quantity = int(orders[2])
    product_and_price[product] = price
    if product in product_and_quanity.keys():
        update = product_and_quanity[product]+quantity
        product_and_quanity[product] = update
    else: product_and_quanity[product] = quantity
    
for k in product_and_price.keys():
    result[k] = product_and_price[k]*product_and_quanity[k]
    
for (k, v) in result.items():
    print(f"{k} -> {v:.2f}")       