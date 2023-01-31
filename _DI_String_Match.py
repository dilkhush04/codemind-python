s=input()
i=0
a=[]
n=len(s)
for fun in s:
    if fun=='I':
        a.append(i)
        i=i+1
    else:
        a.append(n)
        n=n-1
a.append(i)
print(*a)
    