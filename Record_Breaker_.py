t=int(input())
for i in range(1,t+1,1):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    Max=-1
    if n==1:
        ans=1
    else:
        for j in range(n-1):
            if a[j]>Max:
                Max=a[j]
                if a[j]>a[j+1]:
                    ans=ans+1
        if(a[n-1]>Max):
            ans=ans+1
    print('Case #',end='')
    print(i,end='')
    print(':',ans)
       