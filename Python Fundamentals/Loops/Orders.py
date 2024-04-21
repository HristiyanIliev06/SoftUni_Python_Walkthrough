num = int(input())
total_price = 0
for i in range(num):
    ppc = float(input())
    if 0.01>ppc or ppc>100.00: continue
    days = int(input())
    if 1>days or days>31: continue
    cpd = int(input())
    if 1>cpd or cpd>2000: continue
    price = ppc*days*cpd
    print(f'The price for the coffee is: ${price:.2f}')
    total_price+=price

print(f"Total: ${total_price:.2f}")