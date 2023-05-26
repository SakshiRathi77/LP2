from heapq import heappop, heappush

# A* Algorithm
def astar(start_state, goal_state, get_neighbors_fn, heuristic_fn):
    open_set = [(0, start_state)]  # Priority queue of states
    came_from = {}  # Parent pointers
    g_score = {start_state: 0}  # Cost to reach a state
    f_score = {start_state: heuristic_fn(start_state, goal_state)}  # f = g + h

    while open_set:
        _, current_state = heappop(open_set)

        if current_state == goal_state:
            return reconstruct_path(came_from, current_state)

        for neighbor in get_neighbors_fn(current_state):
            tentative_g_score = g_score[current_state] + 1  # Assuming uniform cost for each move

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_state
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic_fn(neighbor, goal_state)
                heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found


# Helper function to reconstruct the path from the start state to the goal state
def reconstruct_path(came_from, current_state):
    path = [current_state]
    while current_state in came_from:
        current_state = came_from[current_state]
        path.append(current_state)
    return path[::-1]  # Reverse the path


# Example usage
# Define the game board as a grid of cells (e.g., '0' represents an empty cell, '1' represents a wall, etc.)
game_board = [
    ['0', '0', '1', '0', '0'],
    ['0', '1', '1', '0', '0'],
    ['0', '0', '0', '0', '1'],
    ['0', '1', '1', '0', '0'],
    ['0', '0', '0', '0', '0']
]

start_state = (0, 0)  # Starting position
goal_state = (4, 4)  # Goal position

# Define the function to get neighboring states for a given state
def get_neighbors(state):
    neighbors = []
    row, col = state

    # Check the neighboring cells (up, down, left, right)
    if row > 0 and game_board[row - 1][col] == '0':
        neighbors.append((row - 1, col))
    if row < len(game_board) - 1 and game_board[row + 1][col] == '0':
        neighbors.append((row + 1, col))
    if col > 0 and game_board[row][col - 1] == '0':
        neighbors.append((row, col - 1))
    if col < len(game_board[0]) - 1 and game_board[row][col + 1] == '0':
        neighbors.append((row, col + 1))

    return neighbors

# Define the heuristic function (Manhattan distance)
def heuristic(state, goal_state):
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

# Use A* algorithm to find the path
path = astar(start_state, goal_state, get_neighbors, heuristic)

if path is not None:
    print("Path found:")
    for state in path:
        print(state)
else:
    print("No path found.")
    
