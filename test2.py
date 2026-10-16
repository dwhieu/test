import sys
from itertools import permutations

def solve():
    input_data=sys.stdin.read().split()
    if not input_data:
        return
    n= int(input_data[0])
    write = sys.stdout.write
    for i, p in enumerate(permutations(range(1,n+1)),1):
        write(f"{i}: "+" ".join(map(str, p))+ "\n")
if __name__=='__main__':
    solve()
