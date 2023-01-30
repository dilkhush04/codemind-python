n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    i=abs(i)
    i=str(i)
    if len(i)==k:
        c=c+1
print(c)