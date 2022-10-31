n=int(input())
a=list(map(int,input().split()))
lst=[]
lst2=[]
for i in range(n):
    for j in range(i+1,n):
        if(a[i]==a[j]):
            lst.append(a[i])
for j in lst:
    if j not in lst2:
        lst2.append(j)
for i in range(len(lst2)):
    print(lst2[i])
            
