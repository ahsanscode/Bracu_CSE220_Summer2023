# -*- coding: utf-8 -*-
"""LAB2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SkBuxD3GyEOI35zJtki76TePDsbx0JVz

**Instructions to Follow (Failing to follow these will result mark penalties).**


1.   You can not use any built-in function except len()
2.   You can not use any other python collections except array (e.g: tuptle, dictionaries etc.). 
3. We will initialize a new array using numpy library. We have to mention the fixed size during initialization. There might be two approach.

  i. arr = np.zeros((10), dtype = int) #Initializing an array length 10 with values 0

  ii. arr = np.array([10, 20, 30, 40]) #Initializing an array length 4 with the values.
4. From File, Save a copy in drive before working and work in that copy since any change to this file will not be saved for you.
"""



# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

#You must run this cell to print matrix and for the driver code to work
def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))

"""Task 1: Zigzag Walk"""

def walk_zigzag(floor):
    # To Do
    row, col = floor.shape
    for var in range(row):
      if var % 2 == 0:
        for varx in range(0,col,2):
          print(floor[var][varx],end=' ')
      if var % 2 != 0:
        for varx in range(col-1,-1,-2):
          print(floor[var][varx],end=' ')
      print()  
    


floor = np.array([[ '3W' , '8B' , '4W' , '6B' , '1W' , '5B'],['3B' , '2W' , '1B' , '6W' , '3B' , '8W'],
                  ['9W' , '0B' , '7W' , '5B' , '3W' , '8B'],['2B' , '1W' , '3B' , '6W' , '0B' , '4W'],
                   ['1W' , '4B' , '2W' , '8B' , '6W' , '6B']])
print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3W 4W 1W 
# 8W 6W 2W 
# 9W 7W 3W 
# 4W 6W 1W 
# 1W 2W 6W

"""Task 2: Landscape Screen"""

def landscape(m):
  #To Do
  row,col = m.shape
  new_array = np.zeros((col,row),dtype=int)
  for var in range(row):
    for varx in range(col):
      new_array[varx][var] = m[var][varx]
  return new_array


m = np.random.randint(15,size=(4,3)) #This creates an np array of 4 x 3 where the values are random numbers from [0,15) range
print_matrix(m)
print()
print_matrix(landscape(m))

"""Task 3: Seating Arrangement"""

def arrangement(m, diff):
  #To Do
  row,col = m.shape
  if row != col :
    return False

  for var in range(row):
    for varx in range(col):
      if var == varx:
        continue
      temp = m[var][varx] - m[varx][var]
      if temp<0 :
        temp*=-1
      if  temp != diff :
        return False
  return True
m = np.array([[7,13,9,14],[12,8,15,11],[10,17,3,2],[15,10,1,4]])
print_matrix(m)
print()
returned_value = arrangement(m,1) 
print(returned_value)#This should print False
unittest.output_test(returned_value, False)

"""Task 4: Chess Piece"""

def validation(row,col):
  if 0 > row  or row > 7  or 0 > col or col > 7 :
    return False
  return True

def up_left(matrix,r,c):
  row1 = r-1
  col1 = c-2 
  row2 = r-2
  col2 = c-1 
  a,b = False,False
  if validation(row1,col1):
    a = True
  if validation(row2,col2):
    b = True



  if a == True and b == True: 
    matrix[row1][col1] = 3
    matrix[row2][col2] = 3

  if a == True and b == False: 
    matrix[row1][col1] = 3

  if a == False and b == True: 
    matrix[row2][col2] = 3


def up_right(matrix,r,c):
  row1 = r-1
  col1 = c+2 
  row2 = r-2
  col2 = c+1 

  a , b = False, False
  if validation(row1,col1):
    a = True
  if validation(row2,col2):
    b = True


  if a == True and b == True: 
    matrix[row1][col1] = 3
    matrix[row2][col2] = 3

  if a == True and b == False: 
    matrix[row1][col1] = 3

  if a == False and b == True: 
    matrix[row2][col2] = 3


def down_left(matrix,r,c):
  row1 = r+1
  col1 = c-2 
  row2 = r+2
  col2 = c-1 
  a,b = False,False

  if validation(row1,col1):
    a = True
  if validation(row2,col2):
    b = True


  if a == True and b == True: 
    matrix[row1][col1] = 3
    matrix[row2][col2] = 3

  if a == True and b == False: 
    matrix[row1][col1] = 3

  if a == False and b == True: 
    matrix[row2][col2] = 3

def down_right(matrix,r,c):
  row1 = r+1
  col1 = c+2 
  row2 = r+2
  col2 = c+1 
  a,b = False,False

  if validation(row1,col1):
    a = True
  if validation(row2,col2):
    b = True


  if a == True and b == True: 
    matrix[row1][col1] = 3
    matrix[row2][col2] = 3

  if a == True and b == False: 
    matrix[row1][col1] = 3

  if a == False and b == True: 
    matrix[row2][col2] = 3





def show_knight_move(knight):
  #To Do
  r,c = knight
  matrix = np.zeros((8,8),dtype=int)
  if validation(r,c):
    matrix[r][c] = 33
    up_left(matrix,r,c)
    up_right(matrix,r,c)
    down_left(matrix,r,c)
    down_right(matrix,r,c)


  

  
  
  return matrix


knight = (3,4)
chess_board = show_knight_move(knight)
print_matrix(chess_board)

"""Bonus Task (UNGRADED)"""

def topple(knight,rook):
  #To Do
  return None


knight = (5,6)
rook = (5,1)9*
chess_board, ans = topple(knight,rook)
print_matrix(chess_board)
print(ans) #This should print Rook can kill