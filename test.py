def check(s):
    return s == s[::-1]
def Try(i,n,s):
    if i==n:
        if check(s):
            print(*s)
        return
    Try(i+1,n,s+"0")
    Try(i+1,n,s+"1")
if __name__ == "__main__":
    n=int(input().strip())
    Try(0,n,"")