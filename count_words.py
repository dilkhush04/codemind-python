s=input()
c=0
lst=['a','e','i','o','u','A','E','I','O','U']
s=s.split(" ")
for i in s:
    if i[0] in lst and i[len(i)-1] not in lst:
        c=c+1
print(c)