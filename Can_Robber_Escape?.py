n=int(input())
a=list(map(int, input().split()))[:n]
c=0
for i in a:
    if(i%2==1):
        c=c+1
if c<=2:
    print("YES")
else:
    print("NO")