def Array( arr,n):
    for i in range(n):
        L_sum=0
        R_sum=0
        for j in range(0,i,1):
            L_sum=L_sum+arr[j]
        for j in range(i+1,n,1):
            R_sum=R_sum+arr[j]
        if(L_sum==R_sum):
            return True
    return False
t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    if(Array(arr,n)):
        print("YES")
    else:
        print("NO")
    t=t-1