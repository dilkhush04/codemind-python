s1=input()
s2=input()
a=[]
b=[]
st='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'
st1=''
s1=s1.lower()
s2=s2.lower()
s1=s1.split(" ")
s2=s2.split(" ")
for i in s1:
    i=list(i)
    for j in i:
        st=st+j
for i in s2:
    i=list(i)
    for j in i:
        st1=st1+j
st=list(st)
st1=list(st1)
for i in st1:
    if i not in st:
        a.append(i)
        
for i in st:
    if i not in st1:
        a.append(i)
a.sort()
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,end='')
        
        