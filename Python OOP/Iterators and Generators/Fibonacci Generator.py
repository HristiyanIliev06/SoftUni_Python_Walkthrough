def fibonacci():
    current = 1
    sum = 0
    while True:
        previous = current
        yield sum
        current = sum
        sum+=previous
        
generator = fibonacci()
for i in range(5):
    print(next(generator))

        