# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

def dijkstra(graph, start):
    def get_parents(a, parents):
        if parents[a] == -1:
            return []
        else:
            return get_parents(parents[a], parents) + [parents[a]]

    inf = float('inf')
    length = len(graph)
    is_visited = [False] * length
    cost = [inf] * length
    parent = [-1] * length
    cost[start] = 0
    min_cost = 0

    while min_cost < inf:
        is_visited[start] = True

        for b, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[b]:
                if cost[b] > vertex + cost[start]:
                    cost[b] = vertex + cost[start]
                    parent[b] = start

        min_cost = inf
        for c in range(length):
            if min_cost > cost[c] and not is_visited[c]:
                min_cost = cost[c]
                start = c

    ways = {d: get_parents(d, parent) + [d] if cost[d] != inf else None for d in range(length)}

    return cost, ways


g = [[1, 0, 1, 1, 9, 0, 0, 0],
     [1, 0, 11, 4, 0, 0, 55, 0],
     [0, 9, 0, 0, 53, 0, 6, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 50, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 5, 0],
     [0, 0, 20, 0, 8, 1, 0, 0],
     [0, 0, 0, 0, 0, 3, 2, 0],
     ]

s = int(input('От какой вершины идти: '))
c, w = dijkstra(g, s)

print(f'Путь от вершины {s}:')
for i in range(len(g)):
    if i != s:
        if c[i] == float('inf'):
            print(f' - до вершины {i}: стоимость ∞, нет доступных маршрутов!')
        else:
            print(f' - до вершины {i}: стоимость {c[i]}, маршрут: {w[i]}')
