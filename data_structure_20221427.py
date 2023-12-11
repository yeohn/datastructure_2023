import heapq

def create_priority_graph(num_nodes, priority_order, node_weights, unreachable_nodes):
    graph = {}
    for i in range(len(priority_order) - 1):
        current_node = priority_order[i]
        next_node = priority_order[i + 1]
        if current_node not in graph:
            graph[current_node] = {}
        if next_node not in unreachable_nodes:
            graph[current_node][next_node] = node_weights[current_node] # 다음 노드에 대한 가중치 설정
        else:
            graph[current_node][next_node] = float('inf') # 지나가지 않는 노드와 연결된 간선의 가중치를 무한대로 설정
    return graph
def dijkstra_priority(graph, start, end):
    distances = {node: {'distance': float('inf'), 'prev': None} for node in graph}
    distances[start]['distance'] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]['distance']:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]['distance']:
                distances[neighbor]['distance'] = distance
                distances[neighbor]['prev'] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    path = []
    current = end
    while current is not None and current in distances:
        path.insert(0, current)
        current = distances[current]['prev'] if 'prev' in distances[current] else None
    return path

# 노드의 우선순위 정의 (작품 번호로 표현)
priority_order = list(range(1, 34))

# 각 노드별 가중치 정의
node_weights = {
    1: 2, 2: 3, 3: 1, 4: float('inf'), 5: float('inf'),
    6: float('inf'), 7: 1, 8: float('inf'), 9: 1, 10: float('inf'),
    11: float('inf'), 12: float('inf'), 13: float('inf'), 14: float('inf'), 15: 4,
    16: float('inf'), 17: 1, 18: float('inf'), 19: 3, 20: float('inf'),
    21: float('inf'), 22: 1, 23: float('inf'), 24: float('inf'), 25: 2,
    26: float('inf'), 27: float('inf'), 28: float('inf'), 29: 3, 30: float('inf'),
    31: 1, 32: float('inf'), 33: float('inf')
}

# 지나가지 않는 노드 정의
unreachable_nodes = [4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 21, 24, 26, 27, 28, 30, 32]

# 노드 간의 우선순위 그래프 생성
node_graph = create_priority_graph(len(priority_order), priority_order, node_weights, unreachable_nodes)

# 전시관과 종료 노드 설정
start_exhibition = int(input("전시관을 입력하세요: "))
start_node = start_exhibition * 2 - 1  # 각 전시관의 첫 번째 작품의 노드 번호
end_node = 33

# 다익스트라 알고리즘을 이용한 최단 우선순위 경로 계산
priority_path = dijkstra_priority(node_graph, start_node, end_node)

# 최단 경로 출력
print(f"제{start_exhibition}전시관의 {start_node}번 작품부터 {end_node}번 작품까지의 최단 우선순위 경로:")
for i, node in enumerate(priority_path):
    print(f"{node}", end="")
    if i < len(priority_path) - 1:
        print(" -> ", end="")
print()
print(f"마지막 작품: {end_node}번")