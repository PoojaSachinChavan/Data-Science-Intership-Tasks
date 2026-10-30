# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:52:38 2026

@author: POOJA
"""

N = 8 
board = [["-" for _ in range(N)] for _ in range(N)] 
# First Queen is already placed 
board[0][0] = "Q" 
def is_safe(row, col): 
    for i in range(row): 
        if board[i][col] == "Q": 
            return False 
    i, j = row - 1, col - 1 
    while i >= 0 and j >= 0: 
        if board[i][j] == "Q": 
            return False 
        i -= 1 
        j -= 1 
    i, j = row - 1, col + 1 
    while i >= 0 and j < N: 
        if board[i][j] == "Q": 
            return False 
        i -= 1 
        j += 1 
    return True 
 
def solve(row): 
    if row == N: 
        return True 
 
    if row == 0: 
        return solve(row + 1) 
    for col in range(N): 
        if is_safe(row, col): 
            board[row][col] = "Q" 
 
            if solve(row + 1): 
                return True 
            board[row][col] = "-" 
    return False 
solve(0) 
print("8-Queens Matrix:") 
for row in board: 
    print(" ".join(row)) 