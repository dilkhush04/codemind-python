s=input()
c=0
s=s.split(" ")
for i in range(len(s)):
    for j in range(len(s[i])):
        ch=s[i][j]
        c=c+1
print(c)