deck = input().split()
shuffles = int(input())
for shuffle in range(shuffles):
    mid = len(deck)//2
    left = deck[:mid]
    right = deck[mid:]
    shuffled_deck=[]
    for index in range(len(left)):
        shuffled_deck.append(left[index])
        shuffled_deck.append(right[index])
    deck = shuffled_deck
print(deck)
