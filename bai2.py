def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        max_so_far = a[0]
        curr_max = a[0]
        
        for i in range(1, n):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far, curr_max)
            
        print(max_so_far)

if __name__ == '__main__':
    solve()