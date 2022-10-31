n=int(input())
b=[]
k=0
a=list(map(int,input().split()))
for i in range(n):
    if a.count(a[i])==1:
        b.append(a[i])
        k=1
b.sort()
if(k==0):
    print("-1")
else:
    print(b[-1])


    