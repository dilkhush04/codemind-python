n=int(input())
for i in range(n):
    test_str = input()
    res = any(chr.isdigit() for chr in test_str)
    if(res==1):
        print("Yes")
    else:
        print("No")