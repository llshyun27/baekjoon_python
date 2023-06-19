from collections import deque
number = int(input())
pair = int(input())
graph = [[]for i in range(number+1)]
visited = [False]*(number+1) # 모든 노드를 미방문처리

for i in range(pair):
    s,e = map(int,input().split())
    #양방향 연결   
    graph[s].append(e)
    graph[e].append(s)

def bfs(graph,start,visited):
    count =int(0)
    queue = deque([start])  #큐에서 첫번째 원소를 빼낸다. 
    visited[start] = True  #현재 노드를 방문처리
    while queue:
        v = queue.popleft() #큐에서 하나의 원소를 뽑는다.
        visited[v] = True  #현재 노드를 방문 처리

        for i in graph[v]:  #해당 원소와 연결되어 있지만
            if visited[i] ==False: #방문하지 않았으면
                queue.append(i) #큐에 삽입
                visited[i] = True #방문처리
                count+=1  
    print(count)

bfs(graph,1,visited)