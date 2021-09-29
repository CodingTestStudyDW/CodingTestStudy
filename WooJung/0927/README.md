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


## BFS(너비 우선 탐색)
- 큐를 이용하여 문제 풀이 가능
- 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
- 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리함
- 2번의 과정을 더이상 수행할 수 없을 때까지 반복


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
