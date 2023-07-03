from collections import deque

#전체 사람의 수
n = int(input())
#촌수 계산해야하는 두사람의 번호
a,b = map(int,input().split())
#부모 자식들간의 관계의 개수 
m = int(input())
#부모 자식 관계 입력받기
graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    s,e = map(int,input().split())
    #양방향 연결
    graph[s].append(e)
    graph[e].append(s)

def bfs(a,b):
    queue = deque([a])  #큐에서 첫번째 원소를 빼낸다.
    while queue:
        c = queue.popleft()
        if c ==b:
            return visited[b]

        for i in graph[c]: #연결되어 있는 경우, 미방문이면 방문하기
            if visited[i] ==False:
                queue.append(i)
                visited[i] = visited[c]+1
    return -1
               


print(bfs(a,b))
