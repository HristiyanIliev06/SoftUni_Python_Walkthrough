def sum_numbers(a, b): return a+b
def subtract(sum, c): return sum-c

def add_and_subtract(a, b, c):
    result = sum_numbers(a, b)
    final_result = subtract(result, c)
    return final_result
    
a=int(input())
b=int(input())
c=int(input())
    
print(add_and_subtract(a, b, c))