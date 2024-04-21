def palindrome(word:str,  zero:int):
    if word[zero]!=word[len(word)-zero-1]:
        return f"{word} is not a palindrome"
    else:
        zero+=1
        palindrome(word, zero)
        if zero==len(word)-zero and word[zero]==word[len(word)-zero]:
            return f"{word} is a palindrome" 
    
print(palindrome("abcba", 1)) #0/100