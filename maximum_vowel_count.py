s=input()
c=0
temp=-999
s=s.split(" ")
for i in range(len(s)):
    c=0
    for j in range(len(s[i])):
        ch=s[i][j]
        if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U" ):
            c=c+1
    if(c>temp):
        temp=c
print(temp)