n=int(input())
temp=9999
a=list(map(int,input().split()))
for i in range(n):
    if temp>a[i]:
        temp=a[i]
print(temp)