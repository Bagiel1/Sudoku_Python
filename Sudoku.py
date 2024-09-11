import random
import copy
import time

sudoku_=[[5,0,0,0,0,0,0,0,0],
         [7,0,0,2,0,0,0,0,1],
         [3,0,0,0,0,0,6,9,0],
         [8,0,5,0,0,2,0,0,0],
         [0,0,0,8,4,0,0,0,2],
         [0,0,0,0,0,0,8,0,0],
         [0,0,0,1,8,0,3,6,0],
         [0,0,3,0,0,0,0,8,7],
         [0,0,0,0,0,0,1,2,0]]


def verificar(lin,col,sudoku):

    if sudoku[lin][col]==0:
       return True
    for c in range(9):
        if c != col and sudoku[lin][col] == sudoku[lin][c]:
             return False

    for l in range(9):
        if l!= lin and sudoku[lin][col] == sudoku[l][col]:
            return False

    linhainicial= 3* (lin//3)
    colunainicial= 3* (col//3)
    for p in range(linhainicial, linhainicial+3):
        for d in range(colunainicial, colunainicial+3):
            if sudoku[p][d] == sudoku[lin][col] and (p,d)!=(lin,col):
                return False

    return True

def backtracking(sudoku,tempol,tempolimite):
  if tempolimite > 10:
    return False
  for linhas in range(9):
      for colunas in range(9):
          if sudoku[linhas][colunas]==0:
              for num in range(1,10):
                  sudoku[linhas][colunas]= num
                  tempolimite=time.time()-tempol
                  if verificar(linhas,colunas,sudoku):
                      if backtracking(sudoku,tempol,tempolimite):
                          return True
                  sudoku[linhas][colunas]=0
              return False
  return True