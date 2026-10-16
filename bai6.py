import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    
    dp = [0] * 105
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, 105):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    out = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        out.append(str(dp[n]))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()