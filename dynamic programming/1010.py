#테스트케이스의 수
n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    m1 = min(a,b)
    m2 = max(a,b)
    mom = m2
    l = m2
    for _ in range(m1-1):
        l = l-1
        mom = mom * l
    son = m1
    l = m1
    for _ in range(m1-1):
        l = l-1
        son = son *l 
    result = int(mom/son)
    print(result)
        
