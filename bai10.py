import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    q = int(input_data[1])
    
    pref = [0] * (n + 1)
    for i in range(n):
        val = int(input_data[2 + i])
        pref[i + 1] = pref[i] + (val if val > 0 else 0)
        
    out = []
    idx = 2 + n
    for _ in range(q):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        out.append(str(pref[r] - pref[l - 1]))
        idx += 2
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()