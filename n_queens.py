import time
import matplotlib.pyplot as plt

def is_safe(board, row, col, n):
  for i in range(col):
    if board[row][i] == 1:
      return False

  i = row
  j = col
  while i >= 0 and j >= 0:
    if board[i][j] == 1:
      return False
    i -= 1
    j -= 1

  i = row
  j = col
  while i < n and j >= 0:
    if board[i][j] == 1:
      return False
    i += 1
    j -= 1

  return True

def solve_n_queens(board, col, n):
  if col >= n:
    return True

  for i in range(n):
    if is_safe(board, i, col, n):
      board[i][col] = 1
      if solve_n_queens(board, col + 1, n):
        return True
      board[i][col] = 0

  return False

def print_solution(board):
  for i in range(len(board)):
    for j in range(len(board)):
      print(board[i][j], end=" ")
    print()

def solve(n):
  board = [[0 for _ in range(n)] for _ in range(n)]

  start_time = time.perf_counter()
  if solve_n_queens(board, 0, n):
    end_time = time.perf_counter()
  else:
    print("Solution does not exist")
  return end_time - start_time

n_values = [4, 8, 12, 16, 20] 
execution_times = []
for n in n_values:
  execution_times.append(solve(n))

for i in range(len(n_values)):
  print(f"Execution Time: {execution_times[i]} seconds for n value {n_values[i]}")

plt.figure(figsize=(8, 6)) 
plt.plot(n_values, execution_times, marker='o', linestyle='-')
plt.xlabel("Board Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("N-Queens Problem Execution Time")
plt.grid(True)
plt.show()