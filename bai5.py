t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(key=lambda val: abs(x - val))
    print(*a)