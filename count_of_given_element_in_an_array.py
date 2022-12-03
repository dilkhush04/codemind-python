n=int(input())
c=0
a=list(map(int,input().split()))
key=int(input())
for i in range(n):
    if a[i]==key:
        c=c+1
print(c)