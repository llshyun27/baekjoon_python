#물이 새는 곳의 개수 n, 테이프의 길이 l이 주어진다.
n,l = map(int,input().split())

#물이 새는 곳의 위치가 주어진다.
loc = list(map(int,input().split()))
loc.sort()
start = loc[0]
count = int(0)

#항승이가 필요한 테이프의 개수를 구한다.
for i in range(1,n):
    if(loc[i]-start>=l):
        count +=1
        start = loc[i]

print(count+1)