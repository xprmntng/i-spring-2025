from heapq import heappop, heappush, heapify

NEIGHBOR_DELTAS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

def two_tuple_add(t1, t2):
    t1a, t1b = t1
    t2a, t2b = t2
    return (t1a + t2a, t1b + t2b)


def walkable(point):
    return grid[point].symbol != '#'


def neighbors_from(point):
    neighbors = []
    for n in NEIGHBOR_DELTAS:
        n = two_tuple_add(n, point)
        if walkable(n):
            neighbors.append(n)
    return neighbors


class Tile():
    def __init__(self, symbol):
        self.prev = None
        self.symbol = symbol


def point_in_heap(h, needle_point):
    for i in range(len(h)):
        cost, point = h[i]
        if point == needle_point:
            return i, cost
    return None, None


def edge_cost(u_point, v_point):
    u_symbol = grid[u_point].symbol
    u_r, u_c = u_point
    v_r, v_c = v_point
    up = v_r < u_r
    down = v_r > u_r
    left = v_c < u_c
    right = v_c > u_c
    if up:
        if u_symbol == '^':
            return 0.5
        if u_symbol == 'v':
            return 2.0
        return 1.0
    if down:
        if u_symbol == 'v':
            return 0.5
        if u_symbol == '^':
            return 2.0
        return 1.0
    if left:
        if u_symbol == '<':
            return 0.5
        if u_symbol == '>':
            return 2.0
        return 1.0
    if right:
        if u_symbol == '>':
            return 0.5
        if u_symbol == '<':
            return 2.0
        return 1.0
    return 1.0


def uniform_cost_search(start, goal):
    '''
    Adapted from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Practical_optimizations_and_infinite_graphs
    '''
    u = (0, start)
    frontier = [u]
    expanded = set()
    while True:
        if len(frontier) == 0:
            return None
        u = heappop(frontier)
        u_cost, u_point = u
        if u_point == goal:
            return u_cost
        expanded.add(u_point)
        for v_point in neighbors_from(u_point):
            if v_point in expanded:
                continue
            v_heap_index, v_cost = point_in_heap(frontier, v_point)
            u_to_v_cost = edge_cost(u_point, v_point) + u_cost
            if v_heap_index is None:
                v = (u_to_v_cost, v_point)
                heappush(frontier, v)
                grid[v_point].prev = u_point
            elif u_to_v_cost < v_cost:
                v_replacement = (u_to_v_cost, v_point)
                frontier[v_heap_index] = v_replacement
                heapify(frontier)
                grid[v_point].prev = u_point


def get_int():
    return int(input())


def get_ints():
    return map(int, input().strip().split())


time_limit = get_int()
n_cols, n_rows = get_ints()

grid = {}
for r in range(n_rows):
    row = input()
    for c in range(n_cols):
        point = (r, c)
        symbol = row[c]
        grid[point] = Tile(symbol)
        if symbol == 'E':
            goal = point
        elif symbol == 'C':
            start = point

cost_to_reach_goal = uniform_cost_search(start, goal)
if cost_to_reach_goal <= time_limit:
    print('CORA makes it')
else:
    print('CORA does not make it')

# Uncomment to show the path to the goal
# path = str(goal)
# p = grid[goal].prev
# while p is not None:
#     path = str(p) + ' → ' + path
#     p = grid[p].prev
# print(path)
# Uncomment to show the time taken to reach the goal
# print('Cost:', cost_to_reach_goal)