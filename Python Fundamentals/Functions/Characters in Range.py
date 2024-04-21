def ascii_table(A, B):
    symbols =[]
    for symbol in range(ord(A)+1, ord(B)):
        symbols.append(chr(symbol))
    return ' '.join(symbols)

A = input()
B = input()
print(ascii_table(A, B))