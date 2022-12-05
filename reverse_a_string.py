s=input()
s=s.split(" ")
for i in range(len(s)-1,-1,-1):
    for j in range(len(s[i])-1,-1,-1):
        print(s[i][j],end="")
    print(end=" ")