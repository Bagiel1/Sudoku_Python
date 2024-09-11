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

def contar_zeros(matriz):
    contador= 0
    for i in matriz:
        contador += i.count(0)
    return contador



def criar():
    tentativas=0
    while tentativas<=2000000:
        tentativas+=1
        novo_sudoku= [[0 if random.random()<0.6 else random.randint(1,9) for _ in range(9)] for _ in range(9)]
        for i in range(9):
          for j in range(9):
            if verificar(i,j,novo_sudoku) == False:
              novo_sudoku= [[0 for _ in range(9)] for _ in range(9)]


        if contar_zeros(novo_sudoku) >= 40 and contar_zeros(novo_sudoku) <= 60:
            teste= copy.deepcopy(novo_sudoku)
            if backtracking(novo_sudoku,time.time(),0):
                print("Solução encontrada após "+str(tentativas)+" tentativas")
                for i in teste:
                  print(i)
                print('\n')
                return  novo_sudoku
            else:
                print("Tentativa Falhou")
    print("Não foi possível criar um sudoku")
    return None



criar()




