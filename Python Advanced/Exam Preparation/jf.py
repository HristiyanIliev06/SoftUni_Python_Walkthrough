
"""def hunter(whether):
    if whether==True: return 'Yes'
    else: return 'No'
    
if hunter(False)=='Yes':
    print('end')"""
    
def comprehension(detected, earnings):
    if detected=='W': earnings+=100
    if detected=='P': earnings-=200
    if detected=='J': earnings+=100000
    return earnings

board = [['W-GW'], ['W--W'], ['--P-']]
print(comprehension(board[0][0], 100))