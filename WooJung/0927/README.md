# DFS && BFS
- 탐색을 시작할 정점의 번호는 V
- 입력으로 주어지는 간선은 양방향


## DFS(깊이 우선 탐색)
- 스택과 재귀를 이용하여 문제 풀이 가능
- 시작 노드에서 인접한 노드 중 숫자가 작은 노드를 선택하여 방문처리 하고 탐색을 들어감
- 더 이상 탐색할 점이 없다면 연결되어있는 점들 중 방문하지 않고 다음으로 큰 노드를 탐색함


```python
def bfs(v):
  # 시작하는 정점
  print(v, end = '')
  # visit의 리스트에 1이라 표기
  visit[v] = 1
  for i in range(1, n+1):
    # 가지 않은 점인데, 이어진 구간일때
    if visit[i] == 0 and s[v][i] == 1:
      dfs(i)
```
```python
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph_list, root_node))
```

## BFS(너비 우선 탐색)
**시작점인 루트노드와 같은 거리에 있는 노드를 우선으로 방문**
- 큐를 이용하여 문제 풀이 가능
- 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
- 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리함
- 2번의 과정을 더이상 수행할 수 없을 때까지 반복
  - 노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보만 큐에 넣어 먼저 큐에 들어있던 노드부터 방문하면 되는 것


```python
def bfs(v):
  queue = [v]
  visit[v] = 0
  # queue가 작동되고 있는 동안
  while(queue):
    v = queue[0]
    print(v, end = '')
    del queue[0]
    for i in range(1, n+1):
      if visit[i] == 1 and s[v][i] == 1:
        queue.append(i)
        visit[i] = 0
```

```python
from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
  
print(BFS_with_adj_list(graph_list, root_node))
```

```python
## 미로 찾기

from collections import deque

def bfs(x,y):
  # bfs이므로 큐 사용
  queue=deque()
  queue.append((x,y))
  # 큐가 빌 때까지 반복
  while queue:
    x,y=queue.popleft()
    # 현재 위치에서 상,하,좌,우 확인
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      # 공간을 벗어난 경우 무시
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      # 괴물이 있는 경우 무시
      if graph[nx][ny]==0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 +1해서 최단기록
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
  # 가장 오른쪽 아래까지의 최단거리 반환
  return graph[n-1][m-1]

n,m=map(int, input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int, input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))

```

![image](https://user-images.githubusercontent.com/72767245/135285786-685207aa-8f34-43e0-9b70-1473eb99755a.png)


