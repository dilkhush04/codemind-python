s=input()
s=s.split(" ")
temp=999
res=0
for word in s:
    c=0
    word=list(word)
    for i in word:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            c=c+1
    if(c<=temp):
        temp=c
for word in s:
    x=0
    word=list(word)
    for i in word:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            x=x+1
    if(x==temp):
        res=res+1
print(res)
    
    
            