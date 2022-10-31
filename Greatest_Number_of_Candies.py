n=int(input())
a=list(map(int,input().split()))[:n]
target=int(input())
temp=-9999
for i in range(n):
    if(temp<a[i]):
        temp=a[i]
for i in range(n):
    if(a[i]+target>=temp):
        print("True",end=' ')
    else:
        print("False",end=' ')