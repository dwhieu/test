import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n= int(input_data[0])
    k=int(input_data[1])

    a= [int(x) for x in input_data[2:2+n]]

    coun = 0

    def quaylui(i, sum, subset):
        nonlocal coun
        if i==n:
            if sum==k:
                print(*sum)
                coun+=1
                return
        quaylui(i+1,sum,subset)
        if sum<k:
            quaylui(i+1, sum + a[i] , subset + [a[i]])
    quaylui(0,0,[])
    print(coun)
if __name__ =='__main__':
    solve()