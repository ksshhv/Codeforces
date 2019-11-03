b = int(input())
g = int(input())
n = int(input())
resd = 0
if b+g == n:
    resd = 1
else:
    mn = min(b, g)
    if mn < n:
        resd = mn + 1
    else:
        resd = n + 1
print(res)
