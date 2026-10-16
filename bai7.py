import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        s = int(input_data[idx+1])
        idx += 2
        
        dp = 1
        for _ in range(n):
            dp |= (dp << int(input_data[idx]))
            idx += 1
            
        if (dp >> s) & 1:
            out.append("YES")
        else:
            out.append("NO")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()