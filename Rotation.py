def rotate(a, n, r):
    for i in range(r):
        last=a[n-1]
        for i in range(n-1,0,-1):
            a[i]=a[i-1]
        a[0]=last
    for i in range(n):
        if (i==n-1):
            print(a[i])
        else:
            print(a[i],end=" ")
for i in range(int(input())):
    n,r=map(int,input().split())
    a=list(map(int,input().split()))
    rotate(a, n,r)
