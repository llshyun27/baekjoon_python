# 섬과 바다로 이루어진 지도가 주어진다.
# 섬의 개수를 세는 프로그램을 작성한다.
# 가로, 세로, 대각선 연결 땅이면 같은 섬이다.
# 1은 땅, 0은 바다이다.

from collections import deque

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=h or ny>=w:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return 1

while True:
    w,h = map(int,input().split()) 
    if w ==0 and h ==0:
        break
    graph =[]
    cnt =0
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] ==1:
                cnt += bfs(i,j)

    print(cnt)