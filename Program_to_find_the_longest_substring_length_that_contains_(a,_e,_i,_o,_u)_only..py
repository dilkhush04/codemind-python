s=input()
c=0
temp=-999
for i in range(len(s)):
    if(s[i]=='a' or s[i]=='e' or  s[i]=='o' or  s[i]=='u' or s[i]=='i'):
        c=c+1
        if(temp<c):
            temp=c
    else:
        c=0
print(temp)
    
    