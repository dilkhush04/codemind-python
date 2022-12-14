def check(a, n):
    for i in range(1, n - 1):
 
        if ((a[i] > a[i - 1] and a[i + 1] < a[i]) or
            (a[i] < a[i - 1] and a[i + 1] > a[i])):
            continue
        else:
            return False
    return True
n=int(input())
a = list(map(int,input().split()))
wave = (n - 1) // 2
if (check(a, n)):
    print(wave)
else:
    print("-1")