import re
products = []
total = 0
while True:
    info = input()
    if info=='Purchase': break
    product = re.search(r'[a-zA-Z]+', info)
    products.append(str(product.group(0)))
    price = re.search(r'\b<([0-9\.]+)\b', info)
    quantity = re.search(r'\b!([0-9]+)', info)
    total+=float(price.group(0))*int(quantity.group(0))
    
print("Bought furniture:\n",'\n'.join(products),f"\nTotal money spend: {total:.2f}")