def Weird(arr,n):
    c=0
    for i in range(n):
        if(arr[i]%2!=0):
            c=c+1
    return int(c/2)
T=int(input())
while(T>0):
    n=int(input())
    arr=list(map(int,input().split()))
    print(Weird(arr,n))
    T=T-1
    