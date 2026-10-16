from itertools import product

t = int(input())
for _ in range(t):
    n = int(input())
    res = [''.join(x) for x in product('AB', repeat=n)]
    print(*res)