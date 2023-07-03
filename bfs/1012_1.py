from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n or graph[nx][ny]==0:
                continue            
            if graph[nx][ny]==1:  
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return 1

for _ in range(int(input())):
    m,n,k = map(int,input().split())
    graph = [[0 for _ in range(m)]for _ in range(n)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(k):
        a,b = map(int,input().split())
        graph[b][a] =1
    
    for i in range(n):
        for j in range(m):
            cnt =0
            if graph[i][j]==1:
                cnt += bfs(i,j)
    print(cnt)