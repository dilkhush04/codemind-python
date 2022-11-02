s=input()
temp=-999
for i in range(len(s)):
    c=0
    for j in range(i,len(s)):
        if(s[i]==s[j]):
            c=c+1
            if(temp<c):
                temp=c
        else:
            c=0
print(temp)
            