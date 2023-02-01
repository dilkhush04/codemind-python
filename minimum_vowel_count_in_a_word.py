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
print(temp)

    
    
            