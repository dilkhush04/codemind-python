n=int(input())
s=0
e=0
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2==0:
        s=s+a[i]
    else:
        e=e+a[i]
print(abs(s-e))