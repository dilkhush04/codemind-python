n=int(input())
a=[]
c=0
d=0
for i in range(n):
    a.append(int(input()))
k=int(input())
for j in range(n):
    if(a[j]<=k):
        c=c+1
    else:
        d=d+2
print(c+d)
    