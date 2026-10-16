t = int(input())
MOD = 10**9 + 7
for _ in range(t):
    n = int(input())
    ans = 1
    for i in range(1, 10):
        ans = ans * (n + i) // i
    print(ans % MOD)