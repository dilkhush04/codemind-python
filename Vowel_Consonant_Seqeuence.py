s=input()
arr=[]
for i in range(len(s)):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        arr.append('V')
    else:
        arr.append('C')
ch=arr[0]
print(ch,end='')
for i in range(1,len(arr),1):
    if arr[i]!=ch:
        print(arr[i],end='')
    ch=arr[i]
    