def is_valid(board, row, col, n):
    # Check if a queen can be placed at the given position
    for i in range(row):
        if board[i][col] == 1:
            return False
        for j in range(n):
            if board[i][j] == 1 and (abs(i - row) == abs(j - col) or j == col):
                return False
    return True

def backtrack(board, row, n, solutions):
    if row == n:
        # All queens have been placed, add the solution
        solution = []
        for i in range(n):
            solution.append(board[i][:])
        solutions.append(solution)
    else:
        for col in range(n):
            if is_valid(board, row, col, n):
                board[row][col] = 1
                backtrack(board, row + 1, n, solutions)
                board[row][col] = 0

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]  # Initialize the board
    solutions = []  # Store the solutions
    backtrack(board, 0, n, solutions)
    return solutions

def calculate_cost(solution):
    # Calculate the cost of a solution
    cost = 0
    n = len(solution)
    for i in range(n):
        for j in range(i + 1, n):
            if solution[i][j] == 1:
                cost += 1
    return cost

def branch_and_bound_n_queens(n):
    solutions = solve_n_queens(n)
    best_solution = None
    min_cost = float('inf')
    for solution in solutions:
        cost = calculate_cost(solution)
        if cost < min_cost:
            min_cost = cost
            best_solution = solution
    return best_solution

# Example usage
n = 8  # Number of queens
solution = branch_and_bound_n_queens(n)
if solution is not None:
    print("Solution found:")
    for row in solution:
        line = ["Q" if cell == 1 else "." for cell in row]
        print(" ".join(line))
else:
    print("No solution found.")


