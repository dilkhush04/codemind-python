m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    s=0
    for j in range(i,n+1):
        s=s+j
        if(s%2!=0):
            c=c+1
print(c)
        