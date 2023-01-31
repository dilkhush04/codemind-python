x=0
for i in range(int(input())):
    s=input()
    for i in range(3):
        if s[i]=='+':
            x=x+1
            break
        elif(s[i]=='-'):
            x=x-1
            break
print(x)
    