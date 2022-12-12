s=input() 

a=[]
k=0
c=['A','E','I','O','U']
b=['a','e','i','o','u']
for i in range(len(s)):
    ch=s[i]
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'or ch=='A' or ch=='E'or ch=='I' or ch=='O' or ch=='U' ):
        a.append(ch)
for i in a:
    if i in b:
        b.remove(i)
    if i in c:
        c.remove(i)
if(len(b)==0 or len(c)==0):
    print("True")
else:
    print("False")