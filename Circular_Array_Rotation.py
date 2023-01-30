n,r,quary=map(int,input().split())
a=list(map(int,input().split()))
for i in range(r):
    last=a[n-1]
    for i in range(n-1,0,-1):
        a[i]=a[i-1]
    a[0]=last
for i in range(quary):
    index=int(input())
    print(a[index])