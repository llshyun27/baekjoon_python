n,k = map(int,input().split())
data = list(input())
cnt =0
for i in range(n):
    if data[i] =='P':
        for j in range(max(i-k,0),min(i+k+1,n)):
            if data[j]=='H':
                data[j] =0
                cnt +=1
                break
print(cnt)
                