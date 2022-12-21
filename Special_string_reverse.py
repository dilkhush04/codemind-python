def letters(S):
    S = list(S)
    left, right = 0, len(S)-1
    while left < right:
        while not S[left].isalpha() and left < right:
            left += 1
        while not S[right].isalpha() and left < right:
            right -= 1
        if left < right:
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1    
    return ''.join(S)
s=input()
print(letters(s))