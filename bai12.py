def solve(n, max_val, current_sum, path, result):
    if current_sum == n:
        result.append(f"({', '.join(map(str, path))})")
        return
    
    for i in range(min(max_val, n - current_sum), 0, -1):
        solve(n, i, current_sum + i, path + [i], result)

t = int(input())
for _ in range(t):
    n = int(input())
    result = []
    solve(n, n, 0, [], result)
    print(" ".join(result))