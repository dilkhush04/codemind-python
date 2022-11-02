a,b=map(int,input().split())
a=str(a)
print(abs(int(a[0:b])-int(a[len(a)-b:])))