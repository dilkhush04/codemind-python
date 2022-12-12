s=input()
a=[]
k=0
b=[]
for i in range(len(s)):
    ch=s[i]
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'or ch=='A' or ch=='E'or ch=='I' or ch=='O' or ch=='U' ):
        a.append(ch)
for i in a:
    if i not in b:
        b.append(i)
        k=k+1
if(k==0):
    print("-1")
else:
    for i in b:
        print(i,end=' ')

    