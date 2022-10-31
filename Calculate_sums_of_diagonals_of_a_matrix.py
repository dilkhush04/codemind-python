n=int(input())
arr=[]
sum1=0
sum2=0
for i in range(n):
    a=list(map(int, input().split()))
    arr.append(a)
for i in range(n):
    for j in range(n):
        if(i==j):
            sum1+=arr[i][j]
        if((i+j)==n-1):
            sum2+=arr[i][j]
print("Principal Diagonal:",end='')
print(sum1)
print("Secondary Diagonal:",end='')
print(sum2)