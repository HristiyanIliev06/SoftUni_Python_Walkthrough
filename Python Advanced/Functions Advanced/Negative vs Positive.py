def reorganise(*args):
    def definesign():
        total_positives = 0
        total_negatives = 0
        
        for arg in args:
            if arg>0: total_positives+=arg
            else: total_negatives+=arg
        
        print(total_negatives)
        print(total_positives)
            
        if total_positives>abs(total_negatives): return "The positives are stronger than the negatives"
        else: return "The negatives are stronger than the positives"
    return definesign()

sequence = list(map(int, input().split()))
print(reorganise(*sequence))