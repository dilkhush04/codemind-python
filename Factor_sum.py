lst=list(map(int,input().split(",")))
n=len(lst)
a=[]
sum=0
k=0
for i in range(n):
    sum=0
    for j in range(1,lst[i]+1):
        if(lst[i]%j==0):
            sum+=j
    if( sum in lst):
        a.append(lst[i])
        k=k+1
s=sorted(a)
num=len(a)
for i in range(num):
    print(s[i], end=' ')
if(k==0):
    print("-1")