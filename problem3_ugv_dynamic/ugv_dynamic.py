import heapq
import random

GRID_SIZE = 20

def generate_grid(density=0.2):
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < density:
                grid[i][j] = 1
    return grid


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    pq = [(0, start)]
    came_from = {}
    cost = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        x, y = current
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx, ny in neighbors:
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                if grid[nx][ny] == 1:
                    continue

                new_cost = cost[current] + 1
                next_node = (nx, ny)

                if next_node not in cost or new_cost < cost[next_node]:
                    cost[next_node] = new_cost
                    priority = new_cost + heuristic(goal, next_node)
                    heapq.heappush(pq, (priority, next_node))
                    came_from[next_node] = current

    return came_from


def add_dynamic_obstacle(grid):
    x = random.randint(0, GRID_SIZE-1)
    y = random.randint(0, GRID_SIZE-1)
    grid[x][y] = 1


def navigate(grid, start, goal):
    current = start

    while current != goal:
        path = astar(grid, current, goal)

        if goal not in path:
            print("No path found!")
            return

        print("Recalculating path...")
        add_dynamic_obstacle(grid)
        current = goal


if __name__ == "__main__":
    grid = generate_grid(0.2)
    navigate(grid, (0,0), (19,19))
