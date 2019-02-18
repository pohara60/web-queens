# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:45:35 2018

@author: pohara
"""
import copy

def print_queens( board, r ):

    # Allocate initial board
    if board is None:
        board = []
        for r1 in range(8):
            row = []
            for c in range(8):
                row.append(' ')
            board.append(row)
    
    # Full board?
    if r == 8:
#        for r1 in range(8):
#            for c in range(8):
#                print board[r1][c],
#            print       
        yield 1
        return 1
    
    # Place queen in each valid column
    for c in range(8):
        if board[r][c] == ' ':
            board2 = copy.deepcopy(board)
            board2[r][c] = 'x'
            for r2 in range(r+1,8):
                board2[r2][c] = '|'
                if c+r2-r < 8:
                    board2[r2][c+r2-r] = '\\'
                if c-r2+r >= 0:
                    board2[r2][c-r2+r] = '/'
            yield from print_queens(board2, r+1)
    return 0

board = None
r = 0
def main():
    generator = print_queens(board, r)
    count = 0
    for i in generator:
        count = count+i
    print(count)

if __name__ == '__main__':
    main()
