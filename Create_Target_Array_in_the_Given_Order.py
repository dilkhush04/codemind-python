m=int(input())
a=list(map(int,input().split()))[:m]
n=int(input())
b=list(map(int,input().split()))[:n]
arr=[]

for i in range(n):
    arr.insert(b[i],a[i])
for i in range(len(arr)):
    print(arr[i],end=" ")
    