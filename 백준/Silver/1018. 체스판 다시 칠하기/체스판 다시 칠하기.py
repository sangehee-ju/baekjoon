import sys


# 8 * 8로 자른 보드를 다시 칠하는 횟수
def repaint(board):
    cnt = 0
    for i in range(7):
        for j in range(7):
            if board[i][j] == board[i + 1][j] == 'W':
                board[i + 1][j] = 'B'
                cnt += 1
            elif board[i][j] == board[i + 1][j] == 'B':
                board[i + 1][j] = 'W'
                cnt += 1

            if board[i][j] == board[i][j + 1] == 'W':
                board[i][j + 1] = 'B'
                cnt += 1
            elif board[i][j] == board[i][j + 1] == 'B':
                board[i][j + 1] = 'W'
                cnt += 1
    return cnt


N, M = map(int, sys.stdin.readline().split())

board = []
temp = []

for _ in range(N):
    board.append(sys.stdin.readline())

for i in range(N - 7):
    for j in range(M - 7):
        idx1 = 0
        idx2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W': idx1 += 1
                    if board[a][b] != 'B': idx2 += 1
                else:
                    if board[a][b] != 'B': idx1 += 1
                    if board[a][b] != 'W': idx2 += 1
        temp.append(idx1)
        temp.append(idx2)

print(min(temp))