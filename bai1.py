def solve():
    t = int(input())
    for _ in range(t):
        n= int(input())
        def backtrack(current_str):
            if len(current_str) == n :
                print(current_str)
                return
            if len(current_str) == 0:
                backtrack("H")
            elif len(current_str) == n-1:
                backtrack(current_str + "A")
            else:
                backtrack(current_str + "A")
                if current_str[-1] != 'H':
                    backtrack(current_str + "H")
        backtrack("")
if __name__ == '__main__':
    solve()      