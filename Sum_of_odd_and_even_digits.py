n=int(input())
even=0
odd=0
a=list(map(int,input().split()))[:n]
for i in range(n):
    if(i%2==0):
        even+=a[i]
    else:
        odd+=a[i]
if((even-odd)==0):
    print("YES")
else:
    print("NO")