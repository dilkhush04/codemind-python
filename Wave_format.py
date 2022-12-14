def swap(arr, a , b ):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
def method(arr ,n):
    for i in range(0,n-1,2):
        swap(arr , i , i+1)
    for i in range(n):
        print(arr[i],end=' ')
n=int(input())
arr1=list(map(int,input().split()))
arr1.sort()
arr=[]
for i in range(n):
    arr.append(arr1[n-i-1])
method(arr,n)