t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    
    num1 = 0
    num2 = 0
    
    for i in range(n):
        if i % 2 == 0:
            num1 = num1 * 10 + a[i]
        else:
            num2 = num2 * 10 + a[i]
            
    print(num1 + num2)