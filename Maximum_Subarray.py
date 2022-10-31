n=int(input())
temp=-99999
a=list(map(int,input().split()))[:n]
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=a[j]
        if(temp<sum):
            temp=sum
print(temp)
        
